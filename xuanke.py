from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pymongo
import logging
import schedule

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


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
        name.send_keys('student-id')
        password.send_keys('password')
        submit.click()
    except TimeoutException:
        return search()


def tap_into_jiaowu():
    driver.maximize_window()
    ShaungXueWei = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#wrap > div:nth-child(2) > div:nth-child(2) > div > div:nth-child(2) > div > div > table > tbody > tr:nth-child(2) > td:nth-child(1) > div > div > a'))
    )
    ShaungXueWei.click()


def solve():
    elem = driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[2]/div/div[2]/div/div/table/tbody/tr[2]/td[1]/div/div/h5/a')
    elem.click()

    # time.sleep(2)
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    # print(driver.page_source)
    time.sleep(3)
    # driver.maximize_window()
    # elem = driver.find_element_by_xpath('//*[@id="sidebar"]/div/div[1]/ul/li[4]/a')

    try:
        elem = driver.find_element_by_css_selector('#sidebar > div > div.nav-wrap > ul > li:nth-child(4) > a > span')
        elem.click()
    except:
        elem = driver.find_element_by_xpath('//*[@id="menu-toggler"]')
        print(elem.id)
        elem.click()
        print('end')

    driver.find_element_by_xpath('//*[@id="sidebar2"]/div[1]/div[1]/div/ul/li[1]/ul/li[2]/a').click()
    # 课表
    for i in range(2, 7):
        for j in range(2, 7):
            try:
                name = '/html/body/div[2]/div[2]/div/div[2]/table/tbody/tr[' + str(j) + ']/td[' + str(i) + ']/div/span[1]'
                classnames = driver.find_element_by_xpath(name).text
                weekdays = i - 1
                times = j - 1
                if (classnames == ''):
                    pass
                else:
                    print(classnames, weekdays, times)
                    data = {
                        'classnames': classnames,
                        'weekdays': weekdays,
                        'times': times
                    }
                    schedule.insert(data)
            except:
                pass

    cnt = 0
    for i in range(2, 20):
        try:
            classname = driver.find_element_by_xpath('//*[@id="selected-container"]/table/tbody/tr[{}]/td[2]'.format(str(i))).text
            cnt = cnt + 1
        except:
            break

    print("现选中共%d门课" % cnt)


def XuanKe():
    driver.find_element_by_xpath('//*[@id="sidebar2"]/div[1]/div[1]/div/ul/li[2]/ul/li[1]/a').click()


def main():
    search()
    tap_into_jiaowu()
    solve()
    XuanKe()


if __name__ == '__main__':
    main()
