# stone, scissors, paper
from tkinter import *
from random import *

root = Tk()    # создаем обьект класса Тк
root.title('Stone scissors paper')
root.geometry('620x410')    # разрешение окна
root.resizable(width=False, height=False)   # отменяет изменение окна
root['bg'] = 'black'    # фон окна


def Whyssp():
    ssp = ['Stone', 'Scissors', 'Paper']
    value = choice(ssp)
    lableText.configure(text=value)


lableText = Label(root, text='', fg='white', font=('Comic Sans MS', 20), bg='black')
lableText.place(y = 200, x = 240)
lableText.pack()

img = PhotoImage(file='q2.png')
l_log = Label(root, image=img)
l_log.pack()

scissors = Button(root,            # создаем первую кнопку "камень"
               text='Scissors',
               font=('Comic Sans MS', 20),
               bg='white',
               command=Whyssp,
               activebackground = '#FFB673'

               )
scissors.place(x=65, y=365)

stone = Button(root,            # создаем 2 кнопку
               text='Stone',
               font=('Comic Sans MS', 20),
               bg='white',
               command=Whyssp,
               activebackground = '#FFB673'

               )
stone.place(x=250, y=310)


paper = Button(root,            # создаем 3 кнопку
               text='Paper',
               font=('Comic Sans MS', 20),
               bg='white',
               command=Whyssp,
               activebackground = '#FFB673'
               )
paper.place(x=430, y=350)

root.mainloop()