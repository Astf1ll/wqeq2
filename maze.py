#создай игру "Лабиринт"!
from pygame import *
#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x  -= self.speed
        if keys_pressed[K_d] and self.rect.x < 650:
            self.rect.x  += self.speed
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 450:
            self.rect.y  += self.speed

class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 200:
            self.direction = "right"
        if self.rect.x >= 310:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


#создай окно игры
window = display.set_mode((700, 500))
display.set_caption("Лабиринт")

font.init()
font = font.Font(None, 70)
win = font.render('text', True, (255, 0, 0))
#класс для спрайтов препятствий
class Wall(sprite.Sprite):
    def __init__(self,color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_heigh):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.heigh = wall_heigh

        self.image = Surface((self.width, self.heigh))
        self.image.fill((color_1, color_2, color_3))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
   
#звуки
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play(-1)
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')


#задай фон сцены
background = transform.scale(image.load("background.jpg"), (700, 500))
#создай 2 спрайта и размести их на сцене
player = Player("hero.png", 40,440,10)
enemy = Enemy("cyborg.png", 300, 120, 7)
lock = GameSprite('treasure.png',540,440,0)
#стена
w1 = Wall(0, 255, 0, 20, 10, 600, 10)
w2 = Wall(0, 255, 0, 120, 150, 10, 400)
w3 = Wall(0, 255, 0, 280, 10, 10, 400)
w4 = Wall(0, 255, 0, 430, 150, 10, 400)
w5 = Wall(0, 255, 0, 590, 10, 10, 400)



clock = time.Clock()
game = True
finish = True
while game:


    if finish:
        window.blit(background, (0, 0))
        player.reset()
        enemy.reset()
        lock.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()



        player.update()
        enemy.update()





        #обработайте событие «клик по кнопке "Закрыть окно"»
        
        

        if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5):
            player.rect.x = 40
            player.rect.y = 440
            kick.play()

        if sprite.collide_rect(player, lock):
            window.blit(win,(350,250))

    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(60)
    display.update()
        
        