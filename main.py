import os
import pyautogui as pg
from time import sleep
import speech_recognition as sr


def creater():
    os.startfile("C:\\Users\\Josh\\AppData\\Local\\atom\\atom.exe")
    sleep(5)
    '''
    pg.hotkey('ctrl', 'n')
    sleep(1)
    pg.hotkey('ctrl', 'shift', 's')
    sleep(2)
    pg.typewrite('pop.py')
    pg.press('enter')
    sleep(2)'''
    pg.hotkey('winright', 'right')


class CodeBot:
    def __init__(self):
        # Initialize recognizer class (for recognizing the speech)
        self.r = sr.Recognizer()

    def listener(self):
        # Reading Microphone as source
        # listening the speech and store in audio_text variable
        with sr.Microphone() as source:
            print("Talk")
            audio_text = self.r.listen(source)
            print("Time over, thanks")
            try:
                # storing the text in var
                self.txt = str(self.r.recognize_google(audio_text)).lower()
                print("Text: " + self.txt)
            except:
                print("Sorry, I did not get that")

    def checker(self):
        # functions
        mycode = {"import module": self.createImpo,
                  "function": self.createFun,
                  "class": self.createClass,
                  "loop": self.createFor,
                  "while loop": self.createWhile,
                  "print this": self.createPrint,
                  }

        myedit = {
            "talk": self.talk,
            "duplicate": self.duplicate,
            "delete line": self.delLine,
            "find": self.findReplace,
            "commentline": self.commentLine,
        }

        if "code" in self.txt:
            for i in mycode:
                if i in self.txt:
                    mycode[i]()

        elif "edit" in self.txt:
            self.listener()
            for i in myedit:
                if i in self.txt:
                    myedit[i]()

        else:
            print("Not a valid command")

    # coding commands

    def talk(self):
        # codes whatever you say
        self.listener()
        pg.typewrite(self.txt)

    def createImpo(self):
        pg.typewrite("import myModule:")
        pg.press("enter")

    def createClass(self):
        pg.typewrite("class MyClass:")
        pg.press('enter')

    def createFun(self):
        print("function name?")
        self.listener()
        pg.typewrite("def " + self.txt + "():\n\tpass")

    def createFor(self):
        print("in range? or in variable?")
        self.listener()
        if "range" in self.txt:
            print("how much?")
            self.listener()
            pg.typewrite("for i in range " + self.txt + ":")
            pg.press('enter')
        elif "variable" in self.txt:
            print("variable name?")
            pg.typewrite("for i in " + self.txt + ":")
            pg.press('enter')
        else:
            print("Not valid")

    def createWhile(self):
        pg.typewrite("while ")
        print("Condition?")
        self.talk()
        pg.typewrite(":")
        pg.press('enter')

    def createPrint(self):
        print("What to print?")
        self.listener()
        pg.typewrite('print("' + self.txt + '")')
        pg.press('enter')

    # edit commands

    def duplicate(self):
        pg.hotkey('ctrl', 'shiftleft', 'd')

    def delLine(self):
        pg.hotkey('ctrl', 'shiftleft', 'k')

    def findReplace(self):
        pg.hotkey('ctrl', 'f')

        self.listener()
        # enter keys to find
        findThis = self.txt
        pg.typewrite(findThis)

        pg.press('tab')
        # to toggle next
        pg.press('f3')
        # toggle prev
        pg.hotkey('shiftleft', 'f3')

        self.listener()
        replaceTo = self.txt
        # change it to...
        replaceTo = replaceTo
        pg.typewrite(replaceTo)

        print("Replace one or all?")
        self.listener()

        if self.txt == "one":
            pg.press('enter')

        elif self.txt == "all":
            pg.hotkey('ctrl', 'enter')

        pg.press('esc')

    def commentLine(self):
        pg.hotkey('ctrl', '/')


bot = CodeBot()
creater()
sleep(7)
bot.listener()
bot.checker()

# pg.moveTo(220, 1079, duration = 1)
print(pg.position())
