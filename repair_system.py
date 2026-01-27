import subprocess

def run_chkdsk():
    subprocess.run(
        "echo S | chkdsk C: /f /r",
        shell=True
    )

def run_dism():
    print("Verificando e reparando a imagem do Windows...")
    subprocess.run(
        ["dism", "/Online", "/Cleanup-Image", "/RestoreHealth"],
        shell=True
    )

def run_sfc():
    print("Verificando a integridade dos arquivos de sistema...")
    subprocess.run(["sfc", "/scannow"], shell=True)

def main():

        run_chkdsk()
        run_dism()
        run_sfc()

if __name__ == "__main__":
    main()
