import os
import pyautogui as pg
from time import sleep
import speech_recognition as sr


def creator():
    os.startfile("C:\\Users\\Josh\\AppData\\Local\\atom\\atom.exe")
    sleep(5)
    pg.hotkey('ctrl', 'n')
    sleep(1)
    pg.hotkey('ctrl', 'shift', 's')
    sleep(2)
    pg.typewrite('poop.py')
    pg.press('enter')
    sleep(2)
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
            audio_text = self.r.listen(source, phrase_time_limit=5)
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
                  "for loop": self.createFor,
                  "while loop": self.createWhile,
                  "print": self.createPrint,
                  "create list": self.list,
                  "append list": self.appendList,
                  }

        myedit = {
            "talk": self.talk,
            "duplicate": self.duplicate,
            "delete line": self.delLine,
            "find": self.findReplace,
            "comment line": self.commentLine,
            "undo" : self.undo,
        }

        self.listener()
        if "edit" in self.txt:
            self.listener()
            for i in myedit:
                if i in self.txt:
                    myedit[i]()

        elif "code" in self.txt:
            self.listener()
            for i in mycode:
                if i in self.txt:
                    mycode[i]()

        else:
            print("choose to code or edit")

        self.checker()


    # coding commands

    def talk(self):
        # codes whatever you say
        self.listener()
        pg.typewrite(self.txt)
        

    def createImpo(self):
        pg.typewrite("import myModule:")
        pg.press("enter")

    def list(self):
        print("list name?")
        self.listener()
        pg.typewrite(self.txt + " = []")
        pg.press('enter')
        
    def appendList(self):
        print("list name")
        self.listener()
        var = self.txt
        print("elements to append")
        self.listener()
        pg.typewrite(var + ".append(" + self.txt +")")

    def createClass(self):
        print("class name?")
        self.listener()
        cl = self.txt
        cl = cl[0].upper() + cl[1:]
        pg.typewrite("class " + cl +":")
        pg.press('enter')

    def createFun(self):
        print("function name?")
        self.listener()
        pg.typewrite("def " + self.txt + "():\npass")
        pg.press('enter')
        pg.press('backspace')


    def createFor(self):
        print("in range or in variable?")
        self.listener()
        if "range" in self.txt:
            print("how much?")
            self.listener()
            pg.typewrite("for i in range " + self.txt + ":")
            pg.press('enter')
        elif "variable" in self.txt:
            print("variable name?")
            self.listener()
            pg.typewrite("for i in " + self.txt + ":")
            pg.press('enter')


    def createWhile(self):
        pg.typewrite("while ")
        print("Condition?")
        self.talk()
        pg.typewrite(":")
        pg.press('enter')

    def createPrint(self):
        print("variable or text")
        self.listener()
        if "variable" in self.txt:
            print("variable name?")
            self.listener()
            pg.typewrite("print(" + self.txt + ")")
            pg.press('enter')
        elif "text" in self.txt:
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
        pg.hotkey('ctrlleft', '/')

    def undo(self):
        pg.hotkey( 'ctrlleft' ,'z')



bot = CodeBot()
bot.checker()

