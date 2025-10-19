import pygame
import sys

# Exemplo de mapa simples (# = parede, espaço = chão)
grid = [
    "#####################",
    "#                   #",
    "#  ####  ####  #### #",
    "#                   #",
    "#####################",
]

# Ajustar ROWS e COLS automaticamente
ROWS = len(grid)
COLS = len(grid[0])
TILE_SIZE = 24

WIDTH = COLS * TILE_SIZE
HEIGHT = ROWS * TILE_SIZE

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# carregar imagem da parede
walls_img_full = pygame.image.load("assets/images/walls.png").convert_alpha()
# escalar para o tamanho do mapa
walls_img_full = pygame.transform.scale(walls_img_full, (WIDTH, HEIGHT))

# criar tile de chão simples (preto)
floor_img = pygame.Surface((TILE_SIZE, TILE_SIZE))
floor_img.fill((0, 0, 0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # desenhar mapa
    for r in range(ROWS):
        for c in range(COLS):
            # desenha chão primeiro
            screen.blit(floor_img, (c * TILE_SIZE, r * TILE_SIZE))
            # desenha parede usando a imagem completa do mapa
            if grid[r][c] == '#':
                # recortar o tile correto da imagem escalada
                tile_rect = pygame.Rect(c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                screen.blit(walls_img_full, (c * TILE_SIZE, r * TILE_SIZE), tile_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
