import os
import pyautogui as pg
from time import sleep
import speech_recognition as sr


class CodeBot:
    def __init__(self):
        # Initialize recognizer class (for recognizing the speech)
        self.r = sr.Recognizer()

    def creater(self):
        os.startfile("C:\\Users\\Josh\\AppData\\Local\\atom\\atom.exe")
        sleep(5)
        pg.hotkey('ctrl', 'n')
        sleep(1)
        pg.hotkey('ctrl', 'shift', 's')
        sleep(2)
        pg.typewrite('pop.py')
        pg.press('enter')
        sleep(2)
        pg.hotkey('winright', 'right')

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
        self.mykeys = {"import module": self.createImpo,
                       "function": self.createFun,
                       "class": self.createClass,
                       "for loop": self.createFor,
                       "while loop": self.createWhile,
                       "print this": self.createPrint,
                       }

        for i in self.mykeys:
            if i in self.txt:
                self.mykeys[i]()
            else:
                print("nada")

    def createImpo(self):
        pass

    def createClass(self):
        pg.typewrite("class MyClass:\n\t")

    def createFun(self):
        pass
        '''print("function name?")
        self.listener()
        pg.typewrite("def " + self.txt + "():\n\tpass")'''

    def createFor(self):
        pass
        '''print("in range? or in variable?")
        self.listener()
        if "range" in self.txt:
            print("how much?")
            self.listener()
            pg.typewrite("for i in range " + self.txt + ":\n\t")
        elif "variable" in self.txt:
            print("variable name?")
            pg.typewrite("for i in " + self.txt + ":\n\t")
        else:
            print("Not valid")'''

    def createWhile(self):
        pass

    def createPrint(self):
        print("khj")







bot = CodeBot()
bot.creater()
sleep(7)
bot.listener()
bot.checker()

# pg.moveTo(220, 1079, duration = 1)
print(pg.position())
