import sys
from colorama import init, Fore, Style

init(autoreset=True)


class menuBuilder:
    BORDER = Fore.CYAN
    TITLE = Fore.YELLOW + Style.BRIGHT
    NUM = Fore.GREEN + Style.BRIGHT
    DESC = Fore.LIGHTBLACK_EX
    ERROR = Fore.RED + Style.BRIGHT
    PROMPT = Fore.MAGENTA + Style.BRIGHT

    def buildMenu(self=None, selectionArray=None, title=None):
        title = title or ""
        rows = []
        for item in selectionArray:
            if isinstance(item, (list, tuple)):
                rows.append((str(item[0]), str(item[1])))
            else:
                rows.append((str(item), None))

        plainLines = []
        for idx, (label, desc) in enumerate(rows, start=1):
            line = "{0}) {1}".format(idx, label)
            if desc:
                line += "  [{0}]".format(desc)
            plainLines.append(line)

        width = max([len(title)] + [len(line) for line in plainLines] + [30]) + 4

        top = menuBuilder.BORDER + "┌" + "─" * width + "┐"
        sep = menuBuilder.BORDER + "├" + "─" * width + "┤"
        bottom = menuBuilder.BORDER + "└" + "─" * width + "┘"

        print("\n" + top)
        print(menuBuilder.BORDER + "│" + menuBuilder.TITLE + title.center(width) + menuBuilder.BORDER + "│")
        print(sep)
        for idx, (label, desc) in enumerate(rows, start=1):
            plain = " {0}) {1}".format(idx, label)
            colored = " " + menuBuilder.NUM + "{0})".format(idx) + Style.RESET_ALL + " " + label
            if desc:
                plain += "  [{0}]".format(desc)
                colored += "  " + menuBuilder.DESC + "[{0}]".format(desc) + Style.RESET_ALL
            pad = " " * (width - len(plain))
            print(menuBuilder.BORDER + "│" + Style.RESET_ALL + colored + pad + menuBuilder.BORDER + "│")
        print(bottom + "\n")

    def readInt(self=None, prompt="Choose an option"):
        while True:
            try:
                raw = input(menuBuilder.PROMPT + "[-] " + prompt + ": " + Style.RESET_ALL)
                return int(raw)
            except ValueError:
                print(menuBuilder.ERROR + "[!] Please enter a valid number." + Style.RESET_ALL)

    def arrowSelect(self=None, selectionArray=None, title=None, prompt="Choose an option"):
        import sys
        if not (sys.stdin.isatty() and sys.stdout.isatty()):
            raise RuntimeError("not an interactive terminal")

        import questionary
        from questionary import Style as QStyle

        rows = []
        for item in selectionArray:
            if isinstance(item, (list, tuple)):
                rows.append((str(item[0]), str(item[1])))
            else:
                rows.append((str(item), None))

        choices = []
        for idx, (label, desc) in enumerate(rows, start=1):
            text = label if not desc else "{0}   ({1})".format(label, desc)
            choices.append(questionary.Choice(title=text, value=idx))

        qStyle = QStyle([
            ('qmark', 'fg:#00d7ff bold'),
            ('question', 'fg:#ffd75f bold'),
            ('pointer', 'fg:#ff5f5f bold'),
            ('highlighted', 'fg:#00d7ff bold'),
            ('selected', 'fg:#5fd7ff'),
            ('instruction', 'fg:#5f5f5f italic'),
            ('answer', 'fg:#ff5fff bold'),
        ])

        width = max([len(title or "")] + [len(l) for l, _ in rows] + [30]) + 4
        print("\n" + menuBuilder.BORDER + "── " + menuBuilder.TITLE + (title or "") + Style.RESET_ALL +
              menuBuilder.BORDER + " " + "─" * max(width - len(title or "") - 4, 0) + Style.RESET_ALL)

        answer = questionary.select(
            prompt,
            choices=choices,
            style=qStyle,
            qmark="▸",
            instruction=" (use ↑/↓ then Enter)",
        ).unsafe_ask()
        print("")
        if answer is None:
            raise RuntimeError("no answer")
        return answer

    def shellBanner(target):
        sys.stdout.write(f"\033]0;shell @ {target}\007")
        sys.stdout.flush()
        label = f"  shell @ {target}  "
        width = max(len(label), 38)
        print("\n" + menuBuilder.BORDER + "┌" + "─" * width + "┐")
        print(menuBuilder.BORDER + "│" + Style.BRIGHT + Fore.WHITE + label.center(width) + Style.RESET_ALL + menuBuilder.BORDER + "│")
        print(menuBuilder.BORDER + "└" + "─" * width + "┘" + Style.RESET_ALL + "\n")

    def choose(self=None, selectionArray=None, title=None, prompt="Choose an option"):
        try:
            return menuBuilder.arrowSelect(selectionArray=selectionArray, title=title, prompt=prompt)
        except KeyboardInterrupt:
            raise
        except Exception:
            pass
        menuBuilder.buildMenu(selectionArray=selectionArray, title=title)
        return menuBuilder.readInt(prompt=prompt)
