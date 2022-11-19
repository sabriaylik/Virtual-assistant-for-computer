
import time



 
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

