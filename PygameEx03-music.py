import pygame,time

pygame.init()  #初始化pygame
pygame.display.set_caption('音樂') #視窗標題

screen = pygame.display.set_mode((350,350))  #視窗大小
screen.fill((255,255,255))                   #視窗顏色

pygame.display.flip()                        #將視窗顯示在螢幕上 

soundObj = pygame.mixer.Sound('match0.wav')  #建立聲音object
soundObj.play()
time.sleep(1)
soundObj.stop()

pygame.mixer.music.load('foo.mp3')
pygame.mixer.music.play(-1,0.0)              #指無數次迴圈 從0.0開始
time.sleep(15)

pygame.mixer.music.stop()


while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT: #如果視窗的X被按下跳出迴圈
        break
pygame.quit()
