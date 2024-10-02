import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

USE_DEVICE_FARM = os.getenv("use_device_farm")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))   #현재 파일 기준 상위 디렉토리 경로를 BASE_DIR에 저장

# Appium 서버 URL 설정
desired_caps = {}
if USE_DEVICE_FARM:
    url = "http://127.0.0.1:4723/wd/hub"
else:
    url = "http://127.0.0.1:4723"
    # 로컬 테스트용 desired_caps 설정
    desired_caps["platformName"] = 'Android'
    desired_caps["deviceName"] = 'emulator-5554'
    desired_caps["automationName"] = 'uiautomator2'
    desired_caps["app"] = 'f"{BASE_DIR}/_sample_apps/test_1.apk'

driver = webdriver.Remote(url, options=UiAutomator2Options().load_capabilities(desired_caps))


# 기존 설치된 앱을 삭제하고 새로 설치하도록 설정
driver.fullReset = True  # 이 옵션으로 기존 앱을 제거하고 새로 설치
# 또는 앱 데이터를 유지하고 싶다면 아래의 옵션을 사용
# driver.noReset = False


def test_1() :
    try:
            # Accessibility ID가 'button_1'인 버튼을 클릭
            button = driver.find_element("accessibility id", "button_1")
            button.click()
            print("버튼 클릭 성공!")
            #time.sleep(10)
    except Exception as e:
            print(f"오류 발생: {e}")

def test_2() :
    try:
        textfild = driver.find_element('class name','android.widget.EditText')
        textfild.click()
        textfild.send_keys('테스트입니다')
        print('입력 성공!')
        time.sleep(10)
    except Exception as e:
        print(f'오류 발생: {e}')

    driver.quit()

