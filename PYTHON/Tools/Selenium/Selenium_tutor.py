from tkinter import *
from tkinter.ttk import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import threading
import time
import requests as req
from bs4 import BeautifulSoup
import subprocess

class app(Tk):
    def __init__(self):
        super().__init__()
        self.mainframe = Frame(self)
        self.mainframe.place(relwidth=1, relheight=1)
        self.w = self.winfo_screenwidth()
        self.h = self.winfo_screenheight()
        self.pos = ((0, 0), (self.w // 2 - 1, 0), (0, self.h //
                    2 - 1), (self.w // 2 - 1, self.h // 2 - 1))
        self.threads = []
        self.creat_window()
        self.creat_text()
        self.creat_thread(4)
        self.creat_button()

    def creat_text(self):
        self.debug = Listbox(self.mainframe)
        self.debug.place(relwidth=1, relheight=0.25)

    def creat_window(self):
        self.title('MMO FB TOOL ONLINE')
        self.minsize(600, 400)
        self.maxsize(600, 400)

    def creat_button(self):
        Button(self.mainframe, text='Start', command=self.start_procession).place(
            relheight=0.1, relwidth=0.25, rely=.75, relx=0.5)
        Button(self.mainframe, text='END', command=self.end_procession).place(
            relheight=0.1, relwidth=0.25, rely=.75,relx=0.75)

    def creat_thread(self, num_thread):
        self.threads = [threading.Thread(target=self.procession, args=(i,)) for i in range(num_thread)]

    def start_procession(self):
        for thread in self.threads:
            thread.start()
            self.debug.insert(0, f'Started Thread {thread.name}')
            time.sleep(1)
    def end_procession(self):
        for thread in self.threads:
            thread.join()
            time.sleep(1)
        self.debug.insert(0, 'END process')

    def procession(self, id):
        options = webdriver.ChromeOptions()
        options.add_argument('--app=https://facebook.com/login')
        driver = webdriver.Chrome(options=options)
        x, y = id * 200, 0
        driver.set_window_rect(x, y, 200, 450)
        
        # Uncomment and update with actual credentials and logic
        # email = driver.find_element(By.ID, 'email')
        # password = driver.find_element(By.ID, 'pass')
        # email.send_keys('your-email@example.com')
        # password.send_keys('your-password')
        # login_btn = driver.find_element(By.ID, 'loginbutton')
        # login_btn.click()
        
        self.debug.insert(0, f'Login acc {id+1} thanh cong')
        time.sleep(1000)  # Simulate long-running task
        driver.quit()  # Close the browser after the task

    def run(self):
        self.mainloop()

if __name__ == '__main__':
    App = app()
    # App.run()


link = 'https://www.uhdpaper.com/search?q=Cat&by-date=true'


service = ChromeService(executable_path=ChromeDriverManager().install())
service.creationflags = subprocess.CREATE_NO_WINDOW
driver = webdriver.Chrome(service=service)

driver.get(link)
time.sleep(100)
# request = req.get(link)

html = driver.page_source
driver.quit()
soup = BeautifulSoup(html,'lxml')
print(soup)


for l in soup.find_all('img'):
    print(l.get('src'))