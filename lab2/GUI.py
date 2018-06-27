# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import third_sem.AMO.lab2.select_sort as my_alg
from tkinter import *
from random import randint
from time import clock


def show_plot_1000(max_len=10000, step=1000):
    """Shows real and teor computational complexity."""
    slave = Toplevel(root)
    slave.title('Graphs of real and teor computational complexity')
    my_time = my_alg.count_sort_time(max_len, step)
    x1 = list(my_time.keys())
    y1 = list(map(lambda key: my_time[key], x1))

    teor_time = list(map(lambda x: x ** 2, list(range(0, max_len+1, step))))

    f = Figure(figsize=(6, 6), dpi=100)
    a = f.add_subplot(211)
    a.set_title('Real computational complexity', fontsize=14)
    a.plot(x1, y1, 'b')
    a.autoscale(enable=True, axis=u'both', tight=False)
    a.set_xlabel('Number of elements', fontsize=11)
    a.set_ylabel('Sorting time, s', fontsize=11)

    b = f.add_subplot(212)
    b.set_title('Theoretical graph', fontsize=14)
    b.plot(x1, teor_time, 'r')
    b.autoscale(enable=True, axis=u'both', tight=False)

    f.tight_layout()

    canvas = FigureCanvasTkAgg(f, slave)
    canvas.show()
    canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)


def random_arr(length):
    """Generate arr with random inetegers and with a long 'length'"""
    _arr = []
    for i in range(length):
        _arr.append(randint(-1000, 1000))
    return _arr


def but_random():
    """Insert random_arr into ent_arr"""
    length = ent_arr.get()
    if check_input(length) == 'error': return

    _arr = random_arr(int(length))
    ent_arr.delete(0, END)
    ent_arr.insert(0, _arr)


def check_input(arr):
    """Check string 'arr' for input errors"""
    global l1
    if arr == '':
        try:
            l1.destroy()
        except NameError:
            pass
        finally:
            l1 = Label(root, text='First input something, then press "Result" or "Random"!', font='Calibri 13 bold', fg='red', bg=main_bg)
            l1.grid(column=0, row=5, columnspan=5, pady=10)
        return 'error'
    elif arr.isalpha():
        try:
            l1.destroy()
        except NameError:
            pass
        finally:
            l1 = Label(root, text='Check your input. There are non-numeric symbols.', fg='red', bg=main_bg)
            l1.grid(column=0, row=5, columnspan=5, pady=10)
        return 'error'
    else:
        try:
            l1.destroy()
        except NameError:
            pass
        return 'OK'


def but_result():
    global l1
    arr = ent_arr.get()

    if check_input(arr) == 'error': return

    for i in [',', '\n', '\t', '\r']:
        arr.replace(i, ' ')
    arr = arr.split(' ')

    for i in range(arr.count('')):
        try:
            arr.remove('')
        except: pass

    for i in range(len(arr)):
        arr[i] = int(arr[i])

    t1 = clock()
    sorted_arr = my_alg.select_sort_min(arr)
    t2 = clock()

    for i in range(len(sorted_arr)):
        sorted_arr[i] = str(sorted_arr[i])

    if len(sorted_arr) > 15:
        with open(r'D:\Python\Brovchenko_projects\third_sem\AMO\lab2\res.txt', 'w') as fs:
            fs.writelines(' '.join(sorted_arr))
            fs.close()

        Button(root, text='Show sorted', command=show_from_file, bg=but_bg, font=but_font).grid(column=0, row=9, columnspan=5)
    else:
        ent_arr.delete(0, END)
        ent_arr.insert(0, ' '.join(sorted_arr))

    Label(root, text='Sorting time: {}'.format(t2-t1), bg=main_bg, font='Calibri 14').grid(column=0, row=7, columnspan=5)


def clear_entry():
    ent_arr.delete(0, END)


def open_file():
    """Arr from file"""
    with open(r'D:\Python\Brovchenko_projects\third_sem\AMO\lab2\f.txt', 'r') as f:
        _text = f.read().split(' ')
        f.close()

    for i in range(_text.count('')):
        try:
            _text.remove('')
        except: pass

    for i in range(len(_text)):
        _text[i] = int(_text[i])

    ent_arr.delete(0, END)
    ent_arr.insert(0, _text)


def show_from_file(file=r'D:\Python\Brovchenko_projects\third_sem\AMO\lab2\res.txt'):
    """Shows the contents of a file"""
    with open(r'{}'.format(file), 'r') as fs:
        arr = fs.read()
        fs.close()
    slave = Toplevel()
    slave.title('Sorted array')
    slave.resizable(width=FALSE, height=FALSE)
    T = Text(slave, height=10, width=60)
    T.pack()
    T.insert(END, arr)


if __name__ == '__main__':
    root = Tk()
    root.title('Select sort')
    root.resizable(width=False, height=False)
    main_bg = 'yellow'
    but_bg = 'chartreuse'
    but_font = 'Calibri 13 bold'

    root['bg'] = main_bg

    Label(root, text='Input here your array', font='Calibri 16 bold', bg=main_bg)\
        .grid(column=0, row=0, columnspan=5, pady=10)
    Label(root, text='*if you want to generate an array randomly, input length', font='Calibri 14', bg=main_bg)\
        .grid(column=0, row=1, columnspan=5, pady=5)
    ent_arr = Entry(root, font='Calibri 14', width=50, bd=0)
    ent_arr.grid(column=0, row=2, columnspan=5, padx=5)

    Button(root, text='Random', command=but_random, font=but_font, bg=but_bg).grid(column=0, row=3, pady=10)
    Button(root, text='From file', command=open_file, font=but_font, bg=but_bg).grid(column=3, row=3, columnspan=2)

    Button(root, text='Result', command=but_result, font=but_font, bg=but_bg).grid(column=0, row=4, pady=10)
    Button(root, text='Show graphics', command=show_plot_1000, font=but_font, bg=but_bg).grid(column=3, row=4, columnspan=2)

    Button(root, text='Clear', command=clear_entry, font='Calibri 13 bold', bg='indianred', relief=GROOVE).grid(column=0, row=3, columnspan=5)
    root.mainloop()
