from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

def search():
    try:
        driver.get('https://cas.bjtu.edu.cn/auth/login/?next=/o/authorize/%3Fresponse_type%3Dcode%26client_id%3DqamiHUSTlVvP6J9iMoPO7yvlb7zEU7qYRVK9P0xf%26state%3D1528084105%26redirect_uri%3Dhttps%3A//mis.bjtu.edu.cn/auth/callback/%3Fredirect_to%3D/home/')
        name = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#id_loginname'))
        )
        password = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#id_password'))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#form1 > div > div > button'))
        )
        name.send_keys('16281154')
        password.send_keys('273919')
        submit.click()
    except TimeoutException:
        return search()

def main():
    search()

if __name__ == '__main__':
    main()
