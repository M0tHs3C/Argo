
from censys.search import SearchClient
from censys.common.exceptions import (CensysException,
                                      CensysRateLimitExceededException)
import sys
import os
import re
from lib import queryBuilder
from lib.menuBuilder import *


class censysSearch:
    def censysGath(self):
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        censys_list = open(path + "/api/censys_api.txt",
                           "r").read().splitlines()
        if censys_list == []:
            print('no censys api found, please insert a valid one')
            api_censys_uid = input('[****]' + 'type here uid:')
            api_censys_scrt = input('[****]' + 'type here secret:')
            with open(path + "/api/censys_api.txt", "w") as api:
                api.write(api_censys_uid + "\n" + api_censys_scrt)
        else:
            try:
                uid = censys_list[0]
                secret = censys_list[1]
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
                    menuBuilder.buildMenu(
                        selectionArray=menuSelection, title="Censys search")
                    try:
                        selection = int(input('[-]Choose an option: '))
                        if selection == 1:
                            menuBuilder.buildMenu(
                                selectionArray=cameraSelection, title="Censys camera search")
                            query = queryBuilder.QueryBuilder.CamQueryBuilderCensys(
                                self)
                        elif selection == 2:
                            menuBuilder.buildMenu(
                                selectionArray=vpnSelection, title="Censys vpn search")
                            query = queryBuilder.QueryBuilder.VpnsQueryBuilderCensys(
                                self)
                    except ValueError:
                        print("[!!!] Wrong input value.")
                    if query != None:
                        print('[Selected query] %s' % query)
                    else:
                        pass
                    censysSearch = SearchClient()
                    apiRequest = censysSearch.v2.hosts.search(query, per_page=100, pages=1)
                    record = apiRequest.view_all()
                    for host in record:
                        ip = record[host]['ip']
                        port = record[host]['services'][0]['port'] if record[host]['services'][0]['port'] else 80
                        #port_raw = port[0]
                        #port = re.findall(r'\d+', port_raw)
                        with open(path + '/host/host.txt', "a") as cen:
                            cen.write(str(ip) + ":" + str(port))
                            cen.write("\n")
                except KeyboardInterrupt:
                    print("[*]Exiting...")
                except CensysException:
                    print("[!]Something wrong with your censys key!")
                except UnboundLocalError:
                    print("[No query passed]")
            except:
                pass


    def samipGathCensys(self):
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        censys_list = open(path + "/api/censys_api.txt",
                           "r").read().splitlines()
        if censys_list == []:
            print('no censys api found, please insert a valid one')
            api_censys_uid = input('[****]' + 'type here uid:')
            api_censys_scrt = input('[****]' + 'type here secret:')
            with open(path + "/api/censys_api.txt", "w") as api:
                api.write(api_censys_uid + "\n" + api_censys_scrt)
        else:
            uid = censys_list[0]
            secret = censys_list[1]
        query = ['services.http.response.html_title:"SAMIP Web Access"']
        try:
            for q in query:
                for record in CensysIPv4(api_id=uid, api_secret=secret).search(q):
                    ip = record['ip']
                    port = record['protocols']
                    port_raw = port[0]
                    port = re.findall(r'\d+', port_raw)
                    with open(path + '/host/host.txt', "a") as cen:
                        cen.write(ip + ":" + str(port[0]))
                        cen.write("\n")
        except KeyboardInterrupt:
            pass
