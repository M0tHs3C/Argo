import sys
import os
from censys.search import CensysHosts
from censys.common.exceptions import CensysException
from lib import queryBuilder
from lib.menuBuilder import *


class censysSearch:
    def censysGath(self):
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        keyPath = path + "/api/censys_api.txt"
        uid = os.environ.get('CENSYS_API_ID', '').strip()
        secret = os.environ.get('CENSYS_API_SECRET', '').strip()
        if not uid or not secret:
            try:
                censys_list = open(keyPath, "r").read().splitlines()
                if len(censys_list) >= 2:
                    uid, secret = censys_list[0].strip(), censys_list[1].strip()
            except FileNotFoundError:
                pass
        if not uid or not secret:
            print('no censys api found, please insert a valid one')
            uid = input('[****]type here uid:').strip()
            secret = input('[****]type here secret:').strip()
            os.makedirs(os.path.dirname(keyPath), exist_ok=True)
            with open(keyPath, "w") as api:
                api.write(uid + "\n" + secret)
        query = None
        try:
            menuSelection = [['Cameras', 'List of cameras query and affiliated'],
                             ['VPNs', 'List of affected vpns']]
            cameraSelection = [['Hikvision', 'services.software.vendor:"Hikvision"'],
                               ['RSP device', 'WIP'],
                               ['Viola DVR', 'WIP'],
                               ['Bticino', 'services.http.response.html_title:"My Home"'],
                               ['GeoVision', 'Beta-testing'],
                               ['GoAhead', 'GoAhead cctv'],
                               ['Boa Server', 'not working'],
                               ['Tattile ANPR camera', 'services.http.response.body_hash:"sha1:c185b57b3ce821a3f5ffffe0479954c10df1279a"'],
                               ['JAWS cctv camera', 'services.http.response.headers.Server:"JAWS/1.0"'],
                               ['Custom query', 'customize your search']]
            vpnSelection = [['Fortinet FortiOS', 'vuln vpns'],
                            ['SAMIP VoIP', 'Samip voip brute']]
            selection = menuBuilder.choose(
                selectionArray=menuSelection, title="Censys search")
            if selection == 1:
                menuBuilder.buildMenu(
                    selectionArray=cameraSelection, title="Censys camera search")
                query = queryBuilder.QueryBuilder.CamQueryBuilderCensys(self)
            elif selection == 2:
                menuBuilder.buildMenu(
                    selectionArray=vpnSelection, title="Censys vpn search")
                query = queryBuilder.QueryBuilder.VpnsQueryBuilderCensys(self)
            if query is None:
                print("[No query passed]")
                return
            print('[Selected query] %s' % query)
            hosts = CensysHosts(api_id=uid, api_secret=secret)
            written = 0
            with open(path + '/host/host.txt', "a") as hostFile:
                for page in hosts.search(query, per_page=100, pages=1):
                    for hit in page:
                        ip = hit['ip']
                        services = hit.get('services') or []
                        port = services[0]['port'] if services else 80
                        hostFile.write(str(ip) + ":" + str(port) + "\n")
                        written += 1
            print("[+] %d host(s) written to host/host.txt" % written)
        except KeyboardInterrupt:
            print("[*]Exiting...")
        except CensysException as error:
            print("[!] Something wrong with your censys key: %s" % error)
