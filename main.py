import random
from time import sleep
import time
import pygame

clockk = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1200, 360), vsync=1)
pygame.display.set_caption("name")
icon = pygame.image.load("img.png")
pygame.display.set_icon(icon)
square = pygame.Surface((50, 150))
square.fill("#fff000")
run = True
my_font = pygame.font.SysFont('notosans', 20)
text_surf = my_font.render("HUBUVBWUIRO", False, "#000000")
bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (1200, 360))
bg_sound = pygame.mixer.Sound("sounds/soundtrack.ogg")
bg_sound.play()
enemy_list = []
walk_left = [
    pygame.image.load('walk/title000_l.png'),
    pygame.image.load('walk/title001_l.png'),
    pygame.image.load('walk/title002_l.png'),
    pygame.image.load('walk/title003_l.png'),
    pygame.image.load('walk/title004_l.png'),
    pygame.image.load('walk/title005_l.png'),
    pygame.image.load('walk/title006_l.png'),
    pygame.image.load('walk/title007_l.png'),
    pygame.image.load('walk/title008_l.png'),
    pygame.image.load('walk/title009_l.png')
]
walk_right = [
    pygame.image.load('walk/tile000.png'),
    pygame.image.load('walk/tile001.png'),
    pygame.image.load('walk/tile002.png'),
    pygame.image.load('walk/tile003.png'),
    pygame.image.load('walk/tile004.png'),
    pygame.image.load('walk/tile005.png'),
    pygame.image.load('walk/tile006.png'),
    pygame.image.load('walk/tile007.png'),
    pygame.image.load('walk/tile008.png'),
    pygame.image.load('walk/tile009.png')
]
player_jump = [
    pygame.image.load('jump/jump000.png'),
    pygame.image.load('jump/jump001.png'),
    pygame.image.load('jump/jump002.png'),
    pygame.image.load('jump/jump003.png'),
    pygame.image.load('jump/jump004.png'),
    pygame.image.load('jump/jump005.png'),
    pygame.image.load('jump/jump006.png'),
    pygame.image.load('jump/jump007.png'),
    pygame.image.load('jump/jump008.png'),
    pygame.image.load('jump/jump009.png')
    # pygame.transform.flip()
]
enemy = pygame.image.load('enemy.jpg')
enemy_x = 1200
player_frames = 0
player_jump_frames = 0
bg_x = 0
player_speed = 5
player_x = 150
player_y = 135
is_jump = False
jump_count = 5
screen.fill("#a0b0f0")
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 5000)
label = pygame.font.SysFont('notosans',50)
label_end = label.render('You Lose',True,'#FFFFFF')
restart_label = label.render('restart',True,'#FFFFFF')
restart_label_rect = restart_label.get_rect(topleft=(500,200))
gp = True
while run:
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 1200, 0))
    if gp:
        player_rect = walk_left[0].get_rect(topleft=(player_x + 48, player_y + 48))

        if enemy_list:
            for (i, el) in enumerate(enemy_list):
                screen.blit(enemy, el)
                el.x -= 10

                if el.x < -45:
                    enemy_list.pop(i)

                if player_rect.colliderect(el):
                    gp = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and is_jump == False:
            screen.blit(walk_left[player_frames], (player_x, player_y))
        elif not keys[pygame.K_LEFT] and is_jump == False:
            screen.blit(walk_right[player_frames], (player_x, player_y))

        if keys[pygame.K_LEFT] and player_x >= 20:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x <= 180:
            player_x += player_speed
        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -5:
                if jump_count > 0:
                    player_y -= (jump_count ** 2)
                    screen.blit(player_jump[player_jump_frames], (player_x, player_y))

                else:
                    player_y += (jump_count ** 2)
                    screen.blit(player_jump[player_jump_frames], (player_x, player_y))
                if player_jump_frames == 9:
                    player_jump_frames = 0
                else:
                    player_jump_frames += 1
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 5
        if player_frames == 9:
            player_frames = 0
        else:
            player_frames += 1
        bg_x -= 2
        enemy_x -= 10
        if bg_x == 1200:
            bg_x = 0
    else:
        screen.fill('#1e1e1e')
        screen.blit(label_end,(500,100))
        screen.blit(restart_label,restart_label_rect)
        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gp = True
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == enemy_timer:
            enemy_list.append(enemy.get_rect(topleft=(random.randint(1200, 1300), 165)))
    clockk.tick(24)
