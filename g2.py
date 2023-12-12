from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Chrome 웹드라이버 인스턴스 생성 (ChromeDriverManager 사용)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# 구글에 접속
driver.get("http://www.google.com")

# 검색어 입력
search_box = driver.find_element(By.NAME, "q")

search_box.send_keys("lofa 한국지방재정공제회")

# 검색 실행
search_box.submit()

# 결과를 로드하는 동안 기다림
time.sleep(5)

# 결과 페이지의 HTML을 출력 (옵션)
driver.save_screenshot('search_results.png')

# 브라우저 닫기
driver.quit()
