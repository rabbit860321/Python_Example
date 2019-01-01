import pygame,sys,random

pygame.init()       #初始化pygame
pygame.display.set_caption('下雪') #視窗標題

screen = pygame.display.set_mode((800,600))  #視窗大小


class Snow(pygame.sprite.Sprite):   #Snow類別繼承sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((2,2))  
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.centery +=1  #方塊中心y座標
        if self.rect.centery >= 600:
            self.rect.centerx = random.randrange(0,800)
            self.rect.centery = random.randrange(-20,-5)

snow_list = pygame.sprite.Group()
        
for i in range(50):
    snow_icon = Snow()
    snow_icon.rect.centerx = random.randrange(0,800)
    snow_icon.rect.centery = random.randrange(0,600)
    snow_list.add(snow_icon)

clock = pygame.time.Clock()

while True:
    clock.tick(24)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #如果視窗的X被按下跳出迴圈
            pygame.quit()
            exit()
            
    screen.fill((0,0,0))                   #視窗顏色
    snow_list.draw(screen)
    snow_list.update()
    
    pygame.display.update()
