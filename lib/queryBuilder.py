from lib import censysSearch
class QueryBuilder:
    def countryAdder(query):
        countryAdd = input('[-] Would you like to add a country to the query (y/n)')
        if str(countryAdd).lower() == 'y':
            try:
                countryCode = input('[?] Enter a country code (eg. DE IT JP):')
                queryModded = query + " and location.country_code:" + countryCode
                return queryModded
            except TypeError:
                print('[-!-] Wrong type, retrying...')
        elif str(countryAdd).lower() == 'n':
            return query
    def cityAdder(query):
        countryAdd = input('[-] Would you like to add a city to the query (y/n)')
        if str(countryAdd).lower() == 'y':
            try:
                countryCode = input('[?] Enter a city name:')
                queryModded = query + " and location.city:" + countryCode
                return queryModded
            except TypeError:
                print('[-!-] Wrong type, retrying...')
        elif str(countryAdd).lower() == 'n':
            return query
    def CamQueryBuilderCensys(self):
        selection = int(input('[-]Choose an option: '))
        if selection == 1:
            query = 'services.software.vendor:"Hikvision"'
        elif selection == 2:
            pass
            # query = 'login.rsp'
        elif selection == 3:
            pass
            # query = '/wap.htm'
        elif selection == 4:
            query = 'services.http.response.html_title:"My Home"'
        elif selection == 5:
            query = 'linux upnp avtech'
        elif selection == 6:
            query = 'GoAhead 5ccc069c403ebaf9f0171e9517f40e41'
        elif selection == 7 or selection == 3:
            query = '80.http.get.headers.server:Boa 0.94.14rc21'
        elif selection == 8:
            query = 'services.http.response.body_hash:"sha1:c185b57b3ce821a3f5ffffe0479954c10df1279a""'
        elif selection == 9:
            query = input('[-]Enter your custom query: ')
        query = QueryBuilder.countryAdder(query)
        query = QueryBuilder.cityAdder(query)
        return query
    def VpnsQueryBuilderCensys(self):
        selection = int(input('[-]Choose an option: '))
        if selection == 1:
            query = '443.https.tls.certificate.parsed.subject.email_address:support@fortinet.com'
        elif selection == 2:
            censysSearch.censysSearch.samipGathCensys(self)
        query = QueryBuilder.countryAdder(query)
        query = QueryBuilder.cityAdder(query)
        return query
    def CamQueryBuilderShodan(self):
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
            query = 'port:554 has_screenshot:true'
        elif selection == 10:
            query = str(input('[-]Enter your custom query: '))
        return query