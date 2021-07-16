import censys
from censys.search import CensysIPv4
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
                    cameraSelection = [['Hikvision', 'Apps-webs 200 OK'],
                                       ['RSP device', 'WIP'],
                                       ['Viola DVR', 'WIP'],
                                       ['Bticino', 'My-Home Bticino'],
                                       ['GeoVision', 'Beta-testing'],
                                       ['GoAhead', 'GoAhead cctv'],
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
                    for record in CensysIPv4(api_id=uid, api_secret=secret).search(query):
                        ip = record['ip']
                        port = record['protocols']
                        port_raw = port[0]
                        port = re.findall(r'\d+', port_raw)
                        with open(path + '/host/host.txt', "a") as cen:
                            cen.write(ip + ":" + str(port[0]))
                            cen.write("\n")
                except KeyboardInterrupt:
                    print("[*]Exiting...")
                except CensysException:
                    pass
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
        query = ['80.http.get.title:"SAMIP Web Access"',
                 '443.http.get.title:"SAMIP Web Access"',
                 '8080.http.get.title:"SAMIP Web Access"',
                 '8888.http.get.title:"SAMIP Web Access"']
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
