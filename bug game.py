from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
import pygame
import sys
import time
import random

from pygame.locals import *

## 함수 선언 부분 ##
def func_open1() :

    WINDOW_WIDTH = 800
    WINDOW_HEIGTH = 600
    GRID_SIZE = 20
    GRID_WIDTH = WINDOW_WIDTH / GRID_SIZE
    GRID_HEIGHT = WINDOW_HEIGTH / GRID_SIZE

    WHITE = (255,255,255)
    GREEN = (0, 50, 0)
    ORANGE = (250, 150, 0)
    GRAY = (100, 100, 100)

    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    FPS = 10

    class Python(object):
        def __init__(self):
            self.create()
            self.color = GREEN

        def create(self):
            self.length = 2
            self.positions = [((WINDOW_WIDTH / 2), (WINDOW_HEIGTH / 2))]
            self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

        def control(self, xy):
            if (xy[0] * -1, xy[1] * -1) == self.direction:
                return
            else:
                self.direction = xy

        def move(self):
            cur = self.positions[0]
            x, y = self.direction
            new = (((cur[0] + (x * GRID_SIZE)) % WINDOW_WIDTH), (cur[1] + (y * GRID_SIZE)) % WINDOW_HEIGTH)
            if new in self.positions[2:]:
                self.create()
            else:
                self.positions.insert(0, new)
                if len(self.positions) > self.length:
                    self.positions.pop()

        def eat(self):
            self.length += 1

        def draw(self, surface):
            for p in self.positions:
                draw_object(surface, self.color, p)

                
    class Feed(object):
        def __init__(self):
            self.position = (0, 0)
            self.color = ORANGE
            self.create()

        def create(self):
            self.position = (random.randint(0, GRID_WIDTH -1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1)*GRID_SIZE)

        def draw(self, surface):
            draw_object(surface, self.color, self.position)


    def draw_object(surface, color, pos):
        r = pygame.Rect((pos[0], pos[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, color, r)

    def check_eat(python, feed):
        if python.positions[0] == feed.position:
            python.eat()
            feed.create()

    def show_info(length, speed, surface):
        font = pygame.font.Font(None, 34)
        text = font.render("Length: " + str(length) + "   speed: " + str(round(speed, 2)), 1, GRAY)
        pos = text.get_rect()
        pos.centerx = 150
        surface.blit(text, pos)
            

    if __name__ == '__main__':
        python = Python()
        feed = Feed()
        
        pygame.init()
        window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH), 0, 32)
        pygame.display.set_caption('Python Game')
        surface = pygame.Surface(window.get_size())
        surface = surface.convert()
        surface.fill(WHITE)
        clock = pygame.time.Clock()
        pygame.key.set_repeat(1, 40)
        window.blit(surface,(0,0))

        while True:

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        python.control(UP)
                    elif event.key == K_DOWN:
                        python.control(DOWN)
                    elif event.key == K_LEFT:
                        python.control(LEFT)
                    elif event.key == K_RIGHT:
                        python.control(RIGHT)

            surface.fill(WHITE)
            python.move()
            check_eat(python, feed)
            speed = (FPS + python.length) / 2
            show_info(python.length, speed, surface)
            python.draw(surface)
            feed.draw(surface)
            window.blit(surface, (0,0))
            pygame.display.flip()
            pygame.display.update()
            clock.tick(speed)

    

    



def func_open2() :

    WINDOW_WIDTH = 800
    WINDOW_HEIGTH = 600
    GRID_SIZE = 20
    GRID_WIDTH = WINDOW_WIDTH / GRID_SIZE
    GRID_HEIGHT = WINDOW_HEIGTH / GRID_SIZE

    WHITE = (255,255,255)
    GREEN = (0, 50, 0)
    ORANGE = (250, 150, 0)
    GRAY = (100, 100, 100)

    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    FPS = 10

    class Python(object):
        def __init__(self):
            self.create()
            self.color = GREEN

        def create(self):
            self.length = 2
            self.positions = [((WINDOW_WIDTH / 2), (WINDOW_HEIGTH / 2))]
            self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

        def control(self, xy):
            if (xy[0] * -1, xy[1] * -1) == self.direction:
                return
            else:
                self.direction = xy

        def move(self):
            cur = self.positions[0]
            x, y = self.direction
            new = (((cur[0] + (x * GRID_SIZE)) % WINDOW_WIDTH), (cur[1] + (y * GRID_SIZE)) % WINDOW_HEIGTH)
            if new in self.positions[2:]:
                self.create()
            else:
                self.positions.insert(0, new)
                if len(self.positions) > self.length:
                    self.positions.pop()

        def eat(self):
            self.length += 1

        def draw(self, surface):
            for p in self.positions:
                draw_object(surface, self.color, p)

                
    class Feed(object):
        def __init__(self):
            self.position = (0, 0)
            self.color = ORANGE
            self.create()

        def create(self):
            self.position = (random.randint(0, GRID_WIDTH -1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1)*GRID_SIZE)

        def draw(self, surface):
            draw_object(surface, self.color, self.position)


    def draw_object(surface, color, pos):
        r = pygame.Rect((pos[0], pos[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, color, r)

    def check_eat(python, feed):
        if python.positions[0] == feed.position:
            python.eat()
            feed.create()

    def show_info(length, speed, surface):
        font = pygame.font.Font(None, 34)
        text = font.render("Length: " + str(length) + "   speed: " + str(round(speed, 2)), 1, GRAY)
        pos = text.get_rect()
        pos.centerx = 150
        surface.blit(text, pos)
            

    if __name__ == '__main__':
        python = Python()
        feed = Feed()
        
        pygame.init()
        window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH), 0, 32)
        pygame.display.set_caption('Python Game')
        surface = pygame.Surface(window.get_size())
        surface = surface.convert()
        surface.fill(WHITE)
        clock = pygame.time.Clock()
        pygame.key.set_repeat(1, 40)
        window.blit(surface,(0,0))

        while True:

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        python.control(UP)
                    elif event.key == K_DOWN:
                        python.control(DOWN)
                    elif event.key == K_LEFT:
                        python.control(LEFT)
                    elif event.key == K_RIGHT:
                        python.control(RIGHT)

            surface.fill(WHITE)
            python.move()
            check_eat(python, feed)
            speed = (FPS + python.length)
            show_info(python.length, speed, surface)
            python.draw(surface)
            feed.draw(surface)
            window.blit(surface, (0,0))
            pygame.display.flip()
            pygame.display.update()
            clock.tick(speed)

    

    



