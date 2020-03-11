from selenium import webdriver
from time import sleep
from secrets import username, password, message


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome("C:/Program Files (x86)/Programming/Tindish/chromedriver.exe")

    def login(self):
        self.driver.maximize_window()
        self.driver.get('https://tinder.com')

        sleep(4)

        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_btn.click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        self.driver.switch_to.window(base_window)

        sleep(3)

        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        sleep(1)

        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()


    def click_girl(self):
        click_girl = self.driver.find_element_by_xpath('//*[@id="matchListNoMessages"]/div[1]/div[2]/a/div[1]')
        click_girl.click()

    def type_message(self):
        type_message = self.driver.find_element_by_xpath('//*[@id="chat-text-area"]')
        type_message.send_keys(message)

    def send(self):
        send = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button/span')
        send.click()

    def click_x(self):
        click_x = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div/button')
        click_x.click()

    def message(self):
        sleep(1)
        self.click_girl()
        sleep(1)
        self.click_x()
        while True:
            sleep(1)
            self.type_message()
            sleep(2)
            self.send()

    #def like(self):
    #    like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
    #    like_btn.click()

    #def dislike(self):
    #    dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
    #    dislike_btn.click()

    #def auto_swipe(self):
    #    while True:
    #        sleep(0.5)
    #        try:
    #            self.like()
    #        except Exception:
    #            try:
    #                self.close_popup()
    #            except Exception:
    #                self.close_match()

    #def close_popup(self):
    #    popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
    #    popup_3.click()

    #def close_match(self):
    #    match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
    #    match_popup.click()

bot = TinderBot()
bot.login()
bot.message()