# Pong Game

import pygame, time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 850, 650
DARK_PURPLE = (48, 25, 52)
BALL_SPEED = 8
PADDLE_SPEED = 10
TIME_LIMIT = 45

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Class for the paddles
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 100)

    def move(self, dy):
        self.rect.y += dy * PADDLE_SPEED
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

# Class for the ball
class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 15, 15)
        self.dx = BALL_SPEED
        self.dy = BALL_SPEED

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.dy = -self.dy

# Main function
def main():
    clock = pygame.time.Clock()
    paddle1 = Paddle(30, HEIGHT // 2 - 50)
    paddle2 = Paddle(WIDTH - 40, HEIGHT // 2 - 50)
    ball = Ball()
    score1, score2 = 0, 0
    start_time = time.time()

    while True:
        screen.fill(DARK_PURPLE)
        elapsed_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1.move(-1)
        if keys[pygame.K_s]:
            paddle1.move(1)
        if keys[pygame.K_UP]:
            paddle2.move(-1)
        if keys[pygame.K_DOWN]:
            paddle2.move(1)

        ball.move()

        if ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
            ball.dx = -ball.dx

        if ball.rect.left <= 0:
            score2 += 1
            ball = Ball()
        if ball.rect.right >= WIDTH:
            score1 += 1
            ball = Ball()

        # Display score and time limit
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"{score1} - {score2}", True, (255, 255, 255))
        time_text = font.render(f"Time: {int(TIME_LIMIT - elapsed_time)}", True, (255, 255, 255))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))
        screen.blit(time_text, (WIDTH - 150, 20))

        if elapsed_time >= TIME_LIMIT:
            break

        pygame.draw.rect(screen, (255, 255, 255), paddle1.rect)
        pygame.draw.rect(screen, (255, 255, 255), paddle2.rect)
        pygame.draw.ellipse(screen, (255, 255, 255), ball.rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()