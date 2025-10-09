import pygame
from sys import exit
pygame.init()
pygame.display.set_caption("Runner")
# icon_image = pygame.image.load('my_icon.png')
# pygame.display.set_icon(icon_image)
screen = pygame.display.set_mode((800 , 400))
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf',50)

# test_surface = pygame.Surface((200,200)) # to create a plain surface
# test_surface.fill("blue") 
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/Ground.png').convert()
text_surface = font.render('SwordDuel',False,'Yellow')
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_position = 800
snail_rect = snail_surface.get_rect(midbottom = (snail_position,300))
player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface,(0,0)) # plot that surface on your display surface
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    snail_rect.x -= 3
    if snail_rect.x == -100 : snail_rect.x = 800
    screen.blit(snail_surface,snail_rect)
    player_rect.left += 1
    screen.blit(player_surf,player_rect)
    pygame.display.update()
    clock.tick(60)