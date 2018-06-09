from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import logging

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome()

# client = pymongo.MongoClient('localhost',27017)
# mis = client['mis']
# schedule = mis['schedule']


wait = WebDriverWait(driver,10)
url = 'https://mis.bjtu.edu.cn/home/'
URL = 'http://jwc.bjtu.edu.cn'

user_id_str = ''
password_str = ''
xpath_str = ''
delta = 0.9

def search():
    try:
        driver.get('https://mis.bjtu.edu.cn/home/')
        name = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#id_loginname'))
        )
        password = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#id_password'))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#form1 > div > div > button'))
        )
        name.send_keys(user_id_str)
        password.send_keys(password_str)
        submit.click()
    except TimeoutException:
        return search()


def tap_into_jiaowu():
    driver.maximize_window()
    ShaungXueWei = driver.find_element_by_css_selector(
                                    '#wrap > div:nth-child(2) > div:nth-child(2) > div > div:nth-child(2) > div > div > table > tbody > tr:nth-child(2) > td:nth-child(1) > div > div > a')

    ShaungXueWei.click()


def solve():
    elem = driver.find_element_by_xpath(
        '//*[@id="wrap"]/div[2]/div[2]/div/div[2]/div/div/table/tbody/tr[2]/td[1]/div/div/h5/a')
    elem.click()

    handles = driver.window_handles
    driver.switch_to.window(handles[1])

    time.sleep(3)

    try:
        elem = driver.find_element_by_css_selector('#sidebar > div > div.nav-wrap > ul > li:nth-child(4) > a > span')
        elem.click()
    except:
        elem = driver.find_element_by_xpath('//*[@id="menu-toggler"]')
        print(elem.id)
        elem.click()
        print('End')

    driver.find_element_by_xpath('//*[@id="sidebar2"]/div[1]/div[1]/div/ul/li[1]/ul/li[2]/a').click()


def duoXuan(i):
    if i == 1:
        driver.find_element_by_xpath('//*[@id="current"]/table/tbody/tr[3]/td[1]/label').click()
    if i == 2:
        driver.find_element_by_xpath('//*[@id="current"]/table/tbody/tr[4]/td[1]/label').click()
    elif i == 3:
        driver.find_element_by_xpath('//*[@id="current"]/table/tbody/tr[5]/td[1]/label').click()
    elif i == 4:
        driver.find_element_by_xpath('//*[@id="current"]/table/tbody/tr[6]/td[1]/label').click()
    elif i == 5:
        driver.find_element_by_xpath('//*[@id="current"]/table/tbody/tr[2]/td[1]/label').click()
    elif i == 6:
        driver.find_element_by_xpath('//*[@id="current"]/table/tbody/tr[7]/td[1]/label').click()
    elif i == 7:
        driver.find_element_by_xpath('//*[@id="current"]/table/tbody/tr[8]/td[1]/label').click()
    else:
        driver.find_element_by_xpath('//*[@id="current"]/table/tbody/tr[9]/td[1]/label').click()
    return True


def XuanKe():
    driver.find_element_by_xpath('//*[@id="sidebar2"]/div[1]/div[1]/div/ul/li[2]/ul/li[1]/a').click()
    flag = False
    try_cnt = 1
    i = 0
    while not flag:
        try:
            flag = duoXuan(i)
        except Exception as e:
            print(i)
            print(e)
            if i == 3:
                i = 0
            i += 1
            driver.refresh()
            try_cnt += 1
            time.sleep(delta)

    driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()
    driver.find_element_by_xpath('//*[@id="select-submit-btn"]').click()
    print("OK!")
    print("You have try " + str(try_cnt) + " times.")


def main():
    search()
    tap_into_jiaowu()
    solve()
    XuanKe()


if __name__ == '__main__':
    main()
    
