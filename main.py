import time
import os
import sys
import ctypes
import defragmentation
import update
import tcp_ip_reset
import security
import repair_system

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
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

if __name__ == "__main__":

    if not sys.platform.startswith("win"):
        print("Este programa só funciona no Windows.")
        sys.exit(1)

    if not is_admin():
        relaunch_as_admin()

    print("\n=== INICIANDO MANUTENÇÃO DO SISTEMA ===\n")

    #defragmentation.main()
    #update.main()
    #tcp_ip_reset.main()
    #repair_system.main()
    security.main()
   
