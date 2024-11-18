import time
import json
import keyboard
import random
import tkinter as tk
from pathlib import Path

from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from tkinter.messagebox import showerror, showwarning, showinfo

ID = "id"
NAME = "name"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"

def saveProfile(login,password):
        options = wd.ChromeOptions()
        options.add_experimental_option("detach",True)
        service = Service(ChromeDriverManager().install())

        browser = wd.Chrome(service=service,options=options)
        browser.get('https://steamcommunity.com/login/home/')
        time.sleep(1)

        open_search = browser.find_element(By.CLASS_NAME, "_3BkiHun-mminuTO-Y-zXke")
        open_search.click()


        search = browser.find_element(By.CLASS_NAME,"_2GBWeup5cttgbTw8FM3tfx")
        search.send_keys(login)

        time.sleep(1)

        search = browser.find_element(By.XPATH, "//input[@class='_2GBWeup5cttgbTw8FM3tfx'][@type='password']")
        search.send_keys(password)

        search = browser.find_element(By.CLASS_NAME,"DjSvCZoKKfoNSmarsEcTS")
        search.click()

        keyboard.wait("ctrl+shift+h") #Для окончания авторизации

        cookies = browser.get_cookies()

        with open('cookies.json', 'w') as file:
            json.dump(cookies, file)

        browser.close()

def changingPaint():
    options = wd.ChromeOptions()
    options.add_experimental_option("detach",True)
    #options.add_argument("--headless=new")
    service = Service(ChromeDriverManager().install())
    driver = wd.Chrome(service=service,options=options)
    driver.get('https://steamcommunity.com/id/self/edit/showcases')
    with open('cookies.json', 'r') as file:
        cookies = json.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
    driver.refresh()
    try:
        time.sleep(5)
        search = driver.find_element(By.ID,"showcase_8_notes")
        search.click()
        time.sleep(1)
        search.clear()
        folder_name = "Paints"
        folder = Path(folder_name)
        n = len(list(folder.iterdir()))

        file = open(f"Paints/{random.randint(1,n)}.txt","r",encoding="utf8")
        for i in file.readlines():
            search.send_keys(i)
        
        time.sleep(1)
        open_search = driver.find_element(By.XPATH, "//*[@id='react_root']/div[3]/div[2]/div/form/div[4]/button[1]")
        #//*[@id="react_root"]/div[3]/div[2]/div/form/div[4]/button[1]
        #//*[@id='react_root']/div[3]/div[2]/div/form/div[4]/button[1]
        open_search.click()
        time.sleep(1)
        driver.close()
    except:
         driver.close()
         showerror(title="Error", message="Information input field is missing")


root = tk.Tk()
root.title("Steam Painter")
root.minsize(width=300, height=150)
root.iconbitmap(default="icon.ico")


# Центрируем содержимое окна
content_frame = tk.Frame(root)
content_frame.pack(expand=True, fill='both')

# Поле для ввода логина
label_login = tk.Label(content_frame, text="Login:")
label_login.place(relx=0.25, rely=0.15, anchor='center')
entry_login = tk.Entry(content_frame)
entry_login.place(relx=0.75, rely=0.15, anchor='center')

# Поле для ввода пароля
label_password = tk.Label(content_frame, text="Password:")
label_password.place(relx=0.25, rely=0.30, anchor='center')
entry_password = tk.Entry(content_frame, show="*")  # Скрываем символы пароля
entry_password.place(relx=0.75, rely=0.30, anchor='center')

# Выпадающий список с выбором "Да" или "Нет"
#option_var = tk.StringVar(value="Yes")  # Начальное значение - "Да"
#choices = ["Yes", "No"]
#label_choice = tk.Label(content_frame, text="Automatic start \n with the system")
#label_choice.place(relx=0.25, rely=0.45, anchor='center')
#dropdown = tk.OptionMenu(content_frame, option_var, *choices)
#dropdown.config(width=10)
#dropdown.place(relx=0.75, rely=0.45, anchor='center')

button_save = tk.Button(content_frame, text="Save login settings", command=lambda: saveProfile(login = entry_login.get(),password = entry_password.get()))
button_save.place(relx=0.35, rely=0.60, anchor='center')

button_run = tk.Button(content_frame, text="Test script", command=lambda: changingPaint())
button_run.place(relx=0.75, rely=0.60, anchor='center')

root.mainloop()
