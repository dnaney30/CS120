import random
import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 20
TARGET_SPEED = 10
FPS = 60
TIME_LIMIT = 10  # seconds

# Initialize Pygame
pygame.init()

# Game Class
class Game:
    def __init__(self):
        self.score = 0
        self.timer = TIME_LIMIT
        self.player = Player()
        self.target = Target()
        self.font = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.player.update()
        self.target.update()
        self.check_collision()
        self.update_timer()

    def draw(self):
        screen.fill((255, 255, 255))
        self.player.draw(screen)
        self.target.draw(screen)
        self.draw_score()
        self.draw_timer()
        pygame.display.flip()

    def check_collision(self):
        if self.player.rect.colliderect(self.target.rect):
            self.score += 1
            self.target.reset_position()
            self.play_collision_sound()

    def update_timer(self):
        if self.timer > 0:
            self.timer -= 1 / 60  # Decrease timer
        else:
            self.running = False  # End game

    def draw_score(self):
        score_label = self.font.render(f'Score: {self.score}', True, (0, 0, 0))
        screen.blit(score_label, (10, 10))

    def draw_timer(self):
        timer_label = self.font.render(f'Time: {int(self.timer)}', True, (0, 0, 0))
        screen.blit(timer_label, (SCREEN_WIDTH - 100, 10))

    def play_collision_sound(self):
        # Placeholder for sound effect
        pass

# Player Class
class Player:
    def __init__(self):
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_UP]:
            self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            self.rect.y += PLAYER_SPEED
        self.boundary_check()

    def boundary_check(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Target Class
class Target:
    def __init__(self):
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(random.randint(0, SCREEN_WIDTH), 0))
        self.direction = 1

    def update(self):
        self.rect.y += TARGET_SPEED * self.direction
        if self.rect.top > SCREEN_HEIGHT or self.rect.bottom < 0:
            self.reset_position()

    def reset_position(self):
        self.rect.x = random.randint(0, SCREEN_WIDTH)
        self.rect.y = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Main Execution
if __name__ == "__main__":
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Game")
    game = Game()
    game.run()
    pygame.quit()