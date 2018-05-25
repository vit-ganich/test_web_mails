# -*- coding: utf-8 -*-
import time
import os
import pyautogui
import logging
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import datetime



class BaseClass():

    
    def __init__(self, test_name, login, password, address_to, log_file):
        self.log_file = log_file
        self.login = login
        self.password = password
        self.address_to = address_to
        self.test_name = test_name
        logging.basicConfig(filename=self.log_file, level=logging.INFO)
        logging.info("\n%s - %s started" % (datetime.now(), self.test_name))

      
    def write_log(self,mess):
        logging.info("%s - %s %s" % (datetime.now(), self.test_name, mess))


    def take_screenshot(self):
        """Takes screenshots and stores them in C:\\Sikuli\\Scripts\\Screenshots"""
        try:
            pyautogui.screenshot('C:\\Sikuli\\Scripts\\Screenshots\\%s_%s.png' % (time.time(), self.test_name))
            logging.info("screenshot - OK")
        except:
            logging.warning("screenshot - WARN")


    def set_up(self, startpage, sleep=0):
        try:
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(15)
            self.driver.get(startpage)
            self.action = ActionChains(self.driver)
            time.sleep(sleep)
            logging.info("Set_up OK")
        except:
            logging.error("set_up ERROR") 
            raise SystemExit()


    def enter_login(self, selector, sleep=0, with_enter=False):
        try:
            self.driver.find_element_by_xpath(selector).send_keys(self.login)
            if with_enter:
                self.action.send_keys(Keys.ENTER).perform()
            time.sleep(sleep)
            logging.info("enter_login OK")
            time.sleep(sleep)
        except:
            logging.error("enter_login ERROR") 
            raise SystemExit()


    def enter_password(self, selector, sleep=0, with_enter=False):
        try:
            self.driver.find_element_by_xpath(selector).send_keys(self.password)
            if with_enter:
                self.action.send_keys(Keys.ENTER).perform()
            time.sleep(sleep)
            logging.info("enter_password OK")
        except:
            logging.error("enter_password ERROR") 
            raise SystemExit()


    def press_button(self, selector, sleep=0):
        try:
            self.driver.find_element_by_xpath(selector).click()
            time.sleep(sleep)
            logging.info("press_button OK")
        except:
            logging.error("press_button ERROR") 
            raise SystemExit()
        

    def enter_address_to(self, selector, sleep=0):
        try:
            self.driver.find_element_by_xpath(selector).send_keys(self.address_to)
            time.sleep(sleep)
            logging.info("enter_address_to OK")
        except:
            logging.error("enter_address_to ERROR") 
            raise SystemExit()


    def enter_address_to_2(self, sleep=0):
        """
        This method only for Outlook.com. Fore some
        reason driver.send_keys() doesn't work
        """
        try:
            pyautogui.typewrite(self.address_to)
            time.sleep(sleep)
            pyautogui.press('enter')
            pyautogui.press('tab')
            time.sleep(sleep)
            logging.info("enter_address_to OK")
        except:
            logging.error("enter_address_to ERROR") 
            raise SystemExit()


    def enter_subject(self, selector, sleep=0):
        try:
            self.driver.find_element_by_xpath(selector).send_keys("autotest")
            time.sleep(sleep)
            logging.info("enter_subject OK")
        except:
            logging.error("enter_subject ERROR") 
            raise SystemExit()


    def enter_mail_body(self, item, selector, sleep=0, with_tab=False):
        try:
            mail_body = self.driver.find_element_by_xpath(selector)
            if not with_tab:
                mail_body.send_keys("%s. Test message firefox" % item)
            else:
                mail_body.send_keys(Keys.TAB, "%s. Test message firefox" % (item))
            self.take_screenshot()  # screenshot
            time.sleep(sleep)
            logging.info("enter_mail_body OK")
        except:
            logging.error("enter_mail_body ERROR") 
            raise SystemExit()


    def press_ctrl_enter(self, sleep=0, enter_only=False):
        try:
            if not enter_only:
                pyautogui.hotkey("ctrl", "enter")
            else:
                pyautogui.press('enter')
            self.take_screenshot()  #  screenshot
            time.sleep(sleep)
        except:
            logging.error("press_ctrl_enter ERROR") 
            raise SystemExit()


    def tear_down(self, sleep=0):
        try:
            time.sleep(sleep)
            os.system(r"TASKKILL /IM firefox.exe /F")
            os.system(r"TASKKILL /IM geckodriver.exe /F")
            logging.info("tear_down OK")
            self.take_screenshot()  #  screenshot
        except:
            logging.error("tear_down ERROR") 
            raise SystemExit()
