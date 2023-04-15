import random
import pyautogui as pg 
import time
quality = ('pure as moon🌚', 'sweet as mango🥭', 'cute as panda🐼')
love = ('like💖', 'love❤️', 'miss😘')
time.sleep(8)
for i in range(200):
    a = random.choice(quality)
    b = random.choice(love)
    pg.write(" You are as "+a" \n ")
    pg.write(" I "+ b +" you")
    pg.press('enter')
