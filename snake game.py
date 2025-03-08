import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Tamaño de la serpiente y la comida
BLOCK_SIZE = 20

# Reloj para controlar la velocidad
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

def reset_game():
    return [(100, 100), (80, 100), (60, 100)], (random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                                                random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE), 0, BLOCK_SIZE, 0

running = True
while running:
    snake, food, score, dx, dy = reset_game()
    game_over = False
    
    while not game_over:
        screen.fill(BLACK)
        
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_over = True
        
        # Controles
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and dy == 0:
            dx, dy = 0, -BLOCK_SIZE
        if keys[pygame.K_DOWN] and dy == 0:
            dx, dy = 0, BLOCK_SIZE
        if keys[pygame.K_LEFT] and dx == 0:
            dx, dy = -BLOCK_SIZE, 0
        if keys[pygame.K_RIGHT] and dx == 0:
            dx, dy = BLOCK_SIZE, 0
        
        # Mover la serpiente
        new_head = (snake[0][0] + dx, snake[0][1] + dy)
        snake.insert(0, new_head)
        
        # Comprobar si ha comido la comida
        if new_head == food:
            score += 1
            food = (random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                    random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)
        else:
            snake.pop()
        
        # Comprobar colisiones
        if (new_head[0] < 0 or new_head[0] >= WIDTH or
                new_head[1] < 0 or new_head[1] >= HEIGHT or
                new_head in snake[1:]):
            game_over = True
        
        # Dibujar comida y serpiente
        pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))
        
        # Mostrar puntuación
        score_text = font.render(f"Puntos: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
        clock.tick(10)

pygame.quit()
