import pygame
from pygame.draw import *
from random import randint

pygame.init()

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30) #инициализация шрифта для надписи очков

FPS = 2 #число обновлений кадров в секунду
screen = pygame.display.set_mode((1200, 800))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN] #набор цветов для шаров

score = 0 # начальное значение очков игрока

def dist(dot1, dot2):
    '''
    Считает расстояние между 2 точками на плоскости.
    dot1 - кортеж с координатами точки 1,
    dot2 - кортеж с координатами точки 2.
    '''
    dist = (dot1[0]-dot2[0])**2 + (dot1[1]-dot2[1])**2
    dist = dist**0.5
    return dist

def show_score():
    '''
    Выводит очки игрока в верхний левый угол экрана.
    '''
    global score
    text_surface = font.render(f'Score:{score}', True, (0, 0, 0))
    screen.blit(text_surface, (50, 20))

def click(event):
    '''
    Обрабатывает нажатие левой кнопки мыши.
    В данной версии - увеличивает очки игрока при нажатии в пределах шара.
    '''
    global score
    if dist(event.pos, (x, y)) < r: score += 1
        

def new_ball():
    '''
    Рисует новый шарик радиуса r, цвета color
    и с центром в точке (x, y).
    Цвет, радиус и координаты центра выбираются случайно.
    '''
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 700)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

screen.fill(WHITE) #заполняет стартовый экран белым цветом
pygame.display.update()

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
    show_score()
    new_ball()
    
    pygame.display.update()
    screen.fill(WHITE) #освобождает экран для следующего шага

pygame.quit()
