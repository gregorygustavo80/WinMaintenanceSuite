import subprocess

def update():
    subprocess.run(["winget", "upgrade", "--all", "-r"], shell=True)

def main():
    update()
   
if __name__ == "__main__":
    main()
