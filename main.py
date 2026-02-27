import sys
import ctypes
import atexit
import defragmentation
import update
import tcp_ip_reset
import security
import repair_system
import subprocess
import time

ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002

def offline_scan():
    subprocess.run(
        ["powershell", "-NoProfile", "-Command", "Start-MpWDOScan"],
        check=True
    )

def prevent_sleep_enable():
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
    )

def prevent_sleep_disable():

    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False

def relaunch_as_admin():
    print("Solicitando privilégios de administrador...")
    params = " ".join([f'"{arg}"' for arg in sys.argv])
    ctypes.windll.shell32.ShellExecuteW(
        None,
        "runas",
        sys.executable,
        params,
        None,
        1
    )
    sys.exit(0)

def main():
    if not sys.platform.startswith("win"):
        print("Este programa só funciona no Windows.")
        sys.exit(1)

    if not is_admin():
        relaunch_as_admin()

    print("\n=== INICIANDO MANUTENÇÃO DO SISTEMA ===\n")

    prevent_sleep_enable()
    atexit.register(prevent_sleep_disable)

    try:
        repair_system.main()
        update.main()
        defragmentation.main()
        security.main()
        tcp_ip_reset.main()
        print("\n=== MANUTENÇÃO FINALIZADA ===\n")
        time.sleep(5)
        print("O computador será reiniciado em 10 segundos...")
        time.sleep(10)
        offline_scan()

    finally:
        prevent_sleep_disable()

if __name__ == "__main__":
    main()

    