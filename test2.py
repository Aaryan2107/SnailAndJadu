import pygame
pygame.init()

# Screen
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Player
player = pygame.Rect(100, 500, 40, 60)
vel_y = 0
gravity = 1
jump_power = -15
on_ground = False

# Platforms
platforms = [pygame.Rect(0, 550, 800, 50), pygame.Rect(300, 400, 200, 20)]

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_SPACE] and on_ground:
        vel_y = jump_power
    
    # Gravity
    vel_y += gravity
    player.y += vel_y
    on_ground = False
    
    # Collision
    for plat in platforms:
        if player.colliderect(plat) and vel_y >= 0:
            player.bottom = plat.top
            vel_y = 0
            on_ground = True
    
    # Draw
    win.fill((135, 206, 235))  # sky blue
    pygame.draw.rect(win, (255, 0, 0), player)  # player
    for plat in platforms:
        pygame.draw.rect(win, (0, 255, 0), plat)
    pygame.display.flip()

pygame.quit()
