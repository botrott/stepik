from tkinter import *
from tkinter import messagebox
from random import *

clicks = 0

def randoms():
    global clicks
    btnclick.place(x=randint(70, 500), y=randint(70, 550))
    clicks += 1
    labelclick['text'] = str(clicks)
    labelclick.pack()

root = Tk()
root.title('Clicker')
root.geometry('600x600')
root.resizable(width=False, height=False)
root['bg'] = 'black'

labelclick = Label(root, text='0', font=('Arial', '20', 'bold'), bg='black', fg='white')
labelclick.pack()

btnclick = Button(root,
                  text='Click',
                  bg='lime',
                  fg='black',
                  padx='20',
                  pady='8',
                  font=('Comic Sans MS', 13, 'bold'),
                  command=randoms
                  )
btnclick.place(x=randint(70, 500), y=randint(70, 550))






root.mainloop()