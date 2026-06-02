def log_key(data):
    with open("log.txt", "a") as f:
        f.write(str(data) + "\n")
