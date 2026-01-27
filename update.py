import subprocess
import threading
import itertools
import time
import sys

def update_apps():
    subprocess.run(["winget", "upgrade", "--all",])

def windows_update(): 

    ps_script = r"""
    if (-not (Get-Module -ListAvailable -Name PSWindowsUpdate)) {
        Install-Module PSWindowsUpdate -Force -Confirm:$false
    }

    Import-Module PSWindowsUpdate

    Get-WindowsUpdate -Install -AcceptAll -IgnoreReboot
    """
    stop_event = threading.Event()
    t = threading.Thread(target=spinner, args=(stop_event,))
    t.start()

    subprocess.run(
        ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", ps_script],
        check=True)
        
    stop_event.set()
    t.join()
    

def spinner(stop_event):
    for char in itertools.cycle("|/-\\"):
        if stop_event.is_set():
            break
        sys.stdout.write(f"\rIniciando Windows Update... {char}")
        sys.stdout.flush()
        time.sleep(0.2)
    sys.stdout.write("\rExecutando Windows Update... concluído ✔\n")

def main():
    update_apps()
    windows_update()

if __name__ == "__main__":
    main()
