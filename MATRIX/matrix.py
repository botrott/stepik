import pygame as pg     # работа с графикой (обращаются через pg.)
import random

class MatrixLetters:       # класс для отрисовки матрицы
    def __init__(self, app):    # инициализация, для того чтобы наш класс мог обращаться к классу MatrixApp, добавляем параметр app
        self.app = app
        #self.letters = 'QWERTYUIOPASDFGHJKLZXCVBNM123456789'  # для отображения определенных символов
        #self.letters = 'ИДИНАХУЙ'
        self.font_size = 14     # размер шрифта
        self.font = pg.font.SysFont('Cousine', self.font_size, bold=True)  # обьект шрифта
        self.letters = [chr(i) for i in range(48, 123)]
        self.columns = app.WIDTH // self.font_size          # создание каплей, обратились к классу app и взяли ширину, делим на кол-во шрифта
        self.drops = [1 for i in range(0, self.columns)]    # создадим список, в котором будем хранить местоположение наших букв, заполним его 1, имеет длинну, сколько каплей помещается на экране

    def draw(self):     # отрисовка символов
        for i in range(0, len(self.drops)):         # от 0 до длины нашего списка
            char = random.choice(self.letters)        # берет случай символ из переменной lettres
            char_render = self.font.render(char, False, (0, 255, 0))    # отрисовываем символ на экране(red, green, blue)
            pos = i * self.font_size, (self.drops[i] - 1) * self.font_size      # посчитаем позицию, если поставить -1, то позиция сместится за край, что придаст лучший вид
            self.app.surface.blit(char_render, pos)            # что отображаем и в каких координатах
            if self.drops[i] * self.font_size > app.HEIGTH and random.uniform(0, 1) > 0.975:  # задаем условие
                self.drops[i] = 0                   # если вышли за пределы, то скидываем букву в начало
            self.drops[i] = self.drops[i] + 1       # будем смещаться на единицу если будет выполнено условие с высотой, и > 0.975

    def run(self):
        self.draw()     # вызывает функцию которая будет отрисовывать символы на экране


class MatrixApp:
    def __init__(self):     # инициализация приложения
        self.RES = self.WIDTH, self.HEIGTH = 1920, 1080   # создаем обьект "резолюшен" который будет содержать ширину и высоту
        pg.init()           # проинициализируем наш pg для нашего приложения
        self.screen = pg.display.set_mode(self.RES)     # создаем экран нашего приложения, self.RES(указывает размер нашего экрана из переменной self.RES)
        #self.surface = pg.Surface(self.RES)            # поверхность отрисовки наших обьектов
        self.surface = pg.Surface(self.RES, pg.SRCALPHA)    # добавлен эффект затухания через pg.SCRALPHA
        self.clock = pg.time.Clock()                    # отлеживает наше время
        self.matrixLetters = MatrixLetters(self)        # вызывем класс, экземпляр класса наших букв

    def draw(self):     # (функция которая будет орисовывать наш экран) закраска раб. поверхности и нанесем на гл.экран
        #self.surface.fill(pg.Color('black'))      # закрасим нашу поверхность черным
        self.surface.fill(pg.Color(0, 0, 0, 10))
        self.matrixLetters.run()     # после заливки, вызываем отрисовку символов
        self.screen.blit(self.surface, (0, 0))      # выводит на экран

    def run(self):      # метод для запуска, главный цикл программы
        while True:       # будет бесконечно отрабатывать(отрисовку экрана, проверку на выход, обновление поверхности, кол-во кадров)
            self.draw()     # вызвали функцию отрисовки нашего экрана
            [exit() for i in pg.event.get() if i.type == pg.QUIT]     # проверка событий на выход программы
            pg.display.flip()       # когда мы запускаем наше приложение, мы должны обновить поверхность
            self.clock.tick(20)     # кол-во кадров в секунду


# структура приложения, с использованием обьекто-оринетированного подхода
# должны убедиться что файл main является запускаемым по умолчанияю,
# для того чтобы его нельзя было заимпортировать, и он сразу выполнился 2 раз

if __name__ == '__main__':  # эта конструкция кода, позволяет запускать тот код, который находится в блоке когда,
                            # в том случае если этот файл является запускаемым первым файлом,
                            # который выбран как исполняемый файл
    app = MatrixApp()       # наше приложение будет храниться в обьекте app, этот обьект будет создаваться
                            # из нашего основного класса MatrixApp
    app.run()               # наш класс будет иметь метод run для запуска