def func_open3() :

    WINDOW_WIDTH = 800
    WINDOW_HEIGTH = 600
    GRID_SIZE = 20
    GRID_WIDTH = WINDOW_WIDTH / GRID_SIZE
    GRID_HEIGHT = WINDOW_HEIGTH / GRID_SIZE

    WHITE = (255,255,255)
    GREEN = (0, 50, 0)
    ORANGE = (250, 150, 0)
    GRAY = (100, 100, 100)

    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    HARD_UP = (0, 1)
    HARD_DOWN = (0, -1)
    HARD_LEFT = (1, 0)
    HARD_RIGHT = (-1, 0)

    FPS = 10

    class Python(object):
        def __init__(self):
            self.create()
            self.color = GREEN

        def create(self):
            self.length = 2
            self.positions = [((WINDOW_WIDTH / 2), (WINDOW_HEIGTH / 2))]
            self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

        def control(self, xy):
            if (xy[0] * -1, xy[1] * -1) == self.direction:
                return
            else:
                self.direction = xy

        def move(self):
            cur = self.positions[0]
            x, y = self.direction
            new = (((cur[0] + (x * GRID_SIZE)) % WINDOW_WIDTH), (cur[1] + (y * GRID_SIZE)) % WINDOW_HEIGTH)
            if new in self.positions[2:]:
                self.create()
            else:
                self.positions.insert(0, new)
                if len(self.positions) > self.length:
                    self.positions.pop()

        def eat(self):
            self.length += 1

        def draw(self, surface):
            for p in self.positions:
                draw_object(surface, self.color, p)

                
    class Feed(object):
        def __init__(self):
            self.position = (0, 0)
            self.color = ORANGE
            self.create()

        def create(self):
            self.position = (random.randint(0, GRID_WIDTH -1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1)*GRID_SIZE)

        def draw(self, surface):
            draw_object(surface, self.color, self.position)


    def draw_object(surface, color, pos):
        r = pygame.Rect((pos[0], pos[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, color, r)

    def check_eat(python, feed):
        if python.positions[0] == feed.position:
            python.eat()
            feed.create()

    def show_info(length, speed, surface):
        font = pygame.font.Font(None, 34)
        text = font.render("Length: " + str(length) + "   speed: " + str(round(speed, 2)), 1, GRAY)
        pos = text.get_rect()
        pos.centerx = 150
        surface.blit(text, pos)
            

    if __name__ == '__main__':
        python = Python()
        feed = Feed()
        
        pygame.init()
        window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH), 0, 32)
        pygame.display.set_caption('Python Game')
        surface = pygame.Surface(window.get_size())
        surface = surface.convert()
        surface.fill(WHITE)
        clock = pygame.time.Clock()
        pygame.key.set_repeat(1, 40)
        window.blit(surface,(0,0))

        while True:

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        python.control(HARD_UP)
                    elif event.key == K_DOWN:
                        python.control(HARD_DOWN)
                    elif event.key == K_LEFT:
                        python.control(HARD_LEFT)
                    elif event.key == K_RIGHT:
                        python.control(HARD_RIGHT)

            surface.fill(WHITE)
            python.move()
            check_eat(python, feed)
            speed = (FPS + python.length)
            show_info(python.length, speed, surface)
            python.draw(surface)
            feed.draw(surface)
            window.blit(surface, (0,0))
            pygame.display.flip()
            pygame.display.update()
            clock.tick(speed)

    

    



def func_exit() :
    window.quit()
    window.destroy()

    


## 메인 코드  부분 ##
window = Tk()
window.geometry("400x400")
window.title("지렁이 키우기")


mainMenu = Menu(window)
window.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "게임 생성", menu=fileMenu)
fileMenu.add_command(label = "쉬움", command=func_open1)
fileMenu.add_separator()
fileMenu.add_command(label = "중간", command=func_open2)
fileMenu.add_separator()
fileMenu.add_command(label = "어려움", command=func_open3)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command=func_exit)

window.mainloop()
