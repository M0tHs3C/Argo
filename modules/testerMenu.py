from modules.hikvisionTester import *
class testerMenu:
    def testerMenu(self):
        usage = """+-------------------------------------------+
|                Menu tester                |
+-------------------------------------------+
|                                           |
|  (1) Hikvision tester                     |
|                                           |
|  (2) coming soon                          |
|                                           |
+-------------------------------------------+
"""
        print(usage)
        selection = int(input(("[-]Choose an option :")))
        if selection == 1:
            hikTester.hikTester(self)