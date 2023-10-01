import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize clock
clock = pygame.time.Clock()

# Initialize Snake
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_direction = (0, 0)
snake_speed = 10

# Initialize Food
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def move_snake(snake, direction):
    head = snake[-1]
    new_head = (head[0] + direction[0], head[1] + direction[1])
    snake.append(new_head)
    if new_head == food:
        generate_food()
    else:
        snake.pop(0)

def generate_food():
    global food
    food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if snake_direction != (0, 1):
                    snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                if snake_direction != (0, -1):
                    snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT:
                if snake_direction != (1, 0):
                    snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                if snake_direction != (-1, 0):
                    snake_direction = (1, 0)

    move_snake(snake, snake_direction)

    # Check for collisions
    if snake[-1] in snake[:-1] or \
            snake[-1][0] < 0 or snake[-1][0] >= GRID_WIDTH or \
            snake[-1][1] < 0 or snake[-1][1] >= GRID_HEIGHT:
        pygame.quit()
        sys.exit()

    # Clear the screen
    screen.fill(WHITE)

    # Draw the snake and food
    draw_snake(snake)
    draw_food(food)

    pygame.display.flip()

    # Control game speed
    clock.tick(snake_speed)
