import pygame
from pygame.draw import *
from random import randint

pygame.init()

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)         #инициализация шрифта для надписи очков

FPS = 20                                                #число обновлений кадров в секунду

SCR_SIZE = (1200, 800)                                  #размеры окна в формате (ширина, высота)
screen = pygame.display.set_mode(SCR_SIZE)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]      #набор цветов для шаров

score = 0                                               # начальное значение очков игрока

balls = []                                              #массив для данных о шарах
balls_number = 5                                        #число шаров, которые одновременно появляются на экране

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
    В данной версии - увеличивает очки игрока при нажатии на шар,
    а затем генерирует новый шар.
    '''
    global score, balls, balls_number
    for i in range(balls_number):
        if dist(event.pos, balls[i]["center"]) < balls[i]["radius"]:
            score += 1
            balls[i] = new_ball()
        

def new_ball():
    '''
    Создает словарь ball_prop с данными о шарике радиуса r, цвета color,
    с центром в точке center = [x, y] и скоростью по осям speed = [dx, dy].
    Цвет, радиус, скорость и координаты центра выбираются случайно.
    '''
    r = randint(10,100)
    ball_prop = {
                "radius": r,
                "center": [randint(r, SCR_SIZE[i] - r) for i in range(2)],
                "speed": [randint(10,30) for i in range(2)],
                "color": COLORS[randint(0, 5)]
                }

    return ball_prop
    

def speed(r, center, speed):
    '''
    Осуществляет изменение положения шарика.
    Принимает на вход радиус шара (int),
    его координаты и скорость по осям (2 списка из 2 элементов).
    Возвращает новые координаты и новую скорость
    в виде 2 списков из 2 элементов.
    '''
    for i in range(2):
        if (center[i] > SCR_SIZE[i] - r) or (center[i] < r):
            speed[i] *= -1

        center[i] += speed[i]

    return center, speed


def generate_balls():
    '''
    Обрабатывает массив с данными шариков, тем самым меняя их положение на экране.
    При первом запуске заполняет пустой массив balls
    с помощью функции new_ball(), при последующих запусках
    изменяет положение каждого шара с помощью функции speed().
    '''
    global balls, balls_number, screen
    for i in range(balls_number):
        if (not balls) or (len(balls) < balls_number):
            balls.append(new_ball())
        else:
            balls[i]["center"], balls[i]["speed"] = speed(balls[i]["radius"],
                                             balls[i]["center"], balls[i]["speed"])

        circle(screen, balls[i]["color"],
               balls[i]["center"], balls[i]["radius"])
    

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
