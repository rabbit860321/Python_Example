import pygame

class MySprite(pygame.sprite.Sprite):   #MySprite類別繼承sprite
    def __init__(self,target):
        pygame.sprite.Sprite.__init__(self)
        self.target_surface = target
        self.image = None
        self.master_image = None
        self.rect = None
        self.topleft = 0,0
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0
        
    def load(self,filename,width,height,columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.rect = 0,0,width,height
        self.columns = columns
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) -1

    def update(self, current_time, rate=60):
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time

        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = ( frame_x, frame_y, self.frame_width, self.frame_height )
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame

        
pygame.init()

screen = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption("Sprite2")
font = pygame.font.Font(None,18)
framerate = pygame.time.Clock()

cat1 = MySprite(screen)
cat1.load('sprite.png',100,100,4)
cat1.rect = (100,100)  #顯示位置

cat2 = MySprite(screen)
cat2.load('sprite.png',100,100,4)
cat2.rect = (200,200)  #顯示位置

group = pygame.sprite.Group()
group.add(cat1)
group.add(cat2)



while True:
    framerate.tick(30)
    ticks = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #如果視窗的X被按下跳出迴圈
            pygame.quit()
            exit()

    screen.fill((255,255,255))
    group.update(ticks)
    group.draw(screen)
    
    pygame.display.update()

