import sys
import keyboard
import colorama
import click

colorama.init()
def ischar(char, error):
    if not len(char) == 1: raise error
def isansifore(obj, error):
    if not hasattr(colorama.Fore, obj): raise error
def isansiback(obj, error):
    if not hasattr(colorama.Back, obj): raise error
def isfunction(function):
    try:
        function()
        return True
    except TypeError:
        return False

class screen:
    def __init__(self, foreColor = "WHITE", backColor = "BLACK", width = 32, height = 16, border = ["-", "|", "#", "#", "#", "#"], stdChar = " ", checkIfChar = True, checkIfColor = True, checkIfBorder = True):
        if checkIfChar: ischar(stdChar, SyntaxError("stdChar is not a single char"))
        if checkIfColor:
            isansifore(foreColor, SyntaxError(f"{foreColor} is not a valid attribute in colorama.ansi.ansiFore"))
            isansiback(backColor, SyntaxError(f"{backColor} is not a valid attribute in colorama.ansi.ansiBack"))
        if checkIfBorder:
            index = 0
            for char in border:
                ischar(char, SyntaxError(f"border[{index}] is not a single char"))
                index += 1
        self.foreColor = getattr(colorama.Fore, foreColor)
        self.backColor = getattr(colorama.Back, backColor)
        self.width = width
        self.height = height
        self.stdChar = stdChar
        self.border = border
        self.values = []
        for i in range(self.height):
            for j in range(self.width):
                self.values.append(self.stdChar)
        self.colors = []
        for i in range(self.height):
            for j in range(self.width):
                self.colors.append(self.foreColor + self.backColor)
    def update(self, clear = True):
        if clear: click.clear()
        render = ""
        render += self.border[2] + self.border[0] * self.width + self.border[3] + "\n"
        index = 0
        for i in range(self.height):
            render += self.border[1]
            for j in range(self.width):
                render += self.colors[index] + self.values[index]
                index += 1
            render += colorama.Fore.RESET + colorama.Back.RESET + self.border[1] + "\n"
        render += colorama.Fore.RESET + colorama.Back.RESET + self.border[4] + self.border[0] * self.width + self.border[5] + "\n"
        print(render)
    def fillChar(self, char):
        ischar(char, SyntaxError("char is not a single char"))
        self.values = []
        for i in range(self.height):
            for j in range(self.width):
                self.values.append(char)
    def fillColor(self, fore, back):
        isansifore(fore, SyntaxError(f"{fore} is not a valid attribute in colorama.ansi.ansiFore"))
        isansiback(back, SyntaxError(f"{back} is not a valid attribute in colorama.ansi.ansiBack"))
        self.colors = []
        for i in range(self.height):
            for j in range(self.width):
                self.colors.append(getattr(colorama.Fore, fore) + getattr(colorama.Back, back))
    def fill(self, char, fore, back):
        ischar(char, SyntaxError("char is not a single char"))
        isansifore(fore, SyntaxError(f"{fore} is not a valid attribute in colorama.ansi.ansiFore"))
        isansiback(back, SyntaxError(f"{back} is not a valid attribute in colorama.ansi.ansiBack"))
        self.values = []
        self.colors = []
        for i in range(self.height):
            for j in range(self.width):
                self.values.append(char)
                self.colors.append(getattr(colorama.Fore, fore) + getattr(colorama.Back, back))
    def coordsToIndex(self, x, y):
        index = 0
        for i in range(self.height):
            for j in range(self.width):
                if i == y and j == x:
                    return index
                index += 1
    def indexToCoords(self, index):
        for x in range(self.height):
            for y in range(self.width):
                if x * y == index:
                    return x, y
class setPixel:
    def byCoords(screen: screen, x: int, y: int, value: str):
        ischar(value, SyntaxError("value is not a single char"))
        index = 0
        for i in range(screen.height):
            for j in range(screen.width):
                if i == y and j == x:
                    screen.values[index] = value
                index += 1
    def byIndex(screen: screen, index: int, value: str):
        screen.values[index] = value
class getPixel:
    def byCoords(screen: screen, x: int, y: int):
        index = 0
        ret = 0
        for i in range(screen.height):
            for j in range(screen.width):
                if i == y and j == x:
                    ret = screen.values[index]
                index += 1
        return ret
    def byIndex(screen: screen, index):
        return screen.values[index]
