import os, sys, socket
from colorama import Fore, Style
from host import host
from lib.menuBuilder import menuBuilder

_BACK = '↩  Back'

PORTS = [21, 22, 23, 25, 80, 443, 2222, 3389, 8080, 8443, 8888]
PORT_NAMES = {
    21: 'FTP',      22: 'SSH',       23: 'Telnet',    25: 'SMTP',
    80: 'HTTP',     443: 'HTTPS',    2222: 'SSH-alt',  3389: 'RDP',
    8080: 'HTTP-alt', 8443: 'HTTPS-alt', 8888: 'HTTP-alt',
}


def _pick_host(path):
    try:
        hosts = [h.strip() for h in open(path + '/host/vuln_host.txt').read().splitlines() if h.strip()]
    except FileNotFoundError:
        print("[!] vuln_host.txt not found — run an exploit first.")
        return None
    if not hosts:
        print("[!] No hosts in vuln_host.txt.")
        return None
    labels = []
    for entry in hosts:
        a = host.Host.addressRegex(entry)
        labels.append(a['ip'] + ':' + str(a['port']))
    sel = menuBuilder.choose(selectionArray=labels, title="Select host") - 1
    return host.Host.addressRegex(hosts[sel])['ip']


class c2:
    def c2Menu(self):
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        options = ['Port scan']

        while True:
            sel = menuBuilder.choose(
                selectionArray=options + [_BACK],
                title="Host Control",
            )
            if sel == len(options) + 1:
                return

            if sel == 1:
                c2.portScan(self, path)

    def portScan(self, path=None):
        if path is None:
            path = os.path.abspath(os.path.dirname(sys.argv[0]))
        ip = _pick_host(path)
        if not ip:
            return

        print(f"\n[*] Scanning {ip} ...\n")
        print(f"  {'PORT':<7} {'SERVICE':<12} STATUS")
        print(Fore.LIGHTBLACK_EX + "  " + "─" * 30 + Style.RESET_ALL)

        for port in PORTS:
            name = PORT_NAMES.get(port, '')
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                open_ = s.connect_ex((ip, port)) == 0
                s.close()
            except Exception:
                open_ = False

            if open_:
                status = Fore.GREEN + Style.BRIGHT + "OPEN" + Style.RESET_ALL
            else:
                status = Fore.LIGHTBLACK_EX + "closed" + Style.RESET_ALL
            print(f"  {port:<7} {name:<12} {status}")
        print()
