import time

from create_db import add_date_sql
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By


def web_driver(x):
    options = webdriver.ChromeOptions()
    # headless
    options.headless = True

    # Подключение веб-драйвера
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\Виктор\Desktop\файлы Артема\evangelion\check_website\chromedriver\chromedriver.exe",
        options=options
    )
    url = 'https://www.avito.ru/rossiya/velosipedy?cd=1'

    try:
        # подключение к сайту
        driver.get(url)
        time.sleep(2)

        # сортировка по дате
        select_elm = driver.find_element(
            By.XPATH,
            '//div[@class="select-select-box-jJiQW select-size-s-VX5kS"]/select[@class="select-select-IdfiC"]'
        )
        select_obj = Select(select_elm)
        select_obj.select_by_index(3)
        time.sleep(1)

        # поиск div на который нужно нажать
        a_name = driver.find_elements(By.CLASS_NAME, 'iva-item-titleStep-pdebR')

        i = 0
        for item in a_name:
            i = i + 1

            item.click()
            driver.switch_to.window(driver.window_handles[1])

            # сбор информации(название, описание, состояние)
            name = driver.find_element(By.CLASS_NAME, 'title-info-title-text')
            text = driver.find_element(
                By.XPATH,
                '//div[@class="style-item-description-1e2Yo"]/div[@itemprop="description"]'
            )
            data = driver.find_element(By.CLASS_NAME, 'params-paramsList__item-1Xeok')
            id_avito = driver.find_element(By.XPATH, '//span[@data-marker="item-view/item-id"]')

            time.sleep(1)

            # добавление в database
            add_date_sql(id_avito.text.split('№')[1].split(',')[0], name.text, text.text, data.text)

            # закрытие окна и возвращение на прошлое
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)

            if i == x:
                break

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
