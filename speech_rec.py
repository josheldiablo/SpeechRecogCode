#import library
import os
import speech_recognition as sr


class Recog:

    def __init__(self):
        # Initialize recognizer class (for recognizing the speech)
        self.r = sr.Recognizer()
        # Reading Microphone as source
        # listening the speech and store in audio_text variable

        # creating a file
        self.fd = "test.txt"
        # popen() is similar to open()
        self.file = open(self.fd, 'w')

    def listener(self):
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

    def check(self):
        fun_lists = ["for loop", "while loop"]

    def when_for(self):
        #checking if its a for loop
        if ('for' in self.txt):
            #if true asking for a range
            print("Range?")
            self.listener()
            #storing range in a var
            loop_range = self.r.recognize_google(self.txt)
            #storing full text in a value
            loop_lim = "for i in range {rangee}:".format(rangee = loop_range)
            print(loop_lim)
            #writing text
            self.file.write(loop_lim)
            self.file.close()
            print("\n\t")

    def when_while(self):
        #checking if its a for loop
        if ('for' in self.txt):
            #if true asking for a range
            print("Range?")
            self.listener()
            #storing range in a var
            loop_range = self.r.recognize_google(self.txt)
            #storing full text in a value
            loop_lim = "for i in range {rangee}:".format(rangee = loop_range)
            print(loop_lim)
            #writing text
            self.file.write(loop_lim)
            self.file.close()
            print("\n\t")

    def readfile(self):
        self.file = open(self.fd, 'r')
        text = self.file.read()
        print(text)


bot = Recog()
bot.listener()
bot.when_for()
bot.readfile()
