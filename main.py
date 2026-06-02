import platform
import threading
import time
from logger_win import run_win_logger
from logger_linux import run_linux_logger

# Shared event to signal suspension
stop_event = threading.Event()

def main():
    print(f"[*] Initializing {platform.system()} Interception Engine...")
    
    # Select mode based on OS
    if platform.system() == "Windows":
        logger_thread = threading.Thread(target=run_win_logger, args=(stop_event,), daemon=True)
    else:
        logger_thread = threading.Thread(target=run_linux_logger, args=(stop_event,), daemon=True)
    
    logger_thread.start()
    print("[+] Engine operational. Press Ctrl+C to suspend interception.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Signal the thread to stop and finalize logs
        stop_event.set()
        logger_thread.join()
        print("\n[!] Engine suspended. Log data flushed to disk.")

if __name__ == "__main__":
    main()
