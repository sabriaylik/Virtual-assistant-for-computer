
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
    
   
class voice_files():
    def __init__(self,location):
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        self.browser=webdriver.Chrome("C:/Users/SasKom/chromedriver.exe",options=option)#,options=option
        
        self.browser.get("https://www.google.com/search?q=%C3%A7eviri&oq=%C3%A7eviri&aqs=chrome.0.69i59j69i61l3j0i433l2j0j0i433.1035j0j7&sourceid=chrome&ie=UTF-8")
        self.present_location=location
        # self.files_ham=os.listdir(self.present_location)
        # self.files=self.extract_files(self.files_ham)
        self.files=self.list_folder()
        time.sleep(2)
        self.change_language()
        self.text=""
       
        self.write_box(self.files)
        self.listen_voice()
    
    def write_box(self,kelime):
        self.bosluk=self.browser.find_element_by_id("tw-source-text-ta")
        # self.bosluk.clear()
        self.bosluk.send_keys(kelime+" ")
        time.sleep(0.5)
        # self.turkcesini_al()
        self.listen_voice()
    
    def listen_voice(self):
        self.voice=self.browser.find_element_by_id("tw-src-spkr-button")
        self.voice.click()

    def change_language(self):
        self.language=self.browser.find_element_by_css_selector("#tw-swap > span")
        self.language.click()

    def extract_files(self,files):
        refresh=""
        for file in files:
            refresh+=file.split(".")[0]+" "
        return refresh
    def list_folder(self):
        collect=""
        print("\n\n\t\t\t\t FILES")
        collect+="files"
        for i in os.listdir(self.present_location):
            temp=i.split('.')
            if len(temp)>1:
                print(temp[0])
                collect+=" "+temp[0]
        print("\n\n\t\t\t\tKLASÖRLER")
        collect+=" klasör"
        for i in os.listdir(self.present_location):
            temp=i.split('.')
            if len(temp)<2:
                print(temp[0])
                collect+=" "+temp[0]
        return collect








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



