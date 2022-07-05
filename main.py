from chromedriver.chrome_check import web_driver


def main():
    # количество обявлений
    x = int(input())

    # запуск веб_драйвера
    web_driver(x)


if __name__ == '__main__':
    main()
