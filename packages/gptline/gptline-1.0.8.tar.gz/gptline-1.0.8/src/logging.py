import tempfile

LOGGING=True
if LOGGING:
    LOGFILE = tempfile.NamedTemporaryFile(delete=False)
    print(f'Logging to {LOGFILE.name}')

def log(message):
    if not LOGGING:
        return
    if isinstance(message, str):
        message = message.encode()
    LOGFILE.write(message + b"\n")
    LOGFILE.flush()

