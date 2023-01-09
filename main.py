import pygame



pygame.init()

Clock = pygame.time.Clock()

#Window size
width = 1000
height = 800

red = (255,0,0)
green = (0, 255, 0)
blue = (0,0,255)

display = pygame.display.set_mode((width,height))
pygame.display.set_caption("EndlessRunner")

player = pygame.image.load("steve.png") #player
font_style = pygame.font.SysFont("Arial", 25)


def message(msg, color, mx, my):  
    mesg = font_style.render(msg, True, color)
    display.blit(mesg,[mx, my])



def game_loop():
    running = True
    x = 150
    y = 600
    dx = 0.5
    dy = 0.5
    
    jumping = False
    y_gravity = 1
    jump_height = 20
    y_velocity = jump_height


    while running:
        display.fill((0,0,0))



        message("Press Q to quit :)", red , 0, 10)
        display.blit(player,(x,y)) #Prints the character 
        pygame.display.update()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #closes the window from the right corner cross
                running = False
                
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_q:#closes the window when press q
                    running = False
                if event.key == pygame.K_c: #continues the loop when press c
                    game_loop()

        keys = pygame.key.get_pressed()  #JUMPING
        if keys[pygame.K_SPACE]:
            jumping = True
        if jumping:
            y -= y_velocity
            y_velocity -= y_gravity
            if y_velocity < -jump_height:
                jumping = False
                y_velocity = jump_height

        Clock.tick(60)

         

    

game_loop()




