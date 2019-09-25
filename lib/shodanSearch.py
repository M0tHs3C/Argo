import shodan,os,sys

class shodanSearch:
    def shodanGath(self):
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        api_shodan_key = open(path + "/Api/api.txt", "r").read()
        if api_shodan_key == "":
            print('no shodan api found, please insert a valid one')
            api_shodan_key_to_file = input('\ntype here:')
            with open(path + "/Api/api.txt", "wb") as api:
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
| (5) custom query                              |
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
                    query = 'AVTECH'
                elif selection == 5:
                    query = str(input('[-]Enter your custom query: '))

                response = api.search(query)
                with open(path + '/Host/host.txt', "w") as host:
                    for service in response['matches']:
                        host.write(str(service['ip_str'] + ":" + str(service['port'])))# host.write(service['port']
                        host.write("\n")
            except KeyboardInterrupt:
                print ("\n[---]exiting now[---]")