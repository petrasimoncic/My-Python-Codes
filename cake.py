import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Birthday Cake Maker")

# Colors
BLUE = (135, 206, 250)
WHITE = (255, 255, 255)
PINK = (255, 182, 193)
BROWN = (160, 82, 45)
YELLOW = (255, 223, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
PEACH = (255, 218, 185)
PASTEL_ORANGE = (255, 200, 150)
LIGHT_YELLOW = (255, 239, 170)

# Load assets
def draw_rectangle(color, x, y, width, height):
    pygame.draw.rect(screen, color, (x, y, width, height))

def draw_circle(color, x, y, radius):
    pygame.draw.circle(screen, color, (x, y), radius)

def draw_text(text, x, y, font_size=30, color=BLACK, center=False):
    font = pygame.font.SysFont(None, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y) if center else (x, y))
    screen.blit(text_surface, text_rect)

# Game state
cake_elements = []
selected_element_index = -1
final_design_selected = False

# Main loop
running = True
while running:
    screen.fill(BLUE)
    
    # Draw the cake elements
    for i, element in enumerate(cake_elements):
        color, rect = element['color'], element['rect']
        if element['type'] == 'rect':
            draw_rectangle(color, *rect)
            if element['color'] == RED:  # Add flame to candles
                flame_x = rect[0] + rect[2] // 2
                flame_y = rect[1]
                draw_circle(ORANGE, flame_x, flame_y, 5)
        elif element['type'] == 'circle':
            draw_circle(color, rect[0], rect[1], rect[2])
        
        # Highlight the selected element only if not finalized
        if not final_design_selected and i == selected_element_index:
            if element['type'] == 'rect':
                pygame.draw.rect(screen, WHITE, (rect[0]-2, rect[1]-2, rect[2]+4, rect[3]+4), 2)
            elif element['type'] == 'circle':
                draw_circle(WHITE, rect[0], rect[1], rect[2] + 3)

    # Draw UI buttons
    draw_rectangle(BROWN, 50, 50, 100, 50)  # Add Chocolate Layer
    draw_rectangle(PASTEL_ORANGE, 200, 50, 100, 50)  # Add Vanilla Layer
    draw_rectangle(YELLOW, 350, 50, 100, 50)  # Add Decoration
    draw_rectangle(RED, 500, 50, 100, 50)  # Add Candles
    draw_rectangle(GREEN, 650, 50, 100, 50)  # Select Design Button
    draw_rectangle(PEACH, 50, 120, 100, 50)  # Frosting
    draw_rectangle(LIGHT_YELLOW, 200, 120, 100, 50)  # Base
    draw_text("Finalize", 700, 75, font_size=25, color=BLACK, center=True)
    draw_text("Frosting", 100, 145, font_size=20, color=BLACK, center=True)
    draw_text("Vanilla", 250, 145, font_size=20, color=BLACK, center=True)
    draw_text("Chocolate", 100, 75, font_size=20, color=BLACK, center=True)
    draw_text("Base", 250, 75, font_size=20, color=BLACK, center=True)
    draw_text("Decoration", 400, 75, font_size=20, color=BLACK, center=True)
    draw_text("Candles", 550, 75, font_size=20, color=BLACK, center=True)

    if final_design_selected:
        draw_text("Happy Birthday, Beryl!", screen_width // 2, screen_height // 2, font_size=50, color=WHITE, center=True)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if event.button == 1:  # Left click to add or finalize design
                if 50 <= mouse_x <= 150 and 50 <= mouse_y <= 100:
                    cake_elements.append({"type": "rect", "color": BROWN, "rect": [screen_width // 2 - 100, screen_height - 100, 200, 40]})
                elif 200 <= mouse_x <= 300 and 50 <= mouse_y <= 100:
                    cake_elements.append({"type": "rect", "color": PASTEL_ORANGE, "rect": [screen_width // 2 - 110, screen_height - 140, 220, 20]})
                elif 350 <= mouse_x <= 450 and 50 <= mouse_y <= 100:
                    cake_elements.append({"type": "circle", "color": YELLOW, "rect": [screen_width // 2, screen_height - 160, 15]})
                elif 500 <= mouse_x <= 600 and 50 <= mouse_y <= 100:
                    cake_elements.append({"type": "rect", "color": RED, "rect": [screen_width // 2 - 5, screen_height - 200, 10, 40]})
                elif 650 <= mouse_x <= 750 and 50 <= mouse_y <= 100:
                    final_design_selected = True
                elif 50 <= mouse_x <= 150 and 120 <= mouse_y <= 170:
                    cake_elements.append({"type": "rect", "color": PEACH, "rect": [screen_width // 2 - 60, screen_height - 180, 120, 30]})
                elif 200 <= mouse_x <= 300 and 120 <= mouse_y <= 170:
                    cake_elements.append({"type": "rect", "color": LIGHT_YELLOW, "rect": [screen_width // 2 - 70, screen_height - 210, 140, 20]})

        elif event.type == pygame.KEYDOWN and not final_design_selected:
            if event.key == pygame.K_TAB:
                selected_element_index = (selected_element_index + 1) % len(cake_elements)
            if selected_element_index != -1:
                if event.key == pygame.K_UP:
                    cake_elements[selected_element_index]['rect'][1] -= 10
                elif event.key == pygame.K_DOWN:
                    cake_elements[selected_element_index]['rect'][1] += 10
                elif event.key == pygame.K_LEFT:
                    cake_elements[selected_element_index]['rect'][0] -= 10
                elif event.key == pygame.K_RIGHT:
                    cake_elements[selected_element_index]['rect'][0] += 10

    pygame.display.flip()

pygame.quit()
sys.exit()
