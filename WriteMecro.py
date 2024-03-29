import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class WriteMecro:

    def dc_mecro(self, title):

        print("start mecro")

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("window-size=1920x1080")
        options.add_argument(
            "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
            )
        options.add_argument("lang=ko_KR")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        
        driver.get("https://gall.dcinside.com/mini/board/write/?id=iana")  # 갤러리 글쓰기 주소
        print("셀레니움 작동")
        time.sleep(2)

        driver.find_element(By.ID, "btn_gall_nick_name_x").click()

        driver.implicitly_wait(5)
        driver.find_element(By.NAME, "name").send_keys(u'알림 테스트')  # 닉네임

        driver.implicitly_wait(5)

        time.sleep(2)

        driver.find_element(By.NAME, "password").send_keys(u'12345')  # 비밀번호

        driver.implicitly_wait(5)

        time.sleep(1)

        driver.find_element(By.XPATH, "//*[@id='write']/div[1]/fieldset/div[3]/ul/li[1]").click()

        time.sleep(1)

        driver.find_element(By.NAME, "subject").send_keys(u'방송 on [테스트 중]')  # 제목

        driver.implicitly_wait(5)

        time.sleep(1)

        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@name='tx_canvas_wysiwyg']"))

        time.sleep(1)

        driver.find_element(By.TAG_NAME, "body")\
            .send_keys(u"이아나 방송 알림봇[임시] \n방송제목 : "
                       + title + "\n방송주소 : https://play.afreecatv.com/ianavlup/253343223\n")

        time.sleep(1)

        # 글등록
        driver.switch_to.default_content()
        print("글 등록 완료")
        time.sleep(5)

        driver.find_element(By.CSS_SELECTOR, 'button.btn_lightpurple.btn_svc.write').click()
        driver.implicitly_wait(5)
        print("글 등록 완료")
        time.sleep(1)

        driver.close()

    def ruri_mecro(self):
        service = Service(executable_path=r'C:/Windows/chromedriver.exe')
        options = webdriver.ChromeOptions()
        options.add_argument('window-size=1920x1080')

        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36")

        driver = webdriver.Chrome(service=service, options=options)

        driver.get("https://user.ruliweb.com/member/login")  # 갤러리 목록 주소

        driver.implicitly_wait(3)

        time.sleep(3)

        # time.sleep(2)

        driver.find_element(By.ID, "user_id").send_keys(u'')  # 비밀번호

        driver.implicitly_wait(1)

        driver.find_element(By.ID, "user_pw").send_keys(u'')  # 비밀번호

        driver.implicitly_wait(1)

        driver.find_element(By.ID, 'login_submit').click()
        time.sleep(3)

        driver.get("https://bbs.ruliweb.com/community/board/301000/write")  # 갤러리 목록 주소
        time.sleep(3)

        driver.find_element(By.ID, "subject").send_keys(u'test')  # 비밀번호

        driver.implicitly_wait(1)

        driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='editor_v2']/div/div[3]/div/div[2]/div[3]/div[2]"))
        driver.find_element(By.ID, "editor_v2").send_keys(u'test body')  # 비밀번호
        time.sleep(30)
