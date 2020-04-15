from time import sleep
from selenium import webdriver

access_url = 'https://dyndns.it/login/?redirect_to=%2Fhost-management%2F'

username = "<username>"
password = "<password>"


try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get(access_url)

    username_input = browser.find_element_by_css_selector("input[name='log']")
    password_input = browser.find_element_by_css_selector("input[name='pwd']")

    username_input.send_keys(username)
    password_input.send_keys(password)

    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()

    sleep(4)

    confirm_host_button = browser.find_element_by_xpath('//*[@id="confirmHostForm"]/button')
    browser.execute_script("arguments[0].click();", confirm_host_button)

    sleep(4)

    browser.close()
    
except Exception as e:
    print(f"error: {str(e)}")
finally:
    browser.close()
