from selenium import webdriver as wd 
from bs4 import BeautifulSoup
import time

driver = wd.Chrome(executable_path=r"C:\Users\user\Desktop\CODE\gui_basic\.vscode\webscraping_basic\chromedriver.exe")
url = 'https://www.bilibili.com/video/BV1Pp4y1Y7EE?from=search&seid=9827543888492460575'
driver.get(url)

last_page_height = driver.execute_script("return document.documentElement.scrollHeight") 

while True: 
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);") 
    time.sleep(3.0) 
    new_page_height = driver.execute_script("return document.documentElement.scrollHeight")
    
    if new_page_height == last_page_height: 
        break 
    last_page_height = new_page_height
    
    
html_source = driver.page_source

driver.close()

soup = BeautifulSoup(html_source, 'lxml')


find_elements_by_xpath( "//*[@id='comment']/div/div[2]/div/div[4]/div[6]/div[2]/p " )