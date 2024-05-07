import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
PLAYER_SPEED = 10
ENEMY_SIZE = 2
ENEMY_SPEED = 19
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)

# Create the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Karlson-like Game")

# Player attributes
player = pygame.Rect(WIDTH // 2 - PLAYER_SIZE // 2, HEIGHT - PLAYER_SIZE - 20, PLAYER_SIZE, PLAYER_SIZE)

# Enemy attributes
enemies = []
enemy_spawn_timer = 0

# Score
score = 0

# Buttons
play_button = pygame.Rect(50, 100, 100, 50)
quit_button = pygame.Rect(50, 200, 100, 50)

# Game loop
running = True
clock = pygame.time.Clock()
game_active = False

while running:
    window.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if play_button.collidepoint(mouse_pos):
                game_active = True
            if quit_button.collidepoint(mouse_pos):
                running = False

    if game_active:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and player.x < WIDTH - PLAYER_SIZE:
            player.x += PLAYER_SPEED

        # Enemy spawning logic
        enemy_spawn_timer += 1
        if enemy_spawn_timer == 60:
            enemy_spawn_timer = 0
            enemy = pygame.Rect(random.randint(0, WIDTH - ENEMY_SIZE), 0, ENEMY_SIZE, ENEMY_SIZE)
            enemies.append(enemy)

        # Move enemies and remove when off screen
        for enemy in enemies:
            enemy.y += ENEMY_SPEED
            if enemy.y > HEIGHT:
                enemies.remove(enemy)
                score += 1

        # Check for collisions
        for enemy in enemies:
            if player.colliderect(enemy):
                # Game over scenario
                running = False

        # Draw player
        pygame.draw.rect(window, RED, player)

        # Draw enemies
        for enemy in enemies:
            pygame.draw.rect(window, RED, enemy)

        # Draw score
        score_text = FONT.render(f"Score: {score}", True, BLACK)
        window.blit(score_text, (WIDTH - 150, 20))

    else:
        # Draw buttons
        pygame.draw.rect(window, RED, play_button)
        pygame.draw.rect(window, RED, quit_button)

        play_text = FONT.render("Play", True, BLACK)
        quit_text = FONT.render("Quit", True, BLACK)
        window.blit(play_text, (play_button.x + 20, play_button.y + 10))
        window.blit(quit_text, (quit_button.x + 20, quit_button.y + 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
