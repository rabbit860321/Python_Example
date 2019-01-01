import pygame

pygame.init()  #初始化pygame
pygame.display.set_caption('畫矩形') #視窗標題

screen = pygame.display.set_mode((350,350))  #視窗大小
screen.fill((255,255,255))                   #視窗顏色

pygame.draw.rect(screen,(255,0,0),(75,50,50,150),0)      #畫矩形
pygame.draw.circle(screen,(0,255,0),(200,200),50,5)      #畫圓形
pygame.draw.ellipse(screen,(0,0,255),(100,80,240,120),3) #畫橢圓形

pygame.display.flip()                        #將視窗顯示在螢幕上

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT: #如果視窗的X被按下跳出迴圈
        break
pygame.quit()
