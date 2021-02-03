import os, sys, re
class Host:
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port

    def addressRegex(hostLine):
        pattern_1 = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        pattern_2 = r'(\:).*'
        match1 = re.search(pattern_1, hostLine)
        match2 = re.search(pattern_2, hostLine)
        ip = match1.group()
        port_raw = match2.group()
        port = port_raw[1:]
        address = {'ip':ip , 'port' : int(port)}
        return address

