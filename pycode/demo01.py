from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(r"F:\作业\python\浏览器驱动\chromedriver_win32\chromedriver.exe")
wd = webdriver.Chrome(service=s)

wd.get("https://www.bilibili.com/")