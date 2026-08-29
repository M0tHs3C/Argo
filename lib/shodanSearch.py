import os, sys
import shodan
from lib import queryBuilder
from lib import menuBuilder
class shodanSearch:
    def shodanGath(self):
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        keyPath = path + "/api/api.txt"
        api_shodan_key = os.environ.get('SHODAN_API_KEY', '').strip()
        if not api_shodan_key:
            try:
                api_shodan_key = open(keyPath, "r").read().strip()
            except FileNotFoundError:
                api_shodan_key = ''
        if not api_shodan_key:
            print('no shodan api found, please insert a valid one')
            api_shodan_key = input('\ntype here:').strip()
            os.makedirs(os.path.dirname(keyPath), exist_ok=True)
            with open(keyPath, "w") as api:
                api.write(api_shodan_key)
        api = shodan.Shodan(api_shodan_key)
        try:
            selection = [['Hikvision', 'http.favicon.hash:999357577'],
                         ['RSP device', 'WIP'],
                         ['Viola DVR', 'WIP'],
                         ['Bticino', 'http.favicon.hash:965868968'],
                         ['GeoVision', 'Beta-testing'],
                         ['GoAhead', 'GoAhead cctv'],
                         ['Mixed webcam w/o password',''],
                         ['ANPR cam', 'http.html_hash:-472107530'],
                         ['Generic RTSP', 'port:554'],
                         ['Energy sentinel web', 'http.favicon.hash:130960039'],
                         ['JAWS server', 'JAWS/1.0'],
                         ['icare', 'http.favicon.hash:1786862297'],
                         ['teleindustria', 'http.favicon.hash:145805043'],
                         ['SAMIP', 'http.title:"SAMIP Web Access"'],
                         ['Custom query', 'customize your search']]
            sel = menuBuilder.menuBuilder.choose(selectionArray=selection + [['Back', '']], title="Shodan search")
            if sel == len(selection) + 1:
                return
            query = queryBuilder.QueryBuilder.CamQueryBuilderShodan(self, selection=sel)
            if not query:
                return
            try:
                response = api.search(query)
                with open(path + '/host/host.txt', "w") as host:
                    for service in response['matches']:
                        host.write(str(service['ip_str']) + ":" + str(service['port']))
                        host.write("\n")
                print("[+] %d host(s) written to host/host.txt" % len(response['matches']))
            except shodan.APIError as error:
                print("[!] Shodan rejected the request: %s" % error)
                answer = input("[?] would you like to reset the api key? (y/n): ")
                if answer.strip().lower() == "y":
                    open(keyPath, "w").close()
            except KeyboardInterrupt:
                pass
        except KeyboardInterrupt:
            print ("\n[---]exiting now[---]")
