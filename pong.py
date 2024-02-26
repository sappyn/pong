import pygame
import random

SCREEN_SIZE_X = 1000
SCREEN_SIZE_Y = 800

L_PADDLE_WIDTH = 25
L_PADDLE_HEIGHT = 150
R_PADDLE_WIDTH = 25
R_PADDLE_HEIGHT = 150
PADDLE_SPEED = 7

BALL_ORIGINAL_X = 500
BALL_ORIGINAL_Y = 300
BALL_ORIGINAL_X_SPEED = 5
BALL_ORIGINAL_Y_SPEED = 5
BALL_WIDTH = 20
BALL_HEIGHT = 20

def intersects(px1, py1, pw, ph, bx1, by1, bw, bh):
    bx2 = bx1 + bw
    by2 = by1 + bh
    px2 = px1 + pw
    py2 = py1 + ph

    if (bx2 > px1 and bx1 < px2 and by2 > py1 and by1 < py2):
        return True
    return False

def main():
    Lscore = 0
    Rscore = 0
    LpaddleX = 10
    LpaddleY = 300
    RpaddleX = 965
    RpaddleY = 300
    ballX = BALL_ORIGINAL_X
    ballY = BALL_ORIGINAL_Y
    ballXSpeed = BALL_ORIGINAL_X_SPEED
    ballYSpeed = BALL_ORIGINAL_Y_SPEED

    pygame.init()
    pygame.display.set_caption('Pong')

    screen = pygame.display.set_mode((SCREEN_SIZE_X, SCREEN_SIZE_Y))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        screen.fill("black")

        # Rendering START
        pygame.draw.rect(screen, "white", pygame.Rect(LpaddleX, LpaddleY, L_PADDLE_WIDTH, L_PADDLE_HEIGHT)) # Left Paddle
        pygame.draw.rect(screen, "white", pygame.Rect(RpaddleX, RpaddleY, R_PADDLE_WIDTH, R_PADDLE_HEIGHT)) # Right Paddle
        pygame.draw.rect(screen, "white", pygame.Rect(ballX, ballY, BALL_WIDTH, BALL_HEIGHT)) # Ball

        # Rendering END

        # Make Ball Move
        ballX += ballXSpeed
        ballY += ballYSpeed

        # Ball Contraints
        if (ballX <= 0 or ballX >= SCREEN_SIZE_X - 15):
            ballX = BALL_ORIGINAL_X
            ballY = BALL_ORIGINAL_Y
            ballXSpeed = BALL_ORIGINAL_X_SPEED
            ballYSpeed = BALL_ORIGINAL_Y_SPEED

            # Randomize direction it goes
            direction = random.randint(1, 3)
            if (direction == 1):
                ballXSpeed *= -1
                ballYSpeed *= -1

        if (ballY <= 0 or ballY >= SCREEN_SIZE_Y - 15):
            ballYSpeed *= -1
        
        # Check if ball hits paddle
        touchingLpaddle = intersects(LpaddleX, LpaddleY, L_PADDLE_WIDTH, L_PADDLE_HEIGHT, ballX, ballY, BALL_WIDTH, BALL_HEIGHT)
        if (touchingLpaddle == True):
            if (ballX < LpaddleX + L_PADDLE_WIDTH):
                ballX = LpaddleX + L_PADDLE_WIDTH
            
            ballXSpeed *= -1

        touchingRpaddle = intersects(RpaddleX, RpaddleY, R_PADDLE_WIDTH, R_PADDLE_HEIGHT, ballX, ballY, BALL_WIDTH, BALL_HEIGHT)
        if (touchingRpaddle == True):
            if (ballX + BALL_WIDTH > RpaddleX):
                ballX = RpaddleX - BALL_WIDTH
            
            ballXSpeed *= -1

        if (touchingLpaddle == True or touchingRpaddle == True): # Increase ball speed when it hits a paddle for difficulty
            if (ballXSpeed > 0):
                ballXSpeed += 0.5
            else:
                ballXSpeed -= 0.5
            
            if (ballYSpeed > 0):
                ballYSpeed += 0.5
            else:
                ballYSpeed -= 0.5

        # On Key Pressed
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_w]):
            LpaddleY -= PADDLE_SPEED
        if (keys[pygame.K_s]):
            LpaddleY += PADDLE_SPEED

        if (keys[pygame.K_UP]):
            RpaddleY -= PADDLE_SPEED
        if (keys[pygame.K_DOWN]):
            RpaddleY += PADDLE_SPEED

        # Paddle Constraints
        if (LpaddleY <= 0):
            LpaddleY = 0
        elif (LpaddleY >= SCREEN_SIZE_Y - 150):
            LpaddleY = SCREEN_SIZE_Y - 150

        if (RpaddleY <= 0):
            RpaddleY = 0
        elif (RpaddleY >= SCREEN_SIZE_Y - 150):
            RpaddleY = SCREEN_SIZE_Y - 150

        pygame.display.flip()
        clock.tick(60) # 60 FPS
    
    pygame.quit()

if __name__ == "__main__":
    main()