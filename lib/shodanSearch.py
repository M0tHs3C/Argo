import shodan,os,sys
import shodan.exception
from lib import queryBuilder
from lib import menuBuilder
class shodanSearch:
    def shodanGath(self):
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        api_shodan_key = open(path + "/api/api.txt", "r").read()
        if api_shodan_key == "":
            print('no shodan api found, please insert a valid one')
            api_shodan_key_to_file = input('\ntype here:')
            with open(path + "/api/api.txt", "w") as api:
                api.write(api_shodan_key_to_file)
            api = shodan.Shodan(api_shodan_key)
        else:
            api = shodan.Shodan(api_shodan_key)
            try:
                selection = [['Hikvision', 'http.favicon.hash:999357577'],
                             ['RSP device', 'WIP'],
                             ['Viola DVR', 'WIP'],
                             ['Bticino', 'My-Home Bticino'],
                             ['GeoVision', 'Beta-testing'],
                             ['GoAhead', 'GoAhead cctv'],
                             ['Mixed webcam w/o password',''],
                             ['ANPR cam', 'http.html_hash:-472107530'],
                             ['Generic RTSP', 'port:554'],
                             ['Energy sentinel web', 'http.favicon.hash:130960039'],
                             ['JAWS server', 'JAWS/1.0'],
                             ['Custom query', 'customize your search']]
                menuBuilder.menuBuilder.buildMenu(selectionArray=selection,title="Shodan search")
                query = queryBuilder.QueryBuilder.CamQueryBuilderShodan(self)
                try:
                    response = api.search(query)
                    with open(path + '/host/host.txt', "w") as host:
                        for service in response['matches']:
                            host.write(str(service['ip_str'] + ":" + str(service['port'])))# host.write(service['port']
                            host.write("\n")
                except shodan.exception.APIError:
                    print("[!] Bad API, try deleting the api.txt file under the api folder and then recreate the file without modifing it, then re-run the tool\n[!] be advise, the file must be empty and when you must paste the api key without space")
                    answer = input("[?] would you like to try to reset the api key system?  (y/n)  :")
                    if str(answer.lower()) == "y":
                        import platform
                        system = platform.system()
                        if system.lower() == "windows":
                            os.system("del " + path + "/api/api.txt")
                            os.system("type nul > "+ path + "/api/api.txt")
                        elif system.lower() == "linux":
                            os.system("rm " + path + "/api/api.txt")
                            os.system("touch " + path + "/api/api.txt")
                except KeyboardInterrupt:
                        pass
            except KeyboardInterrupt:
                print ("\n[---]exiting now[---]")
