from tkinter import *
from googletrans import Translator

def trans():
    text = text_field1.get('1.0', END)             # переменная в которую будет записываться наше 1 текстовое поле text_field1 с 1.0 символа по END
    text_trans = translator.translate(text, dest='en' )       # переменная в которой происходит перевод
    text_field2.delete('1.0', END)              # происходит преобразование, мы удаляем все что было в поле
    text_field2.insert('1.0', text_trans.text)  # вставляем переведенный текст из 1 поля во 2


root = Tk()
root.geometry('500x350')
root.title('Translator')
root.resizable(width=False, height=False)
root['bg'] = 'black'    # фон
translator = Translator()


label = Label(root, fg='white', bg='black', font='Arial 12 bold', text='Enter the text')  # поле для ввода
label.place(relx=0.5, y=30, anchor=CENTER)

text_field1 = Text(root, width=35, height=5, font='Arial 12 bold')
text_field1.place(relx=0.5, y=100, anchor=CENTER)

btn = Button(root, width=35, text='translate...', command=trans)
btn.place(relx=0.5, y=180, anchor=CENTER)

text_field2 = Text(root, width=35, height=5, font='Arial 12 bold')
text_field2.place(relx=0.5, y=260, anchor=CENTER)


root.mainloop()