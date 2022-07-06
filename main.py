from chromedriver.chrome_check import web_driver
from art import tprint

def main():
    tprint('parser', font='sub-zero')

    # количество обявлений
    x = int(input('Введите количество объявлений: '))

    # запуск веб_драйвера
    web_driver(x)


if __name__ == '__main__':
    main()
