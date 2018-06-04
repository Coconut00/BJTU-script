from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

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
        name.send_keys('your student id')
        password.send_keys('password')
        submit.click()
    except TimeoutException:
        return search()

def tap_into_jiaowu():
    ShaungXueWei = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#wrap > div:nth-child(2) > div:nth-child(2) > div > div:nth-child(2) > div > div > table > tbody > tr:nth-child(2) > td:nth-child(1) > div > div > a'))
    )
    ShaungXueWei.click()
    XuanKe = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#menu-toggler'))
    )
    XuanKe.click()
    XuanKe =wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '# sidebar > div > div.nav-wrap > ul > li:nth-child(4) > a > span'))
    )
    XuanKe.click()

def main():
    search()
    tap_into_jiaowu()

if __name__ == '__main__':
    main()
