import subprocess
import threading
import itertools
import time
import sys

def update_data():
    subprocess.run(
        ["powershell", "-Command", "Update-MpSignature -Verbose"],
        shell=True
    )

def quickscan():
    subprocess.run(
        ["powershell", "-Command", "Start-MpScan -ScanType QuickScan"],
        shell=True
    )

def mrt():
    print("Executando o Microsoft Malicious Software Removal Tool (MRT)...") 
    
    stop_event = threading.Event()
    t = threading.Thread(target=spinner, args=(stop_event,))
    t.start()
    
    subprocess.run(["C:\\Windows\\System32\\MRT.exe", "/Q"],shell=False)

    stop_event.set()
    t.join()

def spinner(stop_event):
    for char in itertools.cycle("|/-\\"):
        if stop_event.is_set():
            break
        sys.stdout.write(f"\rExecutando MRT... {char}")
        sys.stdout.flush()
        time.sleep(0.2)
    sys.stdout.write("\rExecutando MRT... concluído ✔\n")


def main():
       update_data()
       quickscan()
       mrt()
              
if __name__ == "__main__":
    main()
