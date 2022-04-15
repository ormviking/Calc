from tkinter import *
import subprocess


def copy2clip(num):
    cmd = f'echo {str(num).strip()}|clip'
    return subprocess.check_call(cmd, shell=True)


def clicked():
    res = (int(b.get())-(int(b.get())*prosent_input()))/kurs
    output = round(res, 2)

    update_output_text(output)


def update_output_text(output):
    clear_input()
    text1.insert(1.0, output)
    copy2clip(output)


def clear_input():
    text1.delete(1.0, END)

def prosent_input():
    prosent = float(b_2.get()) * 0.01
    return prosent

def kurs():
    kurs = float(b_3.get())
    return kurs

window = Tk()
window.title("HotKey только на английском")
window.geometry('400x150')

lbl = Label(window, text="Введи рубли")
lbl.grid(column=0, row=0)

b = Entry(window, width=10)
b.grid(column=1, row=0)
b.focus()

btn = Button(window, text="Нажми!", command=clicked)
btn.grid(column=2, row=0)


btn = Button(window, text="Очистить все!", command=clear_input)
btn.grid(column=2, row=2)

b_2 = Entry(window, width=10)
b_2.grid(column=1, row=3)

lbl_2 = Label(window, text="Введи процент")
lbl_2.grid(column=0, row=3)

btn_2 = Button(window, text="Нажми меня!", command=prosent_input)
btn_2.grid(column=2, row=3)

text1 = Text(window, height=1, font='Arial 14', wrap=WORD)
text1.grid(column=3, row=0)

b_3 = Entry(window, width=10)
b_3.grid(column=1, row=4)

lbl_3 = Label(window, text="Введи курс")
lbl_3.grid(column=0, row=4)

btn_3 = Button(window, text="Нажми меня!", command=kurs)
btn_3.grid(column=2, row=4)
window.mainloop()


