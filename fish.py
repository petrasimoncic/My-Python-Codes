import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 2000
SCREEN_HEIGHT = 1800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fish the Fish")

# Colors
BACKGROUND_BLUE = (135, 206, 235)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

# Game variables
fish_size = (50, 30)
fish_speed = 1
fish_list = []
score = 0
clock = pygame.time.Clock()

# Functions
def create_fish():
    x = random.randint(0, SCREEN_WIDTH - fish_size[0])
    y = random.randint(0, SCREEN_HEIGHT - fish_size[1])
    direction = random.choice([1, -1])
    return [x, y, direction]

def draw_corals():
    pygame.draw.rect(screen, (255, 160, 122), (50, SCREEN_HEIGHT - 100, 100, 100))
    pygame.draw.rect(screen, (255, 127, 80), (650, SCREEN_HEIGHT - 150, 120, 150))

def draw_fish(fish):
    pygame.draw.ellipse(screen, ORANGE, (fish[0], fish[1], fish_size[0], fish_size[1]))
    pygame.draw.polygon(screen, BLUE, [(fish[0], fish[1] + fish_size[1] // 2),
                                       (fish[0] - 20 * fish[2], fish[1]),
                                       (fish[0] - 20 * fish[2], fish[1] + fish_size[1])])

def increase_fish_speed():
    global fish_speed
    fish_speed += 0.01

def move_fish(fish):
    fish[0] += fish_speed * fish[2]

def is_fish_clicked(fish, pos):
    return (fish[0] <= pos[0] <= fish[0] + fish_size[0] and
            fish[1] <= pos[1] <= fish[1] + fish_size[1])

def check_game_over(fish):
    return fish[0] < -fish_size[0] or fish[0] > SCREEN_WIDTH

# Game loop
running = True
spawn_timer = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_timer, 1500)

while running:
    screen.fill(BACKGROUND_BLUE)

    draw_corals()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == spawn_timer:
            fish_list.append(create_fish())
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for fish in fish_list[:]:
                if is_fish_clicked(fish, event.pos):
                    fish_list.remove(fish)
                    score += 1

    for fish in fish_list[:]:
        move_fish(fish)
        draw_fish(fish)
        if check_game_over(fish):
            print(f"Game Over! Final Score: {score}")
            pygame.quit()
            sys.exit()

    # Draw score
    font = pygame.font.SysFont(None, 50)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
