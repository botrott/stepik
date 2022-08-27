from tkinter import *
from tkinter import messagebox      # messagebox необходим для того чтобы подтверждать что мы хотим выйти
from tkinter import filedialog

def chenge_theme(theme):
    text_fild['bg'] = view_colors[theme]['text_bg']
    text_fild['fg'] = view_colors[theme]['text_fg']
    text_fild['insertbackground'] = view_colors[theme]['cursor']
    text_fild['selectbackground'] = view_colors[theme]['select_bg']


def chenge_fonts(ftn):
    text_fild['font'] = fonts[ftn]['font']


def note_exit():
    answer = messagebox.askokcancel('Exit', 'Are you want to exit?')
    if answer:
        root.destroy()

def note_open():
    file_path = filedialog.askopenfilename(title='File selection', filetypes=(('Text documents (*.txt)', '*.txt'), ('All file', '*.*')))
    if file_path:
        text_fild.delete('1.0', END)       # открываем файл и очищается поле с 1.0(первого) символа
        text_fild.insert('1.0', open(file_path, encoding='utf-8').read())

def note_save():
    file_path = filedialog.asksaveasfilename(filetypes=(('Text documents (*.txt)', '*.txt'), ('All file', '*.*')))
    f = open(file_path, 'w', encoding='utf-8')
    text = text_fild.get('1.0', END)          # текст сохранится от 1 символа до последнего
    f.write(text)
    f.close()




root = Tk()
root.title('Note')
root.geometry('600x600')

main_menu = Menu(root)

# Файл
file_menu = Menu(main_menu, tearoff=0)  # tearoff = убирает, "подменю файла"
file_menu.add_command(label='Open', command=note_open)
file_menu.add_command(label='Save', command=note_save)
file_menu.add_separator()       # разделить после "сохранить"
file_menu.add_command(label='Close', command=note_exit)  # кнопка выход
root.config(menu=file_menu)

# Вид
view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)
# темы черная и белая
view_menu_sub.add_command(label='Black theme', command=lambda: chenge_theme('dark'))
view_menu_sub.add_command(label='Light theme', command=lambda: chenge_theme('light'))
view_menu.add_cascade(label='Theme', menu=view_menu_sub)

# шрифт
font_menu_sub.add_command(label='Arial', command=lambda: chenge_fonts('Arial'))
font_menu_sub.add_command(label='Comic Sans MS', command=lambda: chenge_fonts('CSMS'))
font_menu_sub.add_command(label='Times New Roman', command=lambda: chenge_fonts('TNR'))
view_menu.add_cascade(label='Font...', menu=font_menu_sub)
root.config(menu=view_menu)


# добавление списков меню
main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_cascade(label='View', menu=view_menu)
root.config(menu=main_menu)



f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)


# создаем словарь
view_colors = {
    'dark': {
        'text_bg': 'black', 'text_fg': 'lime', 'cursor': 'brown', 'select_bg': '#8D917A'
    },
    'light': {
        'text_bg': 'white', 'text_fg': 'black', 'cursor': '#A5A5A5', 'select_bg': '#FAEEDD'
    }
}

fonts = {
    'Arial': {
        'font': 'Arial 14 bold'
    },
    'CSMS': {
        'font': ('Comic Sans MS', 14, 'bold')
    },
    'TNR': {
        'font': ('Times New Roman', 14, 'bold')
    }
}



text_fild = Text(f_text, bg='black',    # будет находиться в f_text
                 fg='lime',
                 padx=10,           # отступы
                 pady=10,
                 wrap=WORD,          # отвечает за правильный перенос слов
                 insertbackground='brown',   # курсор
                 selectbackground='#8D917A',   # цвет текста при выделении
                 spacing3=10,       # абзацы(отступы)
                 width=30,           # ширина
                 font='Arial 14 bold'
                 )
text_fild.pack(expand=1, fill=BOTH, side=LEFT)

scroll = Scrollbar(f_text, command=text_fild.yview)     # полоса прокрутки
scroll.pack(side=LEFT, fill=Y)      # должны растянуть по Y
text_fild.config(yscrollcommand=scroll.set)

root.mainloop()