class Ui_MainWindow(object):
    def __init__(self):
        
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.fill_table()
        self.MainWindow.show()
        sys.exit(self.app.exec_())
        
    
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(665, 404)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 80, 231, 231))
        self.table.setLineWidth(1)
        self.table.setTabKeyNavigation(True)
        self.table.setShowGrid(True)
        self.table.setRowCount(3)
        self.table.setObjectName("table")
        self.table.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(0, 1, item)
        
        self.blind = QtWidgets.QCheckBox(self.centralwidget)
        self.blind.setGeometry(QtCore.QRect(30, 310, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.blind.setFont(font)
        self.blind.setChecked(True)
        self.blind.setObjectName("blind")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(340, 79, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.start_btn.setFont(font)
        self.start_btn.setStyleSheet("")
        self.start_btn.setObjectName("start_btn")
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setGeometry(QtCore.QRect(450, 79, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.stop_btn.setFont(font)
        self.stop_btn.setObjectName("stop_btn")
        self.sleep_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sleep_btn.setGeometry(QtCore.QRect(340, 139, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.sleep_btn.setFont(font)
        self.sleep_btn.setObjectName("sleep_btn")
        self.sleep_time = QtWidgets.QSpinBox(self.centralwidget)
        self.sleep_time.setGeometry(QtCore.QRect(460, 140, 91, 41))
        self.sleep_time.setObjectName("sleep_time")
        self.search_field = QtWidgets.QTextEdit(self.centralwidget)
        self.search_field.setGeometry(QtCore.QRect(80, 30, 161, 31))
        self.search_field.setObjectName("search_field")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(6, 10, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 210, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.command_text = QtWidgets.QTextEdit(self.centralwidget)
        self.command_text.setGeometry(QtCore.QRect(350, 210, 121, 31))
        self.command_text.setObjectName("command_text")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(480, 210, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.process_text = QtWidgets.QTextEdit(self.centralwidget)
        self.process_text.setGeometry(QtCore.QRect(540, 210, 121, 31))
        self.process_text.setObjectName("process_text")
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(410, 250, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.add_btn.setFont(font)
        self.add_btn.setObjectName("add_btn")
        self.update_btn = QtWidgets.QPushButton(self.centralwidget)
        self.update_btn.setGeometry(QtCore.QRect(410, 300, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.update_btn.setFont(font)
        self.update_btn.setObjectName("update_btn")
        self.given_command = QtWidgets.QLabel(self.centralwidget)
        self.given_command.setGeometry(QtCore.QRect(290, 20, 351, 31))
        self.given_command.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 255);")
        self.given_command.setObjectName("given_command")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 665, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.case_see=True
        
        self.blind.toggled.connect(self.blind_changed)
        self.start_btn.clicked.connect(self.start_button_clicked)
        self.stop_btn.clicked.connect(self.stop_button_clicked)
        self.sleep_btn.clicked.connect(self.sleep_button_clicked)
        self.add_btn.clicked.connect(self.add_button_clicked)
        self.update_btn.clicked.connect(self.update_button_clicked)
        
        
        
    
   
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.table.setSortingEnabled(False)
        item = self.table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Command"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Process"))
        __sortingEnabled = self.table.isSortingEnabled()
        self.table.setSortingEnabled(False)
        self.table.setSortingEnabled(__sortingEnabled)
        self.blind.setText(_translate("MainWindow", "Blind"))
        self.start_btn.setText(_translate("MainWindow", "Start"))
        self.stop_btn.setText(_translate("MainWindow", "Stop"))
        self.sleep_btn.setText(_translate("MainWindow", "Sleep"))
        self.label.setText(_translate("MainWindow", "Search:"))
        self.label_2.setText(_translate("MainWindow", "Command:"))
        self.label_3.setText(_translate("MainWindow", "İşlem:"))
        self.add_btn.setText(_translate("MainWindow", "Add"))
        self.update_btn.setText(_translate("MainWindow", "Update"))
        self.given_command.setText(_translate("MainWindow", "Given Command:"))

    
    def fill_table(self):
        
        file_name="command_operation.txt"
        command=[]
        process=[]
        count=0
        f=open(file_name)
        file=f.read().split(',')
        for i in file:
            # print(i,"\n")
            if count%2==0:
                command.append(i)
            else:
                process.append(i)
            count+=1
        row=0
        self.table.setRowCount(len(command))
        for i in command:
            self.table.setItem(row,0,QtWidgets.QTableWidgetItem(i))
            row+=1
        row=0
        for i in process:
            self.table.setItem(row,1,QtWidgets.QTableWidgetItem(i))
            row+=1
            

    def blind_changed(self):
        pass

    def start_button_clicked(self):
        
        
        self.MainWindow.hide()
        self.file_name="command-process.txt"
        
        self.process_control=Process()
        x=True
        while x:
            self.said=voice_listen()
            if self.said=='arayüz':
                x=False
                self.MainWindow.show()
            else :
                self.process_control.operation(self.said)
                
                
     
    
    
        
    
    def stop_button_clicked(self):
        
        self.run=False
    def sleep_button_clicked(self):
        
        
        self.sleep_time_value=self.sleep_time.value()
        
        self.MainWindow.hide()
        time.sleep(self.sleep_time_value*60)
        self.MainWindow.show()
    def add_button_clicked(self):
       
        pass
    def update_button_clicked(self):
        pass
    
   
    

    def find_present_location(self):
        print("\n\t\t\t Present location:"+self.present_location)
        
    def go_location(self,git):
        self.new_location=git
    def enter_folder(self,file):
        self.present_location+=file
        self.present_location+="\\"
    def open_file(self,file_name):
        self.file_path=self.present_location+"\\"+file_name
        os.startfile(self.file_path)
    def list_folder(self):
        for i in os.listdir(self.present_location):
            print(i)
        






if __name__ == "__main__":
    ekran=Ui_MainWindow()
    
