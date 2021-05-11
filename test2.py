import speech_recognition as sr

r = sr.Recognizer()


def createFor():
    print("for created")


def createWhile():
    print("while created")

def createFun():
    print("function created")

def createImpo():
    print("module imported")


mydict = {"loop": createFor,
          "while loop" : createWhile,
          "import module" : createImpo,
          "function" : createFun,}


with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
    try:
        # storing the text in var
        txt = str(r.recognize_google(audio_text)).lower()
        print("Text: " + txt)
    except:
        print("Sorry, I did not get that")



for i in mydict:
    if i in txt:
        mydict[i]()
    else:
        print("nada")