class setPixelColor:
    def byCoords(screen: screen, x: int, y: int, fore, back):
        isansifore(fore, SyntaxError(f"{fore} is not a valid attribute in colorama.ansi.ansiFore"))
        isansiback(back, SyntaxError(f"{back} is not a valid attribute in colorama.ansi.ansiBack"))
        index = 0
        for i in range(screen.height):
            for j in range(screen.width):
                if i == y and j == x:
                    screen.colors[index] = getattr(colorama.Fore, fore) + getattr(colorama.Back, back)
                index += 1
    def byIndex(screen: screen, index: int, fore, back):
        isansifore(fore, SyntaxError(f"{fore} is not a valid attribute in colorama.ansi.ansiFore"))
        isansiback(back, SyntaxError(f"{back} is not a valid attribute in colorama.ansi.ansiBack"))
        screen.values[index] = getattr(colorama.Fore, fore) + getattr(colorama.Back, back)
class getPixelColor:
    def byCoords(screen: screen, x: int, y: int):
        index = 0
        ret = 0
        for i in range(screen.height):
            for j in range(screen.width):
                if i == y and j == x:
                    ret = screen.colors[index]
                index += 1
        return ret
    def byIndex(screen: screen, index):
        return screen.colors[index]
class keys:
    def waitForKeys(key1 = "none", key2 = "none", key3 = "none", key4 = "none", key5 = "none", key6 = "none", key7 = "none", key8 = "none", key9 = "none", key10 = "none", key11 = "none", key12 = "none", key13 = "none", key14 = "none", key15 = "none", key16 = "none"):
        press = 0
        while press == 0:
            try:
                keyboard.read_key()
            except KeyboardInterrupt:
                click.clear()
                sys.exit(0)
            if not key1 == "none":
                if keyboard.is_pressed(key1):
                    press = 1
            if not key2 == "none":
                if keyboard.is_pressed(key2):
                    press = 2
            if not key3 == "none":
                if keyboard.is_pressed(key3):
                    press = 3
            if not key4 == "none":
                if keyboard.is_pressed(key4):
                    press = 4
            if not key5 == "none":
                if keyboard.is_pressed(key5):
                    press = 5
            if not key6 == "none":
                if keyboard.is_pressed(key6):
                    press = 6
            if not key7 == "none":
                if keyboard.is_pressed(key7):
                    press = 7
            if not key8 == "none":
                if keyboard.is_pressed(key8):
                    press = 8
            if not key9 == "none":
                if keyboard.is_pressed(key9):
                    press = 9
            if not key10 == "none":
                if keyboard.is_pressed(key10):
                    press = 10
            if not key11 == "none":
                if keyboard.is_pressed(key11):
                    press = 11
            if not key12 == "none":
                if keyboard.is_pressed(key12):
                    press = 12
            if not key13 == "none":
                if keyboard.is_pressed(key13):
                    press = 13
            if not key14 == "none":
                if keyboard.is_pressed(key14):
                    press = 14
            if not key15 == "none":
                if keyboard.is_pressed(key15):
                    press = 15
            if not key16 == "none":
                if keyboard.is_pressed(key16):
                    press = 16
        return press
class sprite:
    def __init__(self, x, y, char, fore, back):
        ischar(char, SyntaxError("char is not a single char"))
        isansifore(fore, SyntaxError(f"{fore} is not a valid attribute in colorama.ansi.ansiFore"))
        isansiback(back, SyntaxError(f"{back} is not a valid attribute in colorama.ansi.ansiBack"))
        self.x = x
        self.y = y
        self.char = char
        self.hidden = True
        self.fore = fore
        self.back = back
    def update(self, screen: screen, update = True, clear = True):
        setPixel.byCoords(screen, self.x, self.y, self.char)
        setPixelColor.byCoords(screen, self.x, self.y, self.fore, self.back)
        if update: screen.update(clear=clear)
    def setChar(self, char):
        ischar(char, SyntaxError("char is not a single char"))
        self.char = char
    def setPos(self, x, y):
        self.x = x
        self.y = y
    def changePos(self, x, y):
        self.x += x
        self.y += y
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y
    def changeX(self, x):
        self.x += x
    def changeY(self, y):
        self.y += y
    def setColor(self, fore, back):
        isansifore(fore, SyntaxError(f"{fore} is not a valid attribute in colorama.ansi.ansiFore"))
        isansiback(back, SyntaxError(f"{back} is not a valid attribute in colorama.ansi.ansiBack"))
        self.fore = fore
        self.back = back
class console:
    def clear():
        click.clear()
class text:
    def write(screen: screen, text: str, x, y, fore, back, update = True, clear = True):
        chars = 0
        currX = x
        currY = y
        for char in text:
            if char == "\n":
                currY += 1
                currX -= chars
                chars = 0
                continue
            if char == "\r":
                continue
            setPixel.byCoords(screen, currX, currY, char)
            setPixelColor.byCoords(screen, currX, currY, fore, back)
            currX += 1
            chars += 1
        if update: screen.update(clear=clear)