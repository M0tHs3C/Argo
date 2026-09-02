import os, sys
import shodan
from lib import queryBuilder
from lib.menuBuilder import menuBuilder

_BACK = '↩  Back'

_CAMERAS = [
    ['Hikvision', 'http.favicon.hash:999357577'],
    ['RSP device', 'WIP'],
    ['Viola DVR', 'WIP'],
    ['GeoVision', 'Beta-testing'],
    ['GoAhead', 'GoAhead cctv'],
    ['ANPR cam', 'http.html_hash:-472107530'],
    ['Generic RTSP', 'port:554'],
    ['JAWS server', 'JAWS/1.0'],
]
_VPNS = [
    ['FortiOs', 'WIP'],
]
_IOT = [
    ['Bticino', 'http.favicon.hash:965868968'],
    ['Energy sentinel web', 'http.favicon.hash:130960039'],
    ['icare', 'http.favicon.hash:1786862297'],
    ['teleindustria', 'http.favicon.hash:145805043'],
    ['SAMIP', 'http.title:"SAMIP Web Access"'],
    ['DFWEB', 'http.favicon.hash:-1915294544'],
]
_CATEGORIES = [
    ['Cameras', _CAMERAS],
    ['VPNs', _VPNS],
    ['IoT', _IOT],
]


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
            while True:
                catSel = menuBuilder.choose(
                    selectionArray=[c[0] for c in _CATEGORIES] + ['Custom query', _BACK],
                    title="Shodan search",
                )
                if catSel == len(_CATEGORIES) + 2:
                    return

                if catSel == len(_CATEGORIES) + 1:
                    query = str(input('[-]Enter your custom query: '))
                else:
                    catName, entries = _CATEGORIES[catSel - 1]
                    sel = menuBuilder.choose(
                        selectionArray=entries + [_BACK],
                        title=catName + " query",
                    )
                    if sel == len(entries) + 1:
                        continue
                    _, query = entries[sel - 1]
                    if query in ('WIP', 'Beta-testing'):
                        print("[!] Not available yet")
                        continue

                query = queryBuilder.QueryBuilder.countryAdder(query)
                query = queryBuilder.QueryBuilder.cityAdder(query)
                if not query:
                    continue

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
            print("\n[---]exiting now[---]")
