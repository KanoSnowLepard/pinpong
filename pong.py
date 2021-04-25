from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x,player_y,size_w, size_h, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_w , size_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.direction = "left"
        self.rect.x = player_x
        self.rect.y = player_y
         
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed() 
        if keys_pressed[K_w]:
            self.rect.y -= self.speed
        if keys_pressed[K_s]:
            self.rect.y += self.speed   
    def update_L(self):
        keys_pressed = key.get_pressed() 
        if keys_pressed[K_UP]:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN]:
            self.rect.y += self.speed

font.init()
text = font.SysFont("Arial.ttf", 100).render("Im black",True,(0,0,0))

font1 = font.Font(None, 35)
lose1 = font1.render("igrok 2 win",True,(0,0,0))
font2 = font.Font(None, 35)
lose2 = font2.render("igrok 1 win",True,(0,0,0))

player1 = Player("argo1.png", 10,200,20,150,10)
player2= Player("argo2.png", 640,200,20,150,10)
ball = GameSprite("catball.png",300,300,50,50,30)

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill((255,255,255))
display.set_caption("bong")

clock = time.Clock()
game = True 

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT :
            game == False
    
    window.fill((225,225,225))
    ball.reset()
    ball.rect.y +=speed_y
    ball.rect.x +=speed_x
    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200,200))
    if ball.rect.x > 650:
        finish = True
        window.blit(lose2, (200,200))
    player1.update_r()
    player2.update_L()
    player1.reset()
    player2.reset()
    window.blit(text,(225,225))
    display.update()
    clock.tick(60)
