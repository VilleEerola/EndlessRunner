import pygame
import random



pygame.init()

Clock = pygame.time.Clock()

#Window size
width = 1000
height = 800

red = (255,0,0)
green = (0, 190, 0)
blue = (0,0,255)
yellow = (255, 255, 0)
white = (255, 255, 255)


display = pygame.display.set_mode((width,height))
pygame.display.set_caption("EndlessRunner")

player = pygame.image.load("steve.png") #loading player image
ob1 = pygame.image.load("obstacle.png")
ob2 = pygame.image.load("obstacle1.png")
ob3 = pygame.image.load("obstacle2.png")
background = pygame.image.load("tausta.jpg") #loading background image
font_style = pygame.font.SysFont("Roman Classic", 45)



   

def message(msg, color, mx, my):  
    mesg = font_style.render(msg, True, color)
    display.blit(mesg,[mx, my])


def game_loop():
    running = True

    x = 150
    y = 560
    dx = 4
    score = 0

    obstacles = [1000, 1200, 1400, 1600, 1800, 2000, 2200]
    obstacle_speed = 2
    active = True


    jumping = False
    y_gravity = 1
    jump_height = 17
    y_velocity = jump_height


    while running:
        display.fill((20,20,40))
        pygame.time.delay(10)
        display.blit(background, (0,0))

        score_display = font_style.render(str(score), True, blue )


        message("Press Q to quit :)", white , 0, 10)
        message("Move left and right with arrows, jump with spacebar !", white , 10, 700)
        message("Score : ", blue, 800, 30)
        display.blit(score_display, (920,30))

        
        floor = pygame.draw.rect(display, green, pygame.Rect(0, 600, 1000 , 10 )) #Prints the groundline
        obstacle0 = display.blit(ob2,(obstacles[0], 582))#PRINTS THE OBSTACLES ON THE GROUNDLINE
        obstacle1 = display.blit(ob3,(obstacles[1], 572))
        obstacle2 = display.blit(ob1,(obstacles[2], 562))
        obstacle3 = display.blit(ob2,(obstacles[3], 582))
        obstacle4 = display.blit(ob1,(obstacles[4], 562))
        obstacle5 = display.blit(ob3,(obstacles[5], 572))
        obstacle6 = display.blit(ob1,(obstacles[6], 562))
        playerhtb = pygame.Rect(x, y, 23 , 43 ) # SHOWING THE HITBOXLINE, WILL BE DELETED!!!
        display.blit(player,(x,y)) #Prints the character 
        
        

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #closes the window from the right corner cross
                running = False
                
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_c: #continues the loop when press c
                    game_loop()
                    return 0
                if event.key == pygame.K_q:#closes the window when press q
                    running = False


        
        move = pygame.key.get_pressed() # Moving left and right
        if move [pygame.K_LEFT] and active == True:
            x -= dx
        if move [pygame.K_RIGHT] and active == True:
            x += dx
    

        keys = pygame.key.get_pressed()  #JUMPING
        if keys[pygame.K_SPACE] and active == True:
            jumping = True
        if jumping:
            y -= y_velocity
            y_velocity -= y_gravity
        if y_velocity < -jump_height:
            jumping = False
            y_velocity = jump_height

        i = random.randint(0, 6) # RANDOMIZES WICH OBSTACLE SPAWNS, THREE DIFFERENT SIZE OF OBSTACLES
        for i in range(len(obstacles)):
            if active:
                obstacles[i] -= obstacle_speed
                if obstacles[i] < 0:
                    obstacles[i] = random.randint(1000, 1700)
                    score += 1
                if (playerhtb.colliderect(obstacle0) or playerhtb.colliderect(obstacle1) or playerhtb.colliderect(obstacle2) or playerhtb.colliderect(obstacle3) 
                or playerhtb.colliderect(obstacle4) or playerhtb.colliderect(obstacle5) or playerhtb.colliderect(obstacle6)):
                    active = False   
            else: 
                message("GAME OVER :( Press C to try again !", red , 200, 200)
        
        
        
              
                      
                    
            
            


        

        pygame.display.update()
        Clock.tick(60)
game_loop()




