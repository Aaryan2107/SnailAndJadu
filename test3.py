import pygame
pygame.init()

# Window setup
WIDTH, HEIGHT = 800, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sword Adventure")

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Clock
clock = pygame.time.Clock()

# Player setup
player = pygame.Rect(100, 400, 40, 60)
vel_y = 0
gravity = 1
jump_power = -15
on_ground = False
score = 0

# Platforms
platforms = [pygame.Rect(0, 440, 800, 40), pygame.Rect(300, 350, 200, 20)]

# Enemy
enemy = pygame.Rect(500, 410, 40, 40)
enemy_dir = -1

# Game loop
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
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

    # Collision with platforms
    for plat in platforms:
        if player.colliderect(plat) and vel_y >= 0:
            player.bottom = plat.top
            vel_y = 0
            on_ground = True

    # Enemy movement
    enemy.x += enemy_dir * 2
    if enemy.left < 400 or enemy.right > 700:
        enemy_dir *= -1

    # Check collision with enemy
    if player.colliderect(enemy):
        score -= 1

    # Draw everything
    screen.fill(BLUE)
    pygame.draw.rect(screen, GREEN, player)
    for plat in platforms:
        pygame.draw.rect(screen, (100, 80, 30), plat)
    pygame.draw.rect(screen, RED, enemy)

    # Score display
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()
