import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
import time
from selenium.webdriver.common.keys import Keys

USE_DEVICE_FARM = os.getenv("use_device_farm")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))   #현재 파일 기준 상위 디렉토리 경로를 BASE_DIR에 저장

# Appium 서버 URL 설정
desired_caps = {}
if USE_DEVICE_FARM:
    url = "http://127.0.0.1:4723/wd/hub"
else:
    url = "http://127.0.0.1:4723"
    # 로컬 테스트용 desired_caps 설정
    desired_caps["platformName"] = "Android"
    desired_caps["deviceName"] = "emulator-5554"
    desired_caps["automationName"] = "uiautomator2"
    desired_caps["appPackage"] = "com.google.android.youtube"  # 유튜브 앱 패키지 이름
    desired_caps["appActivity"] = "com.google.android.youtube.HomeActivity"  # 유튜브 앱 기본 액티비티

driver = webdriver.Remote(url, options=UiAutomator2Options().load_capabilities(desired_caps))

try:
    # 유튜브 검색결과 확인
    # 1.알림 팝업 닫기 클릭
    alarm = driver.find_element('id', 'com.android.permissioncontroller:id/permission_deny_button').click()
    serch_click = driver.find_element('accessibility id','Search YouTube').click()
    #2.검색어 입력하기
    serch_input = driver.find_element('id','com.google.android.youtube:id/search_edit_text')
    serch_input.send_keys('kpop')
    #3.입력한 검색어 클릭
    driver.find_element('xpath','//android.widget.TextView[@resource-id="com.google.android.youtube:id/text" and @text="kpop"]').click()
    #4.검색 결과 확인하기
    time.sleep(2)
#     video = driver.find_element('class','android.view.ViewGroup')
#     videoname = video.getattribute('content-desc')
#     print(videoname)
    time.sleep(10)

except Exception as e:
    print(f"오류 발생: {e}")  # 오류 발생 시 출력
finally:
    # 드라이버 종료
    driver.quit()


