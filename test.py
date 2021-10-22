import pygame
from pygame.constants import KEYDOWN
import time
import random

pygame.init()



def message(msg, color, pos):
    mesg= font_style.render(msg, True, color)
    dis.blit(mesg, pos)

def change_snake_head(x, y, score, list):
    size= score+1
    list.append((x,y))
    if(len(list)>size):
        list.pop(0)
    

white= (255, 255, 255)
black= (0, 0, 0)
red= (255, 0, 0)
blue= (0, 0, 255)

score= 0
width= 400
height= 400 

dis= pygame.display.set_mode([width, height])
font_style= pygame.font.SysFont(None, 50)

pygame.display.set_caption("Snake Game")
dis.fill(white)
x= width/2
y= height/2
list=[(x,y)]
food_x= random.randint(0, width)
food_y= random.randint(0, height)

x_change=0
y_change=0

clock= pygame.time.Clock()

game_over=False

while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change= -5
                y_change=0
            if event.key == pygame.K_RIGHT:
                x_change= 5
                y_change=0
            if event.key == pygame.K_UP:
                x_change= 0
                y_change=-5
            if event.key == pygame.K_DOWN:
                x_change=0
                y_change=5
    if x>=width or x <=0 or y>=height or y <=0:
        game_over=True
    x+=x_change
    y+=y_change

    dis.fill(white)
    pygame.draw.rect(dis, blue, [food_x, food_y, 10, 10])
    print(f"({x},{y})-->({food_x},{food_y})")
    if int(x)>=food_x-10 and int(x) <=food_x+10 and int(y)>=food_y-10 and int(y)<=food_y+10:
        food_x= random.randint(0, width)
        food_y= random.randint(0, height)
        score +=1
        print(score)
    message(f"{score}", black, [10, 10])
    change_snake_head(x,y, score, list)
    for ele in list:
        pygame.draw.rect(dis, black, [ele[0], ele[1], 10, 10])

    pygame.display.update()
    clock.tick(30)

dis.fill(white)
message(f'Game Over', red, [width/2, height/2])
pygame.display.update()
time.sleep(5)

pygame.quit()
quit()
