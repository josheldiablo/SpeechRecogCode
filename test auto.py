import pyautogui as pg
import os
from time import sleep



def duplicate():
    pg.hotkey('ctrl', 'shiftleft', 'd')

def delLine():
    pg.hotkey('ctrl', 'shiftleft', 'k')
    
def findReplace():
    pg.hotkey('ctrl', 'f')
    #enter keys to find
    findThis = 'self'
    pg.typewrite(findThis)
    pg.press('tab')
    #to toggle next
    pg.press('f3')
    #toggle prev
    pg.hotkey('shiftleft', 'f3')
    #change it to...
    replaceTo = 'josh'
    pg.typewrite(replaceTo)
    #if replace one
    pg.press('enter')
    pg.press('esc')
    #if replace all
    pg.hotkey('ctrl', 'enter')
    pg.press('esc')
    
def commentLine():
    pg.hotkey('ctrl', '/')
    

os.startfile("C:\\Users\\Josh\\AppData\\Local\\atom\\atom.exe")
sleep(3)
findReplace()
print(pg.position())