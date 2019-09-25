import hikvisionTester
class vulnTester:
    def checker(self):
        usage = """+-----------------------------------------------+
|              Vulnerability checker            |
+-----------------------------------------------+
|                                               |
| (1) Hikvision checker                         |
|                                               |
| (2) Rsp device checker                        |
|                                               |
| (3) Viola DVR checker                         |
|                                               |
+-----------------------------------------------+
"""
        print(usage)
        selection = input("[-]Select a device type to test: ")
        if selection == 1:
            hik = hikvisionTester.hikTester()
            hik.hikTester()