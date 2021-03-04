import csv
import numpy as np
import pandas as pd
from tkinter import *
import tkinter as tk
from tkinter import ttk
import math
import sys

def csv_writer():
    read_a = pd.read_csv('first.csv', sep=";", header=None)
    read_b = pd.read_csv('second.csv', sep=";", header=None)
    m = spin0.get()
    k = spin1.get()
    n = spin2.get()
    m = int(m)
    k = int(k)
    n = int(n)
    g = 0
    obj = open('output.csv', 'w')
    for j in range(n):
        for i in range(m):
            for l in range(k):
                g += np.dot(read_a[i][l], read_b[l][j])
            obj.write(str(g) + ' ;')
            g = 0
        obj.write('\n')
    obj.close()

window = Tk()
window.title("Матрицы для детей")
window.geometry('400x250')

spin0 = Spinbox(window, from_=0, to=9, width=5)
spin0.grid(column=0, padx=180, pady=20, row=0)

spin1 = Spinbox(window, from_=0, to=9, width=5)
spin1.grid(column=0, pady=20, row=1)

spin2 = Spinbox(window, from_=0, to=9, width=5)
spin2.grid(column=0, pady=20, row=2)

btn = Button(window, text='Считаем', command=csv_writer)
btn.grid(column=0, row=3)

window.mainloop()



