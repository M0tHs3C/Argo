from lib.menuBuilder import menuBuilder


class QueryBuilder:
    def countryAdder(query):
        if query is None:
            return query
        countryAdd = input('[-] Would you like to add a country to the query (y/n)')
        if str(countryAdd).lower() == 'y':
            countryCode = input('[?] Enter a country code (eg. DE IT JP):')
            return query + " and location.country_code='" + countryCode.upper() + "'"
        return query
    def cityAdder(query):
        if query is None:
            return query
        cityAdd = input('[-] Would you like to add a city to the query (y/n)')
        if str(cityAdd).lower() == 'y':
            cityName = input('[?] Enter a city name:')
            return query + " and location.city:" + cityName
        return query
    def CamQueryBuilderCensys(self):
        selection = menuBuilder.readInt()
        query = None
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
        elif selection == 7:
            query = '80.http.get.headers.server:Boa 0.94.14rc21'
        elif selection == 8:
            query = 'services.http.response.body_hash:"sha1:c185b57b3ce821a3f5ffffe0479954c10df1279a"'
        elif selection == 9:
            query = 'services.http.response.headers.Server:"JAWS/1.0"'
        elif selection == 10:
            query = input('[-]Enter your custom query: ')
        query = QueryBuilder.countryAdder(query)
        query = QueryBuilder.cityAdder(query)
        return query
    def VpnsQueryBuilderCensys(self):
        selection = menuBuilder.readInt()
        query = None
        if selection == 1:
            query = '(services.tls.certificates.leaf_data.issuer.email_address:"support@fortinet.com") and services.port:10443'
        elif selection == 2:
            query = 'services.http.response.html_title:"SAMIP Web Access"'
        query = QueryBuilder.countryAdder(query)
        query = QueryBuilder.cityAdder(query)
        return query
