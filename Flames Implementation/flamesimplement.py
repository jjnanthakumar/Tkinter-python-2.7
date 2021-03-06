import tkinter as tk
from tkinter import *
from collections import Counter, OrderedDict
import copy
from tkinter import messagebox

root = tk.Tk()
s = tk.IntVar()

__author__ = "jjnanthakumar477@gmail.com"


def count(n1, n2):
    if '.' in n1 or '.' in n2:
        name1 = n1.split('.')
        name2 = n2.split('.')
    else:
        name1 = n1.split()
        name2 = n2.split()
    name1 = [i for i in name1 if len(i) > 1]
    name2 = [i for i in name2 if len(i) > 1]

    n1 = ''.join(name1)
    n2 = ''.join(name2)
    n1 = n1.lower()
    n2 = n2.lower()
    n1 = sorted(n1)
    n2 = sorted(n2)
    freq1 = dict(Counter(n1))
    freq2 = dict(Counter(n2))
    c = copy.deepcopy(freq1)
    c1 = copy.deepcopy(freq2)
    for (char, count), (char1, count1) in zip(c.items(), c1.items()):
        if len(n1) > len(n2):
            if char1 in c.keys():
                freq1[char1] = abs(c1[char1] - c[char1])
                freq2[char1] = 0
            else:
                freq2[char1] = 1
        else:
            if char in c1.keys():
                freq1[char] = abs(c1[char] - c[char])
                freq2[char] = 0
            else:
                freq1[char] = 1
    res = sum(freq2.values()) + sum(freq1.values())
    return res


def flames():
    name1 = str(v1.get())
    name2 = str(v2.get())
    # print name2, name1
    if name1 == '' or name2 == '' or not name1.isalpha() or len(name1) < 1 or len(name2) < 1 or not name2.isalpha():
        messagebox.showerror("Error", message="Invalid Names :(")
        return
    n1 = name1
    n2 = name2

    c = count(n1, n2)
    dic = OrderedDict({'F': "Friends", 'L': "Love", 'A': "Affection", 'M': "Marriage", 'E': "Enemy", 'S': "Sister"})
    lst = ['F', 'L', 'A', 'M', 'E', 'S']
    for i in range(6, 0, -1):
        r = c % i
        if len(lst) == 1 or len(lst) == 0:
            break
        lst.pop(r - 1)
        if r - 1 > 0:
            lst = lst[r - 1:] + lst[:r - 1]

    messagebox.showinfo("Predicted Relation", "The Relation is {}".format(dic.get(''.join(lst), "Sorry")))


def clear():
    res.set('Final Result')
    v2.set('')
    v1.set('')


import os

v1 = StringVar()
v2 = StringVar()
res = StringVar()
w = root.winfo_reqwidth()
h = root.winfo_reqheight()
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
root.geometry('+%d+%d' % (x, y))
root.title("Flames Game")
root.iconbitmap(os.path.abspath('hearts.ico'))

root.configure(bg='pink')
Label(root, text="Enter Your Name: ", justify=tk.LEFT, padx=10).grid(row=1, column=0, sticky=W)
Label(root, text="Enter Another Name: ", justify=tk.LEFT, padx=10).grid(row=2, column=0, sticky=W)
Entry(root, textvariable=v1, fg='red', width=30, justify=tk.CENTER).grid(row=1, column=1, sticky=W, pady=2, padx=10,
                                                                         columnspan=10)
Entry(root, textvariable=v2, fg='red', width=30, justify=tk.CENTER).grid(row=2, column=1, sticky=W, pady=2, padx=10,
                                                                         columnspan=10)
v1.set('')
v2.set('')
Button(root, text='Check Relation', fg='blue', bg='white', command=lambda: flames()).grid(row=4, column=1, sticky=W,
                                                                                          pady=10, padx=5)
Button(root, text='Play Again', fg='blue', bg='white', command=lambda: clear()).grid(row=4, column=2, sticky=W, pady=2)
root.mainloop()
