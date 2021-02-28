from selenium import webdriver
import json
import time

class Test_weixin():
    def setup_method(self, method):
        ch_arg = webdriver.ChromeOptions()
        ch_arg.debugger_address = '127.0.0.1:9022'
        self.driver = webdriver.Chrome()        # options=ch_arg, 输入时按这种模式输入，否则会引发其他问题
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_get_cookie(self):
        '''
        before：chrome -remote-debugging-port=9022  //chrome.exe浏览器路径加入环境变量运行此命令，开启debug模式
        cur_opration:浏览器debug模式下，获取登录后的cookie。
        :return:
        '''
        cookies = self.driver.get_cookies()
        print('cookies:', cookies)
        with open('cookies.txt', 'w', encoding='utf-8') as f:
            json.dump(cookies, f)

    def test_cookie_login(self):
        '''
        正常模式，使用cookie登录企业微信。
        :return:
        '''
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        with open("cookies.txt", "r", encoding="utf-8") as f:
            cookies = json.load(f)
        for i in cookies:
            self.driver.add_cookie(i)
        self.driver.refresh()
        time.sleep(9)
