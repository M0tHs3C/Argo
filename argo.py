# -*- coding: utf-8 -*-
import sys
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

from colorama import Fore, Style, init
init(autoreset=True)

from lib.censysSearch import *
from lib.shodanSearch import *
from modules.upTester import *
from exploit.exploitMenu import *
from modules.testerMenu import *
from modules.fileDelete import *
from lib.menuBuilder import *


ARGO_ART = [
    " █████╗ ██████╗  ██████╗  ██████╗ ",
    "██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗",
    "███████║██████╔╝██║  ███╗██║   ██║",
    "██╔══██║██╔══██╗██║   ██║██║   ██║",
    "██║  ██║██║  ██║╚██████╔╝╚██████╔╝",
    "╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ",
]
ARGO_GRADIENT = [Fore.CYAN, Fore.CYAN, Fore.BLUE, Fore.BLUE, Fore.MAGENTA, Fore.MAGENTA]

# a watchful eye on each side, a nod to Argus Panoptes -- the all-seeing guardian Argo is named after
EYE_OUTLINE = [
    "          ",
    "   ___    ",
    " <  {0}  > ",
    "   ‾‾‾    ",
    "          ",
    "          ",
]
EYE_PUPIL = "◉"


def renderEye():
    return [line.format(EYE_PUPIL) if "{0}" in line else line for line in EYE_OUTLINE]


def renderBanner():
    subtitlePlain = "CCTV / IoT recon & exploitation framework"
    versionPlain = "v2.0  ·  M0thS3c"
    eye = renderEye()
    eyeWidth = len(eye[0])
    width = max([len(line) for line in ARGO_ART] + [len(subtitlePlain), len(versionPlain)])

    rows = []
    for line, color, eyeLine in zip(ARGO_ART, ARGO_GRADIENT, eye):
        eyeColored = Style.DIM + Fore.CYAN + eyeLine.replace(EYE_PUPIL, Style.RESET_ALL + Style.BRIGHT + Fore.RED + EYE_PUPIL + Style.DIM + Fore.CYAN) + Style.RESET_ALL
        rows.append(eyeColored + "  " + Style.BRIGHT + color + line.center(width) + Style.RESET_ALL + "  " + eyeColored)
    art = "\n".join(rows)

    fullWidth = eyeWidth * 2 + 4 + width
    rule = Fore.LIGHTBLACK_EX + "─" * fullWidth + Style.RESET_ALL
    subtitle = Fore.WHITE + Style.DIM + subtitlePlain.center(fullWidth) + Style.RESET_ALL
    version = Fore.MAGENTA + Style.BRIGHT + versionPlain.center(fullWidth) + Style.RESET_ALL
    return "\n" + art + "\n" + rule + "\n" + subtitle + "\n" + version + "\n" + rule + "\n"


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

        banner = renderBanner()
        argoMenu = [["Gather host from shodan", "API key needed"],
                    ["Gather host from censys", "API key needed"],
                    ["Test for up host", "host may be down even if the search is fresh"],
                    ["Test for false positive", "not all host may be vuln"],
                    ["Exploit menu", "List of available exploit"],
                    ["Delete Hosts lists", "Clear history of hosts"]]
        print(banner)
        selectionInput = menuBuilder.choose(selectionArray=argoMenu, title="Argo main menu")
        selection(self, selectionInput)


argo = Argo()
try:
    while 1:
        argo.main()
except (KeyboardInterrupt, EOFError):
    print("\n[ Bye ] Exiting now...")
