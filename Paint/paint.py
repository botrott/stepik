from tkinter import *
from tkinter import messagebox  # messagebox необходим для того чтобы подтверждать что мы хотим выйти
import PIL
from PIL import Image, ImageDraw
from random import *

def activate_point(event):
    x1, y1 = (event.x - 2), (event. y - 2)          # толщина линии
    x2, y2 = (event.x + 2), (event.y + 2)
    cv.create_line(x1, y1, x2, y2, fill='black', width=5) # линия на холсте
    draw.line((x1, y1, x2, y2), fill='black', width=5)   # линия для сохранения

def save():
    file_name = f'image_{randint(0, 100)}.png'
    image1.save(file_name)
    messagebox.showinfo('Save', 'Save under name %s' %file_name)


root = Tk()
root.title('Paint')
root.resizable(width=False, height=False)            # чтобы нельзя было растягивать приложение


cv = Canvas(root, width=1280, height=720, bg='white')       # создаем холст на котором можно рисовать

image1 = PIL.Image.new('RGB', (1280, 720), 'white')      # место где мы будем рисовать
draw = ImageDraw.Draw(image1)                                    # инструмент для рисования

cv.bind('<B1-Motion>', activate_point)         # заменим левую клавишу мыши
cv.pack(expand=1, fill=BOTH)


btn_save = Button(text='Save', bg='black', fg='white', font=('Comic Sans MS', 30), command=save)     # кнопка Save
btn_save.pack()



root.mainloop()