import pygame
from pygame.locals import *
from pygame import mixer
import os
import time
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SHREK BLASTER 2000")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DONKEY = (255, 0, 0)
SHREK = (255, 255, 0)

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

SHREK_HIT_SOUND = pygame.mixer.Sound('Assets/shrek_hit_sound.mp3')
DONKEY_HIT_SOUND = pygame.mixer.Sound('Assets/donkey_hit_sound.mp3')
WHIFF_HIT_SOUND = pygame.mixer.Sound('Assets/sword_whiff.mp3')

WOW_SOUND = pygame.mixer.Sound('Assets/wow2trim.mp3')
MY_SWAMP_SOUND = pygame.mixer.Sound('Assets/myswamp.mp3')
pygame.mixer.music.load('Assets/allstar_mod.mp3')

HEALTH_FONT = pygame.font.SysFont('gabriola', 60)
WINNER_FONT = pygame.font.SysFont('gabriola', 200)

FPS = 60

SHREK_VEL = 4
SHREK_BULLET_VEL = 4
SHREK_MAX_BULLETS = 13
SHREKSHIP_WIDTH, SHREKSHIP_HEIGHT = 200, 140

DONKEY_VEL = 10
DONKEY_BULLET_VEL = 15
DONKEY_MAX_BULLETS = 3
DONKEYSHIP_WIDTH, DONKEYSHIP_HEIGHT = 80, 70

SHREK_HIT = pygame.USEREVENT + 1
DONKEY_HIT = pygame.USEREVENT + 2

SHREK_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'shrek.png'))
SHREK_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(SHREK_SPACESHIP_IMAGE, (300, 300)), 0)

DONKEY_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'donkey2.png'))
DONKEY_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(DONKEY_SPACESHIP_IMAGE, (90, 90)), 0)

SWAMP = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'swamp.png')), (WIDTH, HEIGHT))


def draw_window(donkey, shrek, donkey_bullets, shrek_bullets, donkey_health, shrek_health):
    WIN.blit(SWAMP, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    donkey_health_text = HEALTH_FONT.render("Health: " + str(donkey_health), 1, WHITE)
    shrek_health_text = HEALTH_FONT.render("Health: " + str(shrek_health), 1, WHITE)
    WIN.blit(donkey_health_text, (WIDTH - donkey_health_text.get_width() - 10, 10))
    WIN.blit(shrek_health_text, (10, 10))

    WIN.blit(SHREK_SPACESHIP, (shrek.x, shrek.y))
    WIN.blit(DONKEY_SPACESHIP, (donkey.x, donkey.y))

    for bullet in donkey_bullets:
        pygame.draw.rect(WIN, DONKEY, bullet)

    for bullet in shrek_bullets:
        pygame.draw.rect(WIN, SHREK, bullet)

    pygame.display.update()


def shrek_handle_movement(keys_pressed, shrek):
    if keys_pressed[pygame.K_a] and shrek.x - SHREK_VEL > 0:  # LEFT
        shrek.x -= SHREK_VEL
    if keys_pressed[pygame.K_d] and shrek.x + SHREK_VEL + shrek.width < BORDER.x:  # RIGHT
        shrek.x += SHREK_VEL
    if keys_pressed[pygame.K_w] and shrek.y - SHREK_VEL > 0:  # UP
        shrek.y -= SHREK_VEL
    if keys_pressed[pygame.K_s] and shrek.y + SHREK_VEL + shrek.height < HEIGHT - 15:  # DOWN
        shrek.y += SHREK_VEL


def donkey_handle_movement(keys_pressed, donkey):
    if keys_pressed[pygame.K_LEFT] and donkey.x - DONKEY_VEL > BORDER.x + BORDER.width:  # LEFT
        donkey.x -= DONKEY_VEL
    if keys_pressed[pygame.K_RIGHT] and donkey.x + DONKEY_VEL + donkey.width < WIDTH:  # RIGHT
        donkey.x += DONKEY_VEL
    if keys_pressed[pygame.K_UP] and donkey.y - DONKEY_VEL > 0:  # UP
        donkey.y -= DONKEY_VEL
    if keys_pressed[pygame.K_DOWN] and donkey.y + DONKEY_VEL + donkey.height < HEIGHT - 15:  # DOWN
        donkey.y += DONKEY_VEL

def handle_bullets(shrek_bullets, donkey_bullets, shrek, donkey):
    for bullet in shrek_bullets:
        bullet.x += SHREK_BULLET_VEL
        if donkey.colliderect(bullet):
            pygame.event.post(pygame.event.Event(DONKEY_HIT))
            shrek_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            shrek_bullets.remove(bullet)

    for bullet in donkey_bullets:
        bullet.x -= DONKEY_BULLET_VEL
        if shrek.colliderect(bullet):
            pygame.event.post(pygame.event.Event(SHREK_HIT))
            donkey_bullets.remove(bullet)
        elif bullet.x < 0:
            donkey_bullets.remove(bullet)


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, (255,0,0)) #(255,0,0) is red
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() / 2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():


    donkey = pygame.Rect(700, 300, DONKEYSHIP_WIDTH, DONKEYSHIP_HEIGHT)
    shrek = pygame.Rect(50, 100, SHREKSHIP_WIDTH, SHREKSHIP_HEIGHT)

    donkey_bullets = []
    shrek_bullets = []

    donkey_health = 10
    shrek_health = 25

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f and len(shrek_bullets) < SHREK_MAX_BULLETS:
                    bullet = pygame.Rect(shrek.x + shrek.width, shrek.y + shrek.height//2 - 2, 10, 5)
                    shrek_bullets.append(bullet)
                    WHIFF_HIT_SOUND.play()

                if event.key == pygame.K_l and len(donkey_bullets) < DONKEY_MAX_BULLETS:
                    bullet = pygame.Rect(donkey.x, donkey.y + donkey.height//2 - 2, 10, 5)
                    donkey_bullets.append(bullet)
                    WHIFF_HIT_SOUND.play()

            if event.type == DONKEY_HIT:
                donkey_health -= 1
                if donkey_health != 0:
                    DONKEY_HIT_SOUND.play()

            if event.type == SHREK_HIT:
                shrek_health -= 1
                if shrek_health !=0:
                    SHREK_HIT_SOUND.play()

        winner_text = ""
        if donkey_health <= 0:
            winner_text = "SHRek Wins!"
            shrek_win_face = pygame.image.load(os.path.join('Assets', 'shrek_win.png'))
            shrek_win_enlarge = pygame.transform.rotate(pygame.transform.scale(shrek_win_face, (2000, 1000)), 0)
            WIN.blit(shrek_win_enlarge, (-500, -200))
            WOW_SOUND.play()

        if shrek_health <= 0:
            winner_text = "donky win"
            shrek_lost_rotate = pygame.transform.rotate(pygame.transform.scale(SHREK_SPACESHIP_IMAGE, (450, 450)), 180)
            WIN.blit(shrek_lost_rotate, (shrek.x, shrek.y))
            WOW_SOUND.play()

        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        shrek_handle_movement(keys_pressed, shrek)
        donkey_handle_movement(keys_pressed, donkey)

        handle_bullets(shrek_bullets, donkey_bullets, shrek, donkey)

        draw_window(donkey, shrek, donkey_bullets, shrek_bullets,
                    donkey_health, shrek_health)



    main()


if __name__ == "__main__":

    MY_SWAMP_SOUND.play()
    time.sleep(3)
    pygame.mixer.music.play()
    main()
