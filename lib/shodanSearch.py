import shodan
import os
import sys
import shodan.exception


class shodanSearch:
    def shodanGath(self):
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        api_shodan_key = open(path + "/Api/api.txt", "r").read().rstrip()
        if api_shodan_key == "":
            print('no shodan api found, please insert a valid one')
            api_shodan_key_to_file = input('\ntype here:')
            with open(path + "/Api/api.txt", "w") as api:
                api.write(api_shodan_key_to_file)
            api = shodan.Shodan(api_shodan_key)
        else:
            api = shodan.Shodan(api_shodan_key)
            try:
                print("""+-----------------------------------------------+
|                 Shodan search                 |
+-----------------------------------------------+
|                                               |
| (1) Hikvision query       [ App-webs 200 OK ] |
|                                               |
| (2) Rsp device query      [   login.rsp     ] |
|                                               |
| (3) Viola DVR query       [  /wap.htm       ] |
|                                               |
| (4) AVTECH query          [ AVTECH          ] |
|                                               |
| (5) Geovision query       [Server:thttpd PHP] |
|                                               |
| (6) goAhead query         [GoAhead          ] |
|                                               |
| (7) mixed webcam w/o password                 |
|                                               |
| (8) ANPR cam query        [embedded-server]   |
|                                               |
| (9) custom query                              |
|                                               |
+-----------------------------------------------+
""")
                selection = int(input('[-]Choose an option: '))
                if selection == 1:
                    query = 'App-webs 200 OK'
                elif selection == 2:
                    query = 'login.rsp'
                elif selection == 3:
                    query = '/wap.htm'
                elif selection == 4:
                    query = 'linux upnp avtech'
                elif selection == 5:
                    query = 'Server: thttpd PHP'
                elif selection == 6:
                    query = 'GoAhead 5ccc069c403ebaf9f0171e9517f40e41'
                elif selection == 7:
                    print("[--] by using shodan web interace search for this query, or upgrade your API plan\n"
                          "[1]  has_screenshot:yes webcam\n"
                          "[2]  has_screenshot:yes port:80\n"
                          "[3]  has_screenshot:yes product:""Yawcam webcam viewer httpd\n"
                          "[4]  has_screenshot:yes product:D-Link/Airlink IP webcam http config""\n")
                    # query="has_screenshot:yes product:""D-Link/Airlink IP webcam http config"    #UN-COMMENT IF YOU HAVE PREMIUM PLAN1
                    return
                elif selection == 8:
                    query = 'WWW-Authenticate: Basic realm="Embedded-Device"'
                elif selection == 9:
                    query = str(input('[-]Enter your custom query: '))

                try:
                    response = api.search(query)
                    with open(path + '/Host/host.txt', "w") as host:
                        for service in response['matches']:
                            # host.write(service['port']
                            host.write(
                                str(service['ip_str'] + ":" + str(service['port'])))
                            host.write("\n")
                except shodan.exception.APIError:
                    print("[!] Bad API, try deleting the api.txt file under the api folder and then recreate the file without modifing it, then re-run the tool\n[!] be advise, the file must be empty and when you must paste the api key without space")
                    answer = input(
                        "[?] would you like to try to reset the api key system?  (y/n)  :")
                    if str(answer.lower()) == "y":
                        import platform
                        system = platform.system()
                        if system.lower() == "windows":
                            os.system("del " + path + "/Api/api.txt")
                            os.system("type nul > " + path + "/Api/api.txt")
                        elif system.lower() == "linux" or system.lower() == "darwin":
                            os.system("rm " + path + "/Api/api.txt")
                            os.system("touch " + path + "/Api/api.txt")
                    else:
                        pass

            except KeyboardInterrupt:
                print("\n[---]exiting now[---]")
