from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 웹드라이버 경로 설정
driver_path = 'C:/user/chromedriver_win32/chromedriver.exe'

# Chrome 웹드라이버 인스턴스 생성 (executable_path 사용)
driver = webdriver.Chrome(executable_path=driver_path)

# 구글에 접속
driver.get("http://www.google.com")

# 검색어 입력
search_box = driver.find_element_by_name("q")
search_box.send_keys("lofa")

# 검색 실행
search_box.send_keys(Keys.RETURN)

# 결과를 로드하는 동안 기다림
time.sleep(5)

# 결과 페이지의 HTML을 출력 (옵션)
print(driver.page_source)

