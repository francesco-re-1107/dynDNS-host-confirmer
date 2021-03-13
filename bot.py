from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import schedule
import time
import datetime
import argparse

access_url = 'https://dyndns.it/login/?redirect_to=%2Fhost-management%2F'

my_parser = argparse.ArgumentParser(description='This bot confirms dynDNS host every 15 days')

my_parser.add_argument('username',
                       metavar='username',
                       type=str,
                       help='the username of dynDNS')


my_parser.add_argument('password',
                       metavar='password',
                       type=str,
                       help='the password of dynDNS')

args = my_parser.parse_args()

username = args.username
password = args.password

if username is None or password is None:
    quit()

def job():
    print(str(datetime.datetime.now()) + " - running...")
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)

        browser.get(access_url)

        username_input = browser.find_element_by_css_selector("input[name='log']")
        password_input = browser.find_element_by_css_selector("input[name='pwd']")

        username_input.send_keys(username)
        password_input.send_keys(password)

        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        browser.execute_script("arguments[0].click();", login_button)

        time.sleep(4)

        confirm_host_button = browser.find_element_by_xpath('//*[@id="confirmHostForm"]/button')
        browser.execute_script("arguments[0].click();", confirm_host_button)

        time.sleep(4)

        browser.close()
        
    except Exception as e:
        print("error: " + str(e))

job()
schedule.every(15).days.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)