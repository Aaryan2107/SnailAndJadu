import pygame
from sys import exit
from random import randint
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.gravity = 0
        player_frame_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        player_frame_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
        self.player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()
        self.player_index = 0
        self.player_walk_list = [player_frame_1,player_frame_2]
        self.player_surf = self.player_walk_list[0]
        self.rect = self.player_surf.get_rect(midbottom = (200,300))

    def player_input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
    def animation_state(self):
        if self.rect.bottom < 300:
            self.player_surf = self.player_jump
        else:
            self.player_index += 0.1
            self.player_surf = self.player_walk_list[int(self.player_index)]
            if self.player_index >= len(self.player_walk_list):
                self.player_index = 0
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()


pygame.init()
pygame.display.set_caption("Runner")
# icon_image = pygame.image.load('my_icon.png')
# pygame.display.set_icon(icon_image)
screen = pygame.display.set_mode((800 , 400))
clock = pygame.time.Clock()
font1 = pygame.font.Font('font/Pixeltype.ttf',50)
font2 = pygame.font.Font('font/Pixeltype.ttf',30)
start_time = 0
player = pygame.sprite.GroupSingle()
# player.add(Player())
# test_surface = pygame.Surface((200,200)) # to create a plain surface
# test_surface.fill("blue") 
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/Ground.png').convert()

score_surf = font1.render('SwordDuel',False,(64,64,64)) #(r,g,b)
score_rect = score_surf.get_rect(center = (400,100))

over_surf = font1.render('Game Over',False,(64,64,64))
over_rect = over_surf.get_rect(center = (400,200))

start_surf = font2.render('Click space to start the game',False,(64,64,64))
start_rect = start_surf.get_rect(center = (400,250))

restart_surf = font2.render('Click space to restart the game',False,(64,64,64))
restart_rect = restart_surf.get_rect(center = (400,250))

snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
snail_index = 0
snail_surf_list = [snail_frame_1,snail_frame_2]
snail_surf = snail_surf_list[snail_index] 

fly_frame_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
fly_index = 0
fly_surf_list = [fly_frame_1,fly_frame_2]
fly_surf = fly_surf_list[fly_index]
obstacle_rect_list = []

player_frame_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_frame_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()
player_index = 0
player_walk_list = [player_frame_1,player_frame_2]
player_surf = player_walk_list[0]
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0 
final_score = 0 
player_stand_surf = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand_rect = player_stand_surf.get_rect(center = (200,100))

game_active = False

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer,500)

fly_animation_timer = pygame.USEREVENT + 3 
pygame.time.set_timer(fly_animation_timer,200)


def display_score():
    current_time = (pygame.time.get_ticks() - start_time)//500
    score_surf = font1.render(f'Score: {current_time}',False,(64,64,64)) #(r,g,b)
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return current_time
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf,obstacle_rect)
            else:
             screen.blit(fly_surf,obstacle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []
def collisions(player,obstacle_list):
    if obstacle_list:
        for obstacle in obstacle_list:
            if player.colliderect(obstacle):
                return False
    return True
def player_animation():
    global player_surf,player_index
    if player_rect.bottom > 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk_list):
            player_index = 0
        player_surf = player_walk_list[int(player_index)]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if(player_rect.bottom == 300):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player_gravity = -20
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if player_rect.collidepoint(event.pos):
                        player_gravity = -20
            if event.type == obstacle_timer :
                if randint(0,2):
                    obstacle_rect_list.append(snail_surf.get_rect(midbottom = (randint(900,1100),300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(midbottom = (randint(900,1100),210)))
            if event.type == snail_animation_timer:
                if snail_index == 0:
                    snail_index = 1
                else:
                    snail_index = 0
                snail_surf = snail_surf_list[snail_index]
            if event.type == fly_animation_timer:
                if fly_index == 0:
                    fly_index = 1
                else:
                    fly_index = 0
                fly_surf = fly_surf_list[fly_index]
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_rect.left = 80
                    obstacle_rect_list = []
                    game_active = True
                    start_time = pygame.time.get_ticks()       
        # if event.type == pygame.KEYUP:
        #     print("key up")
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):print("collision")
        # if event.type == pygame.MOUSEMOTION: #this tracks the mouse motion 
        #     print(event.pos) #note: if only the mouse moves it gives position
        # if event.type == pygame.MOUSEBUTTONUP: #this registers the mouse click release
        #     print('MOUSE UP')
    if game_active:
        screen.blit(sky_surface,(0,0)) # plot that surface on your display surface
        screen.blit(ground_surface,(0,300))
        # pygame.draw.rect(screen , 'black' , score_rect , 6 , 20) #width = 6 ,border_radius = 20
        pygame.draw.rect(screen , '#c0e8ec' , score_rect)
        pygame.draw.rect(screen , '#c0e8ec' , score_rect , 10)
        # pygame.draw.line(screen, 'Red', (0,0), (800,400), width=10)
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        # snail_rect.x -= 5
        # if snail_rect.x <= -50 : snail_rect.x = 800
        # screen.blit(snail_surface,snail_rect)
        a = display_score()
        final_score = a
        # player_rect.left += 2
        player_gravity += 1
        player_rect.y += player_gravity
        if(player_rect.bottom >= 300):
            player_rect.bottom = 300
        player_animation()
        screen.blit(player_surf,player_rect)
        player.draw(screen)
        player.update()
        game_active = collisions(player_rect,obstacle_rect_list)
        # if player_rect.colliderect(snail_rect): #to check if the player rect. is colliding with the snail rect.
        #     print("collision")
        # mouse_pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint(mouse_pos): #to check if the mouse is colliding with the mouse 
        #     print(pygame.mouse.get_pressed())
        # keys = pygame.key.get_pressed() #to check the keyboard input
        # if keys[pygame.K_SPACE] == 1:
        #     print("Jump")
        current_time1 = pygame.time.get_ticks()//500
        score_time = str(current_time1)
    else:
        if(final_score == 0):
            screen.fill((94,129,162))
            screen.blit(player_stand_surf,player_stand_rect)
            screen.blit(score_surf,score_rect)
            screen.blit(start_surf,start_rect)

        else:
            screen.fill((94,129,162))
            screen.blit(over_surf,over_rect)
            result_surf = font1.render(f"Your score: {final_score}",False,(0,0,0))
            result_rect = result_surf.get_rect(center = (400,150))
            screen.blit(restart_surf,restart_rect)
            screen.blit(result_surf,result_rect)
    pygame.display.update()
    clock.tick(60)
