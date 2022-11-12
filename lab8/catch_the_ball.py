import pygame
from pygame.draw import *
from random import randint

pygame.init()

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)         #инициализация шрифта для надписи очков

FPS = 20                                                #число обновлений кадров в секунду

WIDTH = 1200                                            #ширина окна
HEIGHT = 800                                            #высота окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]      #набор цветов для шаров

score = 0                                               # начальное значение очков игрока

balls = [] #массив для данных о шарах
balls_number = 5 #число шаров, которые одновременно появляются на экране

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
    В данной версии - увеличивает очки игрока при нажатии в пределах шара,
    а затем генерирует новый шар.
    '''
    global score, balls, balls_number
    for i in range(balls_number):
        if dist(event.pos, balls[i][1]) < balls[i][0]:
            score += 1
            balls[i] = new_ball()
        

def new_ball():
    '''
    Создает список с данными о шарике радиуса r, цвета color,
    с центром в точке (x, y) и скоростью по осям dx и dy.
    Цвет, радиус, скорость и координаты центра выбираются случайно.
    '''
    #global x, y, dx, dy, r, color

    r = randint(10, 100)
    
    x = randint(r, WIDTH-r)
    y = randint(r, HEIGHT-r)

    dx = randint(10,30)
    dy = randint(10,30)

    color = COLORS[randint(0, 5)]

    return [r, [x, y], [dx, dy], color]
    

def speed(r, center, speed):
    '''
    Осуществляет изменение положения шарика
    и отскакивание от стенок.
    '''
    #global x, y, dx, dy, r
    x, y = center
    dx, dy = speed
    if (x > WIDTH - r) or (x < r):
        dx *= -1
    if (y > HEIGHT - r) or (y < r):
        dy *= -1
    x += dx
    y += dy

    return [x, y], [dx, dy]


def generate_balls():
    '''
    Обрабатывает массив с данными шариков,
    тем самым меняя их положение на экране.
    '''
    global balls, balls_number, screen
    for i in range(balls_number):
        if (not balls) or (len(balls) < balls_number):
            balls.append(new_ball())
        else:
            balls[i][1], balls[i][2] = speed(balls[i][0],
                                             balls[i][1], balls[i][2])
        print(balls[i])
        circle(screen, balls[i][-1],
               balls[i][1], balls[i][0])
    

screen.fill(WHITE)                      #заполняет стартовый экран белым цветом
pygame.display.update()

clock = pygame.time.Clock()
finished = False

while not finished:
    generate_balls()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
    show_score()
    
    pygame.display.update()
    screen.fill(WHITE)                  #освобождает экран для следующего шага

pygame.quit()
