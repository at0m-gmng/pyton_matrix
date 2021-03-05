import csv
import numpy as np
import pandas as pd
from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as mb
import math

### матрицы
class Matrix:
    def martix_multiply(self):
        m = int(app.spin0.get())
        k = int(app.spin1.get())
        n = int(app.spin2.get())
        #m = int(m)
        #k = int(k)
        #n = int(n)
        g = 0
        obj = open('output.csv', 'w')
        for j in range(n):
            for i in range(m):
                for l in range(k):
                    g += read_a[i][l]*read_b[l][j]
                obj.write(str(g) + ' ;')
                # сделать проверку g, если не пустое, то назначить ключ
                # который будет считываться в мессендж боксе и
                # в соответствии с ключём выводить сообщение о матрице
                g = 0
            obj.write('\n')
        """
        if obj is None:
            b = None
            mess(b)
            #print(mess(b))
        else:
            b = 1
            mess(b)
            #print(mess(b))
        """
        obj.close()

    def vector(self):
        m = int(app.spin0.get())
        k = int(app.spin1.get())
        n = int(app.spin2.get())
        g = 0
        obj = open('output.csv', 'w')
        for j in range(n):
            for i in range(m):
                for l in range(k):
                    g = read_a[l]*read_b[l][j]
                obj.write(str(g) + ' ;')
                g = 0
            obj.write('\n')
        obj.close()

    def summ(self):
        m = int(app.spin0.get())
        k = int(app.spin1.get())
        n = int(app.spin2.get())
        g = 0
        obj = open('output.csv', 'w')
        for j in range(n):
            for i in range(m):
                for l in range(k):
                    g = read_a[i][j]+read_b[i][j]
                obj.write(str(g) + ' ;')
                g = 0
            obj.write('\n')
        obj.close()

    def on_scal(self):
        m = int(app.spin0.get())
        k = int(app.spin1.get())
        n = int(app.spin2.get())
        g = 0
        obj = open('output.csv', 'w')
        for j in range(n):
            for i in range(m):
                for l in range(k):
                    g = read_a[i][j]*5
                obj.write(str(g) + ' ;')
                g = 0
            obj.write('\n')
        obj.close()

    def multiply(self):
        m = int(app.spin0.get())
        k = int(app.spin1.get())
        n = int(app.spin2.get())
        g = 0
        obj = open('output.csv', 'w')
        for j in range(n):
            for i in range(m):
                for l in range(k):
                    g = read_a[i][j]*read_b[i][j]
                obj.write(str(g) + ' ;')
                g = 0
            obj.write('\n')
        obj.close()

    def opredelitel(self):
        m = int(app.spin0.get())
        k = int(app.spin1.get())
        n = int(app.spin2.get())
        g = 0
        obj = open('output.csv', 'w')
        for j in range(n):
            for i in range(m):
                for l in range(k):
                    g = read_a[i][j]
                if i == (m-1):
                    obj.write(str(g))
                else:
                    obj.write(str(g) + ' ;')
                g = 0
            obj.write('\n')
        obj.close()
        read_b = pd.read_csv('output.csv', sep=";", header=None).to_numpy()
        obj = open('output.csv', 'a')
        g = np.linalg.det(read_b)
        obj.write(str(g))
        obj.close()

    def inv_matrix(self):
        m = int(app.spin0.get())
        k = int(app.spin1.get())
        n = int(app.spin2.get())
        g = 0
        obj = open('output.csv', 'w')
        for j in range(n):
            for i in range(m):
                for l in range(k):
                    g = read_a[i][j]
                if i == (m - 1):
                    obj.write(str(g))
                else:
                    obj.write(str(g) + ' ;')
                g = 0
            obj.write('\n')
        obj.close()
        read_b = pd.read_csv('output.csv', sep=";", header=None).to_numpy()
        obj = open('output.csv', 'a')
        g = np.linalg.inv(read_b)
        obj.write(str(g))
        obj.close()

    def transposition(self):
        m = int(app.spin0.get())
        k = int(app.spin1.get())
        n = int(app.spin2.get())
        g = 0
        obj = open('output.csv', 'w')
        for j in range(n):
            for i in range(m):
                for l in range(k):
                    g = read_a[j][i]
                obj.write(str(g) + ' ;')
                g = 0
            obj.write('\n')
        obj.close()

