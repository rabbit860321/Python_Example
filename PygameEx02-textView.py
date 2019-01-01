import pygame

def show_text(text,x,y):
    text = myfont.render(text,True,(0,0,0))
    screen.blit(text,(x,y))                  #在(x,y)處貼上文字

pygame.init()  #初始化pygame

pygame.display.set_caption('顯示文字')      #視窗標題
screen = pygame.display.set_mode((350,350))  #視窗大小
screen.fill((255,255,255))                   #視窗顏色
        
myfont = pygame.font.Font("msjh.ttc",24)     #建立字體物件

show_text('Hello Python!',50,100)        
show_text('哈囉 Python!',50,200)           
pygame.display.flip()                       #將視窗顯示在螢幕上

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:        #視窗的X被按下跳出迴圈
        break
pygame.quit()
