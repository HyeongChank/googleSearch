from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def operate(keywords):
    for key in keywords:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("http://www.google.com")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(key)
        search_box.submit()
        time.sleep(5)
        driver.quit()

if __name__=="__main__":
    keywords = ['lofa 한국지방재정공제회', '로파 한국지방재정공제회']
    operate(keywords)