### вектора
class Vector:
    def vector_on_scal(self):
        m = 3
        k = 1
        n = 1
        g = 0
        obj = open('output.csv', 'w')
        for i in range(n):
            for j in range(m):
                for l in range(k):
                    g = read_a[i][j]*5
                obj.write(str(g))
                g = 0
                obj.write('\n')
        obj.close()

    def summ_vector(self):
        m = 3
        k = 1
        n = 1
        g = 0
        obj = open('output.csv', 'w')
        for i in range(n):
            for j in range(m):
                for l in range(k):
                    g = read_a[i][j]+read_a[i][j]
                obj.write(str(g))
                g = 0
                obj.write('\n')
        obj.close()

    def mul_vector(self):
        m = 3
        k = 1
        n = 1
        g = 0
        obj = open('output.csv', 'w')
        for i in range(n):
            for j in range(m):
                for l in range(k):
                    g = read_a[i][j]*read_a[i][j]
                obj.write(str(g))
                g = 0
                obj.write('\n')
        obj.close()

    def scal_mul(self):
        m = 3
        k = 1
        n = 1
        g = 0
        obj = open('output.csv', 'w')
        for i in range(n):
            for j in range(m):
                for l in range(k):
                    g += read_a[i][j]*read_a[i][j]
                obj.write(str(g))
                g = 0
                obj.write('\n')
        obj.close()

    def mull_vect(self):
        # считывает в качестве исходных данных
        # первые 3 координаты из каждого файла
        m = 3
        k = 1
        n = 1
        g = 0
        obj = open('output.csv', 'w')
        for i in range(n):
            for j in range(m):
                for l in range(k):
                    g = read_a[i][j]
                obj.write(str(g))
                g = 0
                obj.write('\n')
        obj.close()
        read_new_a = pd.read_csv('output.csv', sep=";", header=None).to_numpy()

        obj = open('output.csv', 'w')
        for i in range(n):
            for j in range(m):
                for l in range(k):
                    g = read_b[i][j]
                obj.write(str(g))
                g = 0
                obj.write('\n')
        obj.close()
        read_new_b = pd.read_csv('output.csv', sep=";", header=None).to_numpy()
        #print(read_new_a)
        #print(read_new_b)
        #print(np.cross(read_new_a, read_new_b, axis=0))

        obj = open('output.csv', 'w')
        for l in range(k):
            g = np.cross(read_new_a, read_new_b, axis=0)
            obj.write(str(g))
            g = 0
            obj.write('\n')
        obj.close()

    def length_vect(self):
        m = 3
        k = 1
        n = 1
        g = 0
        obj = open('output.csv', 'w')
        for i in range(n):
            for j in range(m):
                for l in range(k):
                    g = read_a[i][j]
                obj.write(str(g))
                g = 0
                obj.write('\n')
        obj.close()
        read_out = pd.read_csv('output.csv', sep=";", header=None)
        print(read_out)

        obj = open('output.csv', 'a')
        for i in range(n):
            for j in range(m):
                for l in range(k):
                    g += read_out[i][j]**2
                obj.write(str(g))
        obj.write('\n')
        obj.write(str(math.sqrt(g)))
        obj.close()

