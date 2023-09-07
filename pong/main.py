import pygame,sys
def ball_animation():
    global ball_speedx,ball_speedy
    ball.x+=ball_speedx
    ball.y+=ball_speedy  
    #we are making it a bouncy ball by turning it negative whenever we exceed our width and height
    if ball.top < 0 or ball.bottom >= HEIGHT:
        ball_speedy *= -1
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speedx *= -1  

    if ball.colliderect(player)  or ball.colliderect(oppenent) :
        ball_speedx *= -1      #we tell the ball to change the horizantal (x) direction


pygame.init()


clock=pygame.time.Clock()

WIDTH = 400
HEIGHT = 500
screen =pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("pong")

#game rects
ball=pygame.Rect(WIDTH/2-15,HEIGHT/2-15,30,30)
player=pygame.Rect(WIDTH-20,HEIGHT/2-70,10,140)
oppenent=pygame.Rect(10,HEIGHT/2 -70,10,140)

bg_color=pygame.Color("grey12")
light_grey=(200,200,200)


ball_speedx=7
ball_speedy=7
player_speed = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if pygame.event == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7  
        if pygame.event == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7         
                  


    ball_animation()
    player.y += player_speed
        

    #drawing
    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey,player)  
    pygame.draw.rect(screen,light_grey,oppenent) 
    pygame.draw.ellipse(screen,light_grey,ball)  
    pygame.draw.aaline(screen,light_grey,(WIDTH/2,0), (WIDTH/2,HEIGHT))  #to draw lines that seperate



    pygame.display.flip()
    clock.tick(60)