import os
import subprocess
import time

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

def restart_computer():
    print("O computador será reiniciado para concluir as alterações...")
    time.sleep(10)
    os.system("shutdown /r /t 0")

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
