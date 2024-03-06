import pygame
import random
import time
pygame.init()

size = [400, 900] #화면 사이즈 
screen = pygame.display.set_mode(size)

title = "game"
pygame.display.set_caption(title)
#게임 설정 
clock = pygame.time.Clock()

class obj:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.move = 0
    def put_img(self, address):
        if address[-3:] == "png":
            self.img = pygame.image.load(address).convert_alpha()
        else :
            self.img = pygame.image.load(address)
            self.sx, self.sy = self.img.get_size()
            
    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx, sy))
        self.sx, self.sy = self.img.get_size()

    def show(self):
        screen.blit(self.img, (self.x,self.y))

def crash(a, b):
    if (a.x-b.sx <= b.x) and (b.x <= a.x + a.sx):
        if  (a.y-b.sy <= b.y) and (b.y <= a.y + a.sy):
            return True
        else :
            return False 
    else :
        return False 
    

ss = obj()
ss.put_img("C:/Users/join/Downloads/char.png")#이미지의 주소 
ss.change_size(50,80)
ss.x = round(size[0]/2 - ss.sx/2)
ss.y = size[1]-ss.sy-15
ss.move = 5

left_go = False
right_go = False
space_go = False


m_list = []
a_list = []        
black = (0,0,0)
white = (255,255,255)
k = 0

kill = 0



#이벤트
SB = 0
while SB == 0:

    clock.tick(60) #FPS설정

    for event in pygame.event.get(): #실시간으로 동작을 받는다(각종 입력 감지)
        if event.type == pygame.QUIT:
            SB = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  #왼쪽 
                left_go = True
            elif event.key == pygame.K_RIGHT:   #오른쪽 
                right_go = True
            elif event.key == pygame.K_SPACE: #발사 
                space_go = True
                k = 0
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_go = False
            elif event.key == pygame.K_RIGHT:
                right_go = False
            elif event.key == pygame.K_SPACE: #발사
                space_go = False
    
#입력, 시간에 따른 변화
    if left_go == True:
        ss.x -=ss.move
        if ss.x <= 0:
            ss.x = 0
    elif right_go == True:
        ss.x += ss.move
        if ss.x >= size[0] - ss.sx:
            ss.x = size[0] - ss.sx
   
    if space_go == True and k%6 == 0:
        mm = obj()
        mm.put_img("C:/Users/join/Downloads/mm.png")#이미지의 주소 
        mm.change_size(30,50)
        mm.x = round(ss.x + ss.sx/2 - mm.sx/2)
        mm.y = ss.y - mm.sy - 10
        mm.move = 15
        m_list.append(mm)

    k += 1
    d_list = []
    for i in range(len(m_list)):
        m = m_list[i]
        m.y -= m.move
        if m.y <= -m.sy:
            d_list.append(i)
    for d in d_list:
        del m_list[d]

    if random.random() > 0.98 :
        aa = obj()
        aa.put_img("C:/Users/join/Downloads/bb1.png")#이미지의 주소 
        aa.change_size(60,60)
        aa.x = random.randrange(0,size[0]-aa.sx-round(ss.sx/2))
        aa.y = 10
        aa.move = 1
        a_list.append(aa)
    d_list = []
    
    for i in range(len(a_list)):
        a = a_list[i]
        a.y += a.move
        if a.y >= size[1]: 
            d_list.append(i)
    for d in d_list:
        del a_list[d]
        

    dm_list = []
    da_list = []
    for i in range(len(m_list)):
        for j in range(len(a_list)):
            m=m_list[i]
            a=a_list[j]
            if crash(m,a) == True:
                dm_list.append(i)
                da_list.append(j)
    dm_list = list(set(dm_list))#중복 없애기>리스트의 형태로 다시 변형
    da_list = list(set(da_list))

    for dm in dm_list:
        del m_list[dm]
    for da in dm_list:
        del a_list[da]
        kill += 1

    for i in range(len(a_list)):
        a = a_list[i]
        if crash(a, ss) == True:
            SB = 1
            time.sleep(1)
 

    #그림
    screen.fill(black)
    ss.show()
    for m in m_list:
        m.show()
        
    for a in a_list:
        a.show()

    font = pygame.font.Font("C:/Windows/Fonts/ebrimabd.ttf", 20)
    text = font.render("kill : {} ".format(kill), True, (255,255,255))
    screen.blit(text,(10,5))

    #update
    pygame.display.flip()

#종료
pygame.quit()
