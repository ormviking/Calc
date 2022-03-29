from tkinter import *
import subprocess


def copy2clip(num):
    cmd = f'echo {str(num).strip()}|clip'
    return subprocess.check_call(cmd, shell=True)


def clicked():
    res = (int(b.get())-(int(b.get())*0.10))/110
    output = round(res, 2)

    update_output_text(output)


def update_output_text(output):
    clear_input()
    text1.insert(1.0, output)
    copy2clip(output)


def clear_input():
    text1.delete(1.0, END)


window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x150')

lbl = Label(window, text="Привет")
lbl.grid(column=0, row=0)



b = Entry(window, width=10)
b.grid(column=1, row=0)
b.focus()

btn = Button(window, text="Нажми!", command=clicked)
btn.grid(column=2, row=0)


btn = Button(window, text="Очистить!", command=clear_input)
btn.grid(column=2, row=2)

text1 = Text(window, height=1, font='Arial 14', wrap=WORD)
text1.grid(column=3, row=0)

window.mainloop()


