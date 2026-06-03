import platform, threading, time
from logger_win import run_win_logger
from logger_linux import run_linux_logger

stop_event = threading.Event()

def main():
    print(f"[*] Engine Active: {platform.system()}")
    target = run_win_logger if platform.system() == "Windows" else run_linux_logger
    t = threading.Thread(target=target, args=(stop_event,), daemon=True)
    t.start()
    
    try:
        while True: time.sleep(1)
    except KeyboardInterrupt:
        print("\n[!] Signaling suspension and flushing buffers...")
        stop_event.set()
        t.join()
        print("[+] Session closed. Log file generated.")

if __name__ == "__main__":
    main()
