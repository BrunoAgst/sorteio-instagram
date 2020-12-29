from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
import random
import os
from dotenv import load_dotenv
load_dotenv()

#config additional webdriver firefox
firefox_options = Options()
firefox_options.add_argument('--headless')
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('--disable-dev-shm-usage')


#setting config
driver = webdriver.Firefox(firefox_options=firefox_options, executable_path=rf'C:\tools\selenium\geckodriver')

def search_winner(url_insta):
    url = 'https://www.instagram.com'

    driver.get(url)
    sleep(5)

    username = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
    username.send_keys(os.getenv("USERNAME"))

    password = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
    password.send_keys(os.getenv("PASSWORD"))

    btn_login = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[1]/div[3]/button/div')
    btn_login.click()
    sleep(5)

    btn_info = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
    btn_info.click()
    sleep(5)

    btn_notify = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
    btn_notify.click()
    sleep(5)

    driver.get(url_insta)
    sleep(5)

    condition = True
    while condition:
        try:
            btn_comments = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/div[1]/ul/li/div/button/span')
            btn_comments.click()
            sleep(5)
        except:
            condition = False
            pass

    users = driver.find_elements_by_class_name('Mr508')
    list_users = []

    for item in users:
        user = item.find_element_by_class_name('_6lAjh ')
        if user in list_users:
            continue
        else:
            list_users.append(user.text)

    winner = random.choice(list_users)

    return winner