

import VoiceFiles

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



class Process():
    def __init__(self):
        self.present_location="E:\\"
        self.temp_konum="E:\\"
        # self.operation()
        pass
    def find_present_location(self):
        print("\n\n\n\n\n\t\t\t Present Location:"+self.present_location)
        
    def go_location(self,go):
        self.new_location=go
    def enter_folder(self,folder):
        if path.isdir(self.present_location+folder):
                self.present_location+=folder
                self.present_location+="\\"
        else:
            print("don't find location ")
        self.find_present_location()
        self.list_folder()
    def slide_control(self):
        time.sleep(5)
        keyboard.press_and_release("F5")
        time.sleep(1)
        command=""
        while command!="close":
            command=voice_listen()
            # print("slayt komut:",komut,len(komut))
            if command=="next":
                keyboard.press_and_release("right arrow")
            elif command=="back":
                keyboard.press_and_release("left arrow")
            elif command=="exit":
                keyboard.press_and_release("Esc")
            else :
                pass
        self.close_program()
    def video_control(self):
        
        keyboard.press_and_release("Enter")
        time.sleep(1)
        komut=""
        while komut!="close":
            komut=voice_listen()
            # print("slayt komut:",komut,len(komut))
            if komut=="next":
                keyboard.press_and_release("right arrow")
            elif komut=="back":
                keyboard.press_and_release("left arrow")
            elif komut=="exit":
                keyboard.press_and_release("Esc")
            else :
                pass
        self.close_program()
    def open_file(self,file_name):
        
        for i in os.listdir(self.present_location):
            temp=i.split('.')
            if temp[0]==file_name:
                self.present_extension=temp[1]
                os.startfile(self.present_location+i)
                if(self.present_extension=="pptx"):
                    self.slide_control()
                if(self.present_extension=="mp4"):
                    self.video_control()
    def list_folder(self):
        print("\n\n\t\t\t\t FILES")
        for i in os.listdir(self.present_location):
            temp=i.split('.')
            if len(temp)>1:
                print(temp[0])
        print("\n\n\t\t\t\t FOLDERS")
        for i in os.listdir(self.present_location):
            temp=i.split('.')
            if len(temp)<2:
                print(temp[0])
        
    def go_back(self):
        location=self.present_location.split("\\")
        location2=""
        for i in range(0,len(location)-2):
            location2+=location[i]  +"\\" 
        print(location2)
        self.present_location=location2
        self.list_folder()
    def close_program(self):
        extensions=["mp3","docx","mp4","pptx","txt"]
        programs=["wmplayer","WINWORD","GOM","POWERPNT","notepad"]
        
        for i in range(len(extensions)):
            if self.present_extension==extensions[i]:
                os.system("taskkill /IM " + programs[i]+".exe")
    def choice_check(self,choice):
        control=False#
        for i in os.listdir(self.present_location):#klasörleri listeleme
            temp=i.split('.')
            if len(temp)<2:
                if temp[0]==choice:
                    control=True#tercih dosya
        return control
    
    def remove(self,command):
        command=command.split(" ")
        file=str(command[1:])
        kind=self.choice_check(file)
        if kind:
            os.rmdir(self.present_location+file)
        else:
            os.remove(self.present_location+file)
    
    def update(self,command):
        command=command.split(" ")
        file=str(command[1:])
        
    def operation(self,command):
        print("*"*30)
        sayac=int(0)
        self.find_present_location()
        self.list_folder()
        
        self.selection=command
        kind=self.choice_check(self.selection)
        print("\n\n\t\t KOMUT :",sayac," :",self.selection)
        sayac+=1
        if self.selection!="bir şey söylenmedi":
            if self.selection == "previous":
               self.go_back() 
            elif self.selection=="close":
                self.close_program()
            elif self.selection=="voice":
                run=voice_files(self.present_location)
            elif self.selection.split(" ")[0]=="remove":
                self.remove(self.selection)
            elif self.selection.split(" ")[0]=="update":
                self.remove(self.selection)
            elif self.selection=="folder 1": 
                self.present_location="C:\\"
            elif self.selection=="folder 2": 
                self.present_location="E:\\"
            else:
                if kind:
                    self.enter_folder(self.selection)
                else:
                    self.open_file(self.selection)
        else:   
            print("don't give command")
