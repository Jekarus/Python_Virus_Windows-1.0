# Вирус много рандомных окон 1.0

from tkinter import *
import random
import time


def about():
    i = 0
    otherFrame = []  # общий список пустой
    while True:
        w = random.randint(1, 1920)  # рандомные координаты ширины
        h = random.randint(1, 1080)  # рандомные координаты высоты
        a = Toplevel()  # присваивание окну TopLEvel переменной
        a.geometry('650x250+{}+{}'.format(w, h))  # форомат нового окошка + координаты появления
        otherFrame.append(a)
        i += 1
        if i % 1000 == 0:
            time.sleep(1) # время старта программы после нажатия кнопки
            root.update() # обновление окна


root = Tk()
root.title("Главное окно")
root.geometry('200x150+960+540') # 2 последние цифры координаты появления окна
about()


root.mainloop()