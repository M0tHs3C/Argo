# -*- coding: utf-8 -*-
from lib.censysSearch import *
from lib.shodanSearch import *
from modules.upTester import *
from exploit.exploitMenu import *
from modules.testerMenu import *
from modules.fileDelete import *
from lib.menuBuilder import *
class Argo:
    def main(self):
        def selection(self, selectionArg):
            if selectionArg == 1:
                shodanSearch.shodanGath(self)
            elif selectionArg == 2:
                censysSearch.censysGath(self)
            elif selectionArg == 3:
                upTester.Tcp(self)
            elif selectionArg == 4:
                testerMenu.testerMenu(self)
            elif selectionArg == 5:
                exploitMenu.exploitMenu(self)
            elif selectionArg == 6:
                fileDelete.deleteFileContent(self)


        banner = """\n    __ _ _ __ __ _  ___\n   / _` | '__/ _` |/ _ \ \n  | (_| | | | (_| | (_) |\n   \__,_|_|  \__, |\___/     V 2.0 by M0thS3c\n             |___/       """
        argoMenu = [["Gather host from shodan", "API key needed"],
                    ["Gather host from censys", "API key needed"],
                    ["Test for up host", "host may be down even if the search is fresh"],
                    ["Test for false positive", "not all host may be vuln"],
                    ["Exploit menu", "List of available exploit"],
                    ["Delete Hosts lists", "Clear history of hosts"]]
        print(banner)
        menuBuilder.buildMenu(selectionArray=argoMenu,title="Argo main menu")
        selectionInput = input("[-]Choose an option: ")
        try:
            selection(self, int(selectionInput))
        except ValueError:
            print("[!!!] You  entered a wrong input")




argo = Argo()
try:
    while 1:
        argo.main()
except KeyboardInterrupt:
    print("\n[ Bye ] Exiting now...")