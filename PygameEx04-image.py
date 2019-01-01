import pygame,sys

pygame.init()  #初始化pygame
pygame.display.set_caption('圖片') #視窗標題

screen = pygame.display.set_mode((800,600))  #視窗大小
screen.fill((255,255,255))                   #視窗顏色

i = 0
bg = 'background.png'
mouse_image = 'cat02.png'
dog_image = 'dog01.png'

image = pygame.image.load(bg).convert()
mouse_cursor = pygame.image.load(mouse_image).convert_alpha()
dog = pygame.image.load(dog_image).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #如果視窗的X被按下跳出迴圈
            pygame.quit()
            exit()

    screen.blit(image,(0,0))        #背景
    screen.blit(dog,(700-i,400))    #dog

    i += 1
    if(i == 800):
        i = 0
        pygame.time.wait(100)

    x,y = pygame.mouse.get_pos()    #取得滑鼠座標
    screen.blit(mouse_cursor,(x,y)) #鼠標
    pygame.time.wait(10)
    
    pygame.display.update()
