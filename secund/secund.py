from tkinter import *
from datetime import datetime

temp = 0
after_id = ""
def tick():
    global temp, after_id   # метод after = обновляет функцию каждую секунду (1000(1 секунда) если указать 10000(10 секунд)
    after_id = root.after(1000, tick)
    f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")     # форматирование видов минут и секунд
    lable1.config(text=str(f_temp))
    temp += 1

def start_tick():
    btnStart.pack_forget()      # кнопка будет скрываться после нажатия старт
    btnStop.pack()              # кнопка будет отображена
    tick()

def stop_tick():
    btnStop.pack_forget()
    btnCont.pack()
    btnReset.pack()
    root.after_cancel(after_id)

def continue_tick():
    btnCont.pack_forget()
    btnReset.pack_forget()
    btnStop.pack()
    tick()

def reset_tick():
    global temp
    temp = 0
    lable1.configure(text='00:00')
    btnCont.pack_forget()
    btnReset.pack_forget()
    btnStart.pack()

root = Tk()
root.title('Stopwatch')
root.geometry('230x200')
root.resizable(width=False, height=False)
root['bg'] = 'white'

lable1 = Label(root, width=10, font='Arial 30', text='00:00')
lable1['bg'] = 'white'
lable1.pack()


btnStart = Button(root, font='Arial 15', text='Start', width=15, bg='#FF6200', activebackground='#FF9640', command=start_tick)
btnStop = Button(root, font='Arial 15', text='Stop', width=15, bg='#FF6200', activebackground='#FF9640', command=stop_tick)
btnCont = Button(root, font='Arial 15', text='Continue', width=15, bg='#FF6200', activebackground='#FF9640', command=continue_tick)
btnReset = Button(root, font='Arial 15', text='Reset', width=15, bg='#FF6200', activebackground='#FF9640', command=reset_tick)
btnStart.pack()


root.mainloop()