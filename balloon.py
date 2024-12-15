import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Balloon Pop Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALLOON_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (255, 20, 147)]

# Game variables
balloons = []
confetti_particles = []
score = 0
font = pygame.font.SysFont("Arial", 50)

# Balloon class
class Balloon(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.color = color
        self.rect = pygame.Rect(x, y, 60, 80)
        self.speed = random.randint(1, 2)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            balloons.remove(self)

    def draw(self, surface):
        # Draw balloon body
        pygame.draw.ellipse(surface, self.color, self.rect)
        # Draw string
        pygame.draw.line(surface, BLACK, (self.rect.centerx, self.rect.bottom), 
                         (self.rect.centerx, self.rect.bottom + 50), 2)

# Confetti class
class Confetti:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.speed_x = random.uniform(-2, 2)
        self.speed_y = random.uniform(-2, 2)
        self.size = random.randint(3, 7)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Confetti bounce effect
        if self.x <= 0 or self.x >= SCREEN_WIDTH:
            self.speed_x *= -1
        if self.y <= 0 or self.y >= SCREEN_HEIGHT:
            self.speed_y *= -1

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)

# Create balloons
def create_balloon():
    x = random.randint(50, SCREEN_WIDTH - 100)
    y = SCREEN_HEIGHT
    color = random.choice(BALLOON_COLORS)
    balloon = Balloon(x, y, color)
    balloons.append(balloon)

# Create confetti
def create_confetti():
    for _ in range(300):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        color = random.choice(BALLOON_COLORS)
        confetti_particles.append(Confetti(x, y, color))

# Main game loop
running = True
clock = pygame.time.Clock()
confetti_active = False

while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Balloon popping detection
        if event.type == pygame.MOUSEBUTTONDOWN:
            for balloon in balloons:
                if balloon.rect.collidepoint(event.pos):
                    balloons.remove(balloon)
                    score += 1

    # Create new balloons
    if random.randint(0, 50) == 0:
        create_balloon()

    # Update and draw balloons
    for balloon in balloons:
        balloon.update()
        balloon.draw(screen)

    # Trigger confetti
    if score >= 5 and not confetti_active:
        create_confetti()
        confetti_active = True

    # Update and draw confetti
    if confetti_active:
        for particle in confetti_particles:
            particle.move()
            particle.draw(screen)

        text = font.render("Happy Birthday!", True, BLACK)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
