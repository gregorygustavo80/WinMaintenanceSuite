import subprocess

def ip():
    subprocess.run(["netsh", "int", "ip", "reset"], shell=True)

def tcp():
    subprocess.run(["netsh", "int", "tcp", "reset"], shell=True)

def winsock():
    subprocess.run(["netsh", "winsock", "reset"], shell=True)

def flush():
    subprocess.run(["ipconfig", "/flushdns"], shell=True)

def register():
    subprocess.run(["ipconfig", "/registerdns"], shell=True)

def release():
    subprocess.run(["ipconfig", "/release"], shell=True)

def renew():
    subprocess.run(["ipconfig", "/renew"], shell=True)

def main():

        ip()
        tcp()
        winsock()
        flush()
        register()
        release()
        renew()

if __name__ == "__main__":
    main()
