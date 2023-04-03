import pygame
import time

pygame.init() #initialize all imported pygame modules by returning a tuple
pygame.display.set_caption('Snake game, created by devanshi')

# initialize color variables
blue = (0,0,225)
red = (255,0,0)
white = (255,255,255)
green = (57,255,20)
black = (0,0,0)

dis_height = 500
dis_width = 500
dis = pygame.display.set_mode((dis_height,dis_width)) #create surface using a tuple/list as a parameter
snake_block = 10
snake_speed = 20
clock = pygame.time.Clock() #limits maximum frame rate of game

font_style = pygame.font.SysFont(None, 50)

def message(msg,color):
    fmtt_msg = font_style.render(msg, True, color)
    msg_width, msg_height = fmtt_msg.get_size()
    x = (dis_width / 2) - (msg_width / 2)
    y = (dis_height / 2) - (msg_height / 2)
    dis.blit(fmtt_msg, (x, y))


# def snakeGameLoop(): 
    game_over = False
    game_close = False

    # (x, y) coordinates of the top-left corner of the rectangle (snake)
    x1 = dis_width/2
    y1 = dis_height/2

    # Since the snake is moving, its coordinates update as well : 
    x1_change = 0
    y1_change = 0

    # FOOD
    # foodx = random.randrange(0,)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            ## MOVING THE SNAKE
            # This uses key events in the KEYDOWN class : K_UP, K_DOWN, K_LEFT, K_RIGHT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change -= 10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change += 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change += 10
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change -= 10

        ## SETTING BOUNDARIES
        if x1 <= 0 or x1 >= dis_width or y1 <= 0 or y1 >= dis_height:
            game_over = True

        ## CREATING THE SNAKE
        x1 += x1_change # positon : abscissa
        y1 -= y1_change # postion : ordinate
        dis.fill(black)
        pygame.draw.rect(dis, green, [x1,y1,snake_block,snake_block]) # use draw.rect func to create snake
        # Last two values are the width and height of the rectangle.
        pygame.display.update() #updates the screen
        clock.tick(snake_speed)

    #  

    message("Game over", red)
    pygame.display.update()
    time.sleep(2) #delays execution of code by 2 seconds
    pygame.quit()
    quit()