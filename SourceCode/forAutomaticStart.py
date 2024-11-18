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

def changingPaint():
    options = wd.ChromeOptions()
    options.add_experimental_option("detach",True)
    options.add_argument("--headless=new")
    service = Service(ChromeDriverManager().install())

    driver = wd.Chrome(service=service,options=options)
    driver.get('https://steamcommunity.com/id/self/edit/showcases')
    with open('cookies.json', 'r') as file:
        cookies = json.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)

    driver.refresh()
    try:
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

changingPaint()