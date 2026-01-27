import subprocess

COMMANDS = [
    ["netsh", "int", "ip", "reset"],
    ["netsh", "int", "tcp", "reset"],
    ["netsh", "winsock", "reset"],
    ["ipconfig", "/flushdns"],
    ["ipconfig", "/registerdns"],
    ["ipconfig", "/release"],
    ["ipconfig", "/renew"],
]

def main():
    for cmd in COMMANDS:
        subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    main()
