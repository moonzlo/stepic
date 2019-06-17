from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def working():

    driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
    from selenium.webdriver.support import expected_conditions as ec
    from selenium.webdriver.support.ui import WebDriverWait
    try:
        def login(url):
            try:
                def calc(x):
                    return str(math.log(abs(12 * math.sin(int(x)))))

                driver.get(url)
                button = WebDriverWait(driver, 10).until(
                    EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))
                driver.find_element_by_id('book').click()
                driver.implicitly_wait(1)
                num = driver.find_element_by_id('input_value').text
                value = calc(num)
                driver.find_element_by_xpath('//input').send_keys(value)
                driver.find_element_by_id('solve').click()
                time.sleep(10)

            except NoSuchElementException as error:
                print(f'Ошибка теста: {error}')

        test_url1 = 'http://suninjuly.github.io/explicit_wait2.html'

        login(test_url1)


    except Exception as errors:
        print(f'Ошибка в глобальном скоупе | {errors}')

    finally:
        driver.close()
        time.sleep(1)
        driver.quit()


working()

