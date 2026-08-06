from modules.hikvisionTester import *
from lib.menuBuilder import *
class testerMenu:
    def testerMenu(self):
        testerSelection = ['Hikvision tester', 'coming soon']
        selection = menuBuilder.choose(selectionArray=testerSelection, title="Menu tester")
        if selection == 1:
            hikTester.hikTester(self)