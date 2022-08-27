from tkinter import *

root = Tk()
root.title('Click counter')
root.geometry('200x200')
root.resizable(width=False, height=False)
root.config(bg='#e8e8e8')

img = PhotoImage(file='w2.png')
llog = Label(root, image=img)
llog.config(bg='#e8e8e8')
llog.place(x=50, y=70)


count = 0   # переменная для кликов, изначально равна 0

def cliked():   # функция для кликера
    global count
    count += 1
    Click.configure(text=count)     # текст меняется на "счетчик"


Click = Label(root, text='0', font='Arial 25')  # начальный текст '0'
Click.config(bg='#e8e8e8')
Click.pack()    # вывод лейбла клик


btn = Button(root, text='Click me', padx='20', pady='18', command=cliked)   # кнопка, ее текст, задаем х и у, command = подключает кликер
btn.config(bg='#e8e8e8')
btn.pack()

root.mainloop()