### скаляры
class Scal:

    functions = {
        "sin": math.sin,
        "cos": math.cos,
        "n!": math.factorial,
        "√2": math.sqrt
    }

    # логика калькулятора
    def calc(key, text):
        if key == "=":
            # исчисления
            result = eval(text)
            return text + "=" + str(result)

        # очищение поля ввода
        elif key == "C":
            return ""

        elif key == "±":
            if "=" in text:
                return ""
            try:
                if text[0] == "-":
                    return text[1:]
                else:
                    return "-" + text
            except IndexError:
                pass

        elif key == "π":
            return text + str(math.pi)

        elif key == "xⁿ":
            return text + "**"

        elif key in Scal.functions:
            return text + "=" + str(Scal.functions[key](int(text)))

        # elif key in {"(", ")"}:  # Будет обработано в else
        #     return text + key

        else:
            if "=" in text:
                text = ""
            return text + key

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Матрицы для детей")
        self.geometry('745x250')

        #объявление вкладок
        tab_control = ttk.Notebook(self)
        tab1 = ttk.Frame(tab_control)
        tab2 = ttk.Frame(tab_control)
        tab3 = ttk.Frame(tab_control)

        tab_control.add(tab1, text='Матрицы')
        tab_control.add(tab2, text='Вектора')
        tab_control.add(tab3, text='Скаляры')
        tab_control.pack(expand=1, fill='both')

        # поля для размерности матриц
        self.spin0 = Spinbox(tab1, from_=0, to=9, width=5)
        self.spin0.grid(column=0, padx=25, row=0)

        self.spin1 = Spinbox(tab1, from_=0, to=9, width=5)
        self.spin1.grid(column=1, padx=50, row=0)

        self.spin2 = Spinbox(tab1, from_=0, to=9, width=5)
        self.spin2.grid(column=2, padx=70, row=0)

        ### кнопки матриц
        btn = Button(tab1, text='Матричное произведение', width=25, command=Matrix().martix_multiply)
        btn.grid(row=2, column=0, padx=0, pady=5)

        btn = Button(tab1,  text='Сложение', width=25, command=Matrix().summ)
        btn.grid(row=2, column=1, padx=0, pady=5)

        btn = Button(tab1,  text='Матрица на скаляр', width=25, command=Matrix().on_scal)
        btn.grid(row=2, column=2, padx=0, pady=5)

        btn = Button(tab1,  text='Вектор на матрицу', width=25, command=Matrix().vector)
        btn.grid(row=2, column=3, padx=0, pady=5)

        btn = Button(tab1, text='Поэлементное произведение', width=25, command=Matrix().multiply)
        btn.grid(row=3, column=0, padx=0, pady=5)

        btn = Button(tab1,  text='След и определитель', width=25, command=Matrix().opredelitel)
        btn.grid(row=3, column=1, padx=0, pady=5)

        btn = Button(tab1,  text='Обратная матрица', width=25, command=Matrix().inv_matrix)
        btn.grid(row=3, column=2, padx=0, pady=5)

        btn = Button(tab1,  text='Транспонирование', width=25, command=Matrix().transposition)
        btn.grid(row=3, column=3, padx=0, pady=5)

        ### кнопки векторов
        btn = Button(tab2, text='Вектор на скаляр', width=25, command=Vector().vector_on_scal)
        btn.grid(row=2, column=0, padx=0, pady=5)

        btn = Button(tab2,  text='Поэлементное Сложение', width=25, command=Vector().summ_vector)
        btn.grid(row=2, column=1, padx=0, pady=5)

        btn = Button(tab2,  text='Поэлементное Умножение', width=25, command=Vector().mul_vector)
        btn.grid(row=2, column=2, padx=0, pady=5)

        btn = Button(tab2,  text='Вектор на матрицу', width=25, command=Matrix().vector)
        btn.grid(row=2, column=3, padx=0, pady=5)

        btn = Button(tab2, text='Скалярное произведение', width=25, command=Vector().scal_mul)
        btn.grid(row=3, column=0, padx=0, pady=5)

        btn = Button(tab2,  text='Векторное произведение', width=25, command=Vector().mull_vect)
        btn.grid(row=3, column=1, padx=0, pady=5)

        btn = Button(tab2,  text='Длина вектора', width=25, command=Vector().length_vect)
        btn.grid(row=3, column=2, padx=0, pady=5)

        btn = Button(tab2,  text='Проверка сонаправленности', width=25, command=0)
        btn.grid(row=3, column=3, padx=0, pady=5)

        btn = Button(tab2,  text='Проверка на ортогональность', width=25, command=0)
        btn.grid(row=4, column=0, padx=0, pady=5)

        ### кнопки калькулятора
        bttn_list = [
            "7", "8", "9", "C", "±",
            "4", "5", "6", "/", "-",
            "1", "2", "3", "*", "+",
            "0", ".", "=", "(", ")",
            "n!", "√2", "xⁿ", "π",
            "sin", "cos"]
        r = 1
        c = 0
        for i in bttn_list:
            rel = ""
            def command(key=i):
                try:
                    result = Scal.calc(key, calc_entry.get())
                except Exception as ex:
                    mb.showerror("Error!", "Check the correctness of data")
                    raise
                else:
                    calc_entry.delete(0, tk.END)
                    calc_entry.insert(0, result)

            ttk.Button(tab3, text=i, command=command, width=10).grid(row=r, column=c)
            c += 1
            if c > 4:
                c = 0
                r += 1

        calc_entry = Entry(tab3, width=33)
        calc_entry.grid(row=0, column=0, columnspan=5)

if __name__ == "__main__":
    read_a = pd.read_csv('first.csv', sep=";", header=None)
    read_b = pd.read_csv('second.csv', sep=";", header=None)
    app = App()
    app.mainloop()



