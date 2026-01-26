import subprocess

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
    
def main():
        update_data()
        quickscan()
  
if __name__ == "__main__":
    main()
