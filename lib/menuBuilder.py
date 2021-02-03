class menuBuilder:
    def buildMenu(self=None,selectionArray=None,title=None):
        separator = "+------------------------------------------------+"
        menuSize = len(separator)
        menuEnd = "|"
        spaceTitleCenter = ((int(menuSize / 2)- 1)-int(len(title)/2))*" "
        if int(len(title)%2) == 0:
            spaceTitleRight = spaceTitleCenter
        else:
            spaceTitleRight = (len(spaceTitleCenter)-1)*" "
        titleBuilder = separator + "\n" + menuEnd + spaceTitleCenter + title + (spaceTitleRight) + menuEnd + "\n" + separator + "\n"
        print(titleBuilder)
        counter = 1
        iterator = 0
        for selection in selectionArray:
            if type(selection) == list:
                print(str(counter) + ") "+ selection[0] + "   [" + selection[1] + "]\n")
                counter += 1
            else:
                print(str(counter) + ") "+ selectionArray[iterator] + "\n")
                iterator += 1
                counter += 1
