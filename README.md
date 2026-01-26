# Windows Maintenance Suite 🛠️
![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Status](https://img.shields.io/badge/status-Em%20desenvolvimento-orange)
![Language](https://img.shields.io/badge/language-Python-blue)


Conjunto de scripts em **Python** para automatizar a manutenção de sistemas **Windows**, incluindo desfragmentação/otimização de disco, atualizações, reparos do sistema, redefinição de rede e verificação de segurança.

O script principal (`main.py`) executa todos os módulos em sequência com privilégios de administrador.

## ⚙️ Requisitos

- Windows 10 ou 11  
- Python **3.8+**  
- Executar como **Administrador**  
- `winget` instalado (padrão no Windows 10/11)  
- PowerShell habilitado  

---

## 📁 Estrutura do Projeto

```text
.
├── main.py
├── desfragmentation.py
├── update.py
├── tcp_ip_reset.py
├── security.py
├── repair_system.py
└── README.md

````
## 📄 Descrição dos arquivos

### main.py
Orquestrador principal do sistema.

- Verifica se o sistema operacional é Windows  
- Solicita privilégios de administrador  
- Executa todos os módulos de manutenção  
- Reinicia o computador ao final do processo  

---

### desfragmentation.py

- Detecta automaticamente se o disco é **SSD** ou **HDD**
- Executa:
  - **SSD** → Optimize / TRIM
  - **HDD** → Desfragmentação completa + otimização de boot
- Gera logs em `C:\Logs`

---

### update.py
- Atualiza todos os pacotes instalados via **winget**

---

### tcp_ip_reset.py
Restaura configurações de rede:

- TCP/IP  
- Winsock  
- DNS  
- IP release / renew  

---

### security.py

- Atualiza assinaturas do **Windows Defender**
- Executa verificação rápida (**Quick Scan**)

---

### repair_system.py
Executa ferramentas de reparo do Windows:

- CHKDSK (agendado para o próximo boot)
- DISM
- SFC /scannow

---
## 🚀 Como usar

Clone o repositório:
````
git clone https://github.com/gregorygustavo80/WinMaintenanceSuite.git`
````
````
cd WinMaintenanceSuite
````

Execute o script principal:
````
python main.py
````
⚠️ O sistema será reiniciado automaticamente ao final do processo.

## 📄 Licença

Este projeto está licenciado sob a licença MIT.  
Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

