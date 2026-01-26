import subprocess
import datetime
import os
import time

DRIVE = "C:"
LOG_DIR = r"C:\Logs"

def run_cmd(cmd, log_file):
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True,
        text=True,
        encoding="cp850"  
    )
    for line in process.stdout:
        print(line, end="")
        log_file.write(line)

def get_media_type(drive_letter):
    ps_cmd = f"""
    $p = Get-Partition -DriveLetter {drive_letter.replace(':','')}
    $disk = Get-Disk -Number $p.DiskNumber
    $phys = Get-PhysicalDisk | Where-Object {{ $_.DeviceId -eq $disk.Number }}

    if ($phys.SpindleSpeed -eq 0) {{
        "SSD"
    }}
    elseif ($disk.MediaType -eq "SSD") {{
        "SSD"
    }}
    else {{
        "HDD"
    }}
    """
    return subprocess.check_output(
        ["powershell", "-NoProfile", "-Command", ps_cmd],
        text=True
    ).strip()

def main():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = os.path.join(LOG_DIR, f"defrag_{DRIVE[0]}_{timestamp}.log")

    with open(log_path, "w", encoding="utf-8") as log:
        log.write(f"Drive: {DRIVE}\n")
        log.write(f"Início: {datetime.datetime.now()}\n")
        log.write("-" * 50 + "\n")

        media_type = get_media_type(DRIVE)
        log.write(f"Tipo de mídia: {media_type}\n")
        log.write("-" * 50 + "\n")

        if media_type.upper() == "SSD":
            print("SSD detectado → Executando Optimize/TRIM")
            log.write("SSD → defrag /O /H /V\n")
            run_cmd(f"defrag {DRIVE} /O /H /V", log)

        else:
            print("HDD detectado → Executando desfragmentação completa")

            log.write("HDD → Consolidação de espaço livre\n")
            run_cmd(f"defrag {DRIVE} /X /H /V", log)

            log.write("\nHDD → Otimização de boot\n")
            run_cmd(f"defrag {DRIVE} /B /H /V", log)

        log.write("\nFinalizado em: " + str(datetime.datetime.now()))

    print(f"\nLog salvo em: {log_path}")

if __name__ == "__main__":
        main()
        time.sleep(10)
    