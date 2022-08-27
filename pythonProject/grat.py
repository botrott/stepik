# from tkinter import *
#
# root = Tk()
# root.title('Тестовое приложение')
# root.geometry('600x600')    # разрешение
# root.resizable(width=False, height=False)   # изменяемый размер, ширина, высота
# #root.iconbitmap('smile.ico')
#
# #root.config(bg= 'black')   # фон способ 1
# root['bg'] = 'green'        # фон способ 2
#
#
# def click():
#     print('Hello!')
#
# btn = Button(root, text = 'Кнопка',     # кнопка
#                    command = click,     # если поставить скобки после click, то кнопка не зациклится
#                    font=("Comic Sans MS", 20, 'bold'),  # шрифт кортежем задается, когда название состоит из нескольк. слов
#                    # font = 'Arial 20',    # шрифт Ариал, размер 20 пикселей
#                    # width = 10,           # ширина кнопки
#                    # height = 10          # высота кнопки
#                    bg = 'orange',          # цвет кнопки
#                    activebackground = 'red',  # при нажатии она станет красной
#                    activeforeground = 'yellow',  # при нажатии текст станет желтым
#                    fg = 'blue'                   # текст синий
#              )
# btn.pack()
#
# label = Label(root,
#                    text = 'Text',     # text
#                    font=("Arial", 20, 'italic'),  # шрифт кортежем задается, когда название состоит из нескольк. слов
#                    bg = 'lime',          # цвет кнопки
#                    fg = 'black'                   #
#              )
# label.pack()
#
# img = PhotoImage(file='q1.png')
# l_logo = Label(root, image=img)
# l_logo.pack()
#
# root.mainloop()     # цикл который отслеживает события происходящие в нем(клик на кнопку)


# lesson Entry.
# from tkinter import *
#
# root = Tk()
# root.title('Text')
# root.geometry('600x600')
# root.resizable(width=False, height=False)
#
# # root.config(bg = 'black')
# root ['bg'] = 'black'
#
# def add():
#     e.insert(END, 'Hello')
#
# def dele():
#     e.delete(0, END)
#
# def get():
#     label1['text'] = e.get()
#
#
# e = Entry(root, show='*')     # текстовое поле для ввода
# e.pack()            # show = позовляет изменить формат, поставляемых символов
#
# # e.insert(0, 'Hello')      # задается надпись в текстовом поле, 0 это индекс, откуда старт
# # e.insert(END, ' word!')     # 5 это индекс первого слова (hello) либо можно использовать константу 'END'
#
# btn1 = Button(root, font='Arial 15', text='insert', command=add)    # кнопка 1
# btn1.pack()
#
# btn2 = Button(root, font='Arial 15', text='delete', command=dele)    # кнопка 1
# btn2.pack()
#
# btn3 = Button(root, font='Arial 15', text='get', command=get)    # кнопка 1
# btn3.pack()
#
# label1 = Label(root, bg='black', fg='white')    # fg= цвет текста
# label1.pack()
#
# root.mainloop()


# метод pack
# from tkinter import *
#
# root = Tk()
# root.title('Text')
# root.geometry('600x600')
# root.resizable(width=False, height=False)
#
# root['bg'] = 'black'

# РАЗБОР МЕТОДА SIDE (TOP, BOTTOM, LEFT, RIGHT)
# l1 = Label(root, text='1', font='15', fg='white', bg='yellow', width='8', height='4').pack(side=LEFT)    # по умолчанию side = TOP, т.е расположен сверху по середине, но если изменить на BOTTOM
# l2 = Label(root, text='2', font='15', fg='white', bg='brown', width='8', height='4').pack(side=RIGHT)
# l3 = Label(root, text='3', font='15', fg='white', bg='blue', width='8', height='4').pack(side=TOP)
# l4 = Label(root, text='4', font='15', fg='white', bg='pink', width='8', height='4').pack(side=BOTTOM)

# РАЗБОР МЕТОДА EXPAND
# l1 = Label(root, text='1', font='15', fg='white', bg='yellow', width='8', height='4').pack(expand=1, fill=BOTH)    # по умолчанию 0, fill = позволяет растянуть лейбл, по Х(горизонт) и У(верт), константа BOTH растянет на все окно


# ПАРАМЕТР ANCHOR
# l1 = Label(root, text='1', font='15', fg='white', bg='yellow', width='8', height='4').pack(expand=1, anchor=W)     # выставляет значения по компасу S(юг), W(запад)
#
# root.mainloop()



# разбор метода PLACE

# from tkinter import *
#
# root = Tk()
# root.title('Text')
# root.geometry('500x500')
# root.resizable(width=False, height=False)
#
# root['bg'] = 'black'
#
# l1 = Label(root, text='Hello', fg='white', bg='brown', padx=20, pady=20)
# # l1.place(x=100, y=100)    # отступы по х и у
# l1.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.5, relheight=0.5)    # отступы будут по 50%,
#
# root.mainloop()




# виджет TOPLEVEL (урок 7)
# from tkinter import *
#
# root = Tk()
# root.title('Test')
# root.geometry('500x500')
#
# def open_win():
#     win = Toplevel()           # toplevel это виджет, который позволяет открывать дочерние окна
#     win.geometry('200x200+300+300')  # параметры +300 задают появление на Х и У
#     win.grab_set()     # не дает повторно открыть окно win
#     l = Label(win, text='Toplevel', font='Arial 15 bold', fg='brown').pack()  # pack означает вывод
#     win.overrideredirect(1)     # окно закрепляется(нет возможности закрыть, свернуть
#     win.after(2000, lambda: win.destroy())  # через какое время закроется окно (2000 = 2 сек.)
#
# btn = Button(root, font='Arial 15', text='Open', padx=40, pady=5, command=open_win).place(relx=0.5, rely=0.5, anchor=CENTER)     # выводим кнопку на центр
#
# root.mainloop()



# ttk (урок 8)
# from tkinter import *
# from tkinter import ttk
#
# root = Tk()
# root.title('Testing')
# root.geometry('600x600')
#
# s = ttk.Style()         # обьект класса стайл, чтобы посмотреть какие есть темы
# print(s.theme_names(), s.theme_use('clam')) # theme_name - указывает на темы которые доступны, use - на текущую, чтобы поменять вводим в ("") нужную тему
# # s.configure('.', foreground='yellow')               # метод для использование стилей (название стиля, опции), '.'(будет применяться ко всем элементам)
# # s.configure('TButton', foreground='yellow')        # для изменения стиля чего то конкретного добавляетяс Т
# s.configure('one.TButton', foreground='yellow', padding=20)     # padding высота(кнопки)
#
# Button(root, text='One', padx=10).pack()
# ttk.Button(root, text='Two', width=20).pack()         # "padx" нельзя использовать в ttk
# ttk.Button(root, text='Three', width=20, style='one.TButton').pack()     # указываем к конкретной кнопки применение ттк
#
# Entry(root).pack()
# ttk.Entry(root).pack()
#
# root.mainloop()



# рисование в tkinter (урок 9)




