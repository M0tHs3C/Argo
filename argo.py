# -*- coding: utf-8 -*-
from lib.censysSearch import *
from lib.shodanSearch import *
from modules.upTester import *
from exploit.exploitMenu import *
from modules.testerMenu import *
from modules.fileDelete import *

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




        usage = """\n                     ,-""-.     _                          ,-""-.  ,-""-.
                    / ,--. \   /_\  _ __ __ _  ___        / ,--. \/ ,--.'\ 
                   | ( () ) | //_\\\| '__/ _` |/ _ \      | ( () )||( () ) |
                    \,`--'./ /  _  \ | | (_| | (_) |  ,-""\.`--'-/\-`--',/""-.
                    /`-..-'\ \_/ \_/_|  \__, |\___/  / ,--.`-..-'--`-..-',--.'\ 
                   | ( () ) |           |___/       | ( () ) | ( () ) | ( () ) |
                    \ `--' /                         \ `--' / \ `--' / \ `--' /
                   +-`-..-'---------------------------`-..-'---`-..-'---`-..-'-------+
                   |                                                                 |
                   |  (1) Gather host from shodan     [API key from shodan needed ]  |
                   |                                                                 |
                   |  (2) Gather host from censys     [API key and secret needed  ]  |
                   |                                                                 |
                   |  (3) Test for really up host     [Not always the host are up ]  |
                   |                                                                 |
                   |  (4) Test for false positive     [Not all results may be vuln]  |
                   |                                                                 |
                   |  (5) Exploit menu                [Exploit from multiple cctv ]  |
                   |                                                                 |
                   |  (6) Delete host list            [Clear the history of hosts ]  |
                   |                                                                 |
                   +-----------------------------------------------------------------+

"""
        print(usage)
        selectionInput = input("[-]Choose an option: ")
        selection(self,int(selectionInput))



argo = Argo()
while 1:
    argo.main()