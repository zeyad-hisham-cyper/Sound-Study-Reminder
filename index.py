import os
import time
from turtle import *
from gtts import gTTS

setup()
t1 = Turtle() 

seconds = 0
minutes = 0
hours = 0


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("audio.mp3")


while True:
    t1.clear()
    t1.write(str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2),
             font=("arial", 50, "italic"))
    seconds = seconds + 1
    time.sleep(1)
    if seconds == 60:
        seconds = 0
        minutes = minutes + 1
    if minutes == 60:
        minutes = 0
        hours = hours + 1
    if minutes == 0 and seconds == 0:
        speak("Time")
    if hours == 24:
        hours = 0
