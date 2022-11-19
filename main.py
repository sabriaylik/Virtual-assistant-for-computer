
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time
import keyboard
import os
import speech_recognition as sr
from os import path

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser


import UI
from UI import Ui_MainWindow

def voice_listen():
    
    r=sr.Recognizer()    
    with sr.Microphone() as source:
        os.system("\n\n\n\n\n\n")
        print("listening")
        audio=r.record(source,duration=3)
        try:
            command=r.recognize_google(audio,language="en-us").lower()
            print(command,len(command))
            return command
                
        except:
            str="nothing was said"
            return str
    
if __name__ == "__main__":
    ekran=Ui_MainWindow()
    
