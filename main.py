import pygame
import random

# Game constants
WIDTH, HEIGHT = 800, 600
FPS = 30
BLOCK_SIZE = 40

# Colors
green = (0, 255, 0)
sky_blue = (135, 206, 250)
brown = (139, 69, 19)

class Block:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)

class MinecraftGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.blocks = []
        self.running = True
        self.populate_blocks()

    def populate_blocks(self):
        for x in range(0, WIDTH, BLOCK_SIZE):
            for y in range(HEIGHT - BLOCK_SIZE, HEIGHT, BLOCK_SIZE):
                if random.choice([True, False]):
                    self.blocks.append(Block(x, y))

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass  # Game logic will go here

    def draw(self):
        self.screen.fill(sky_blue)
        for block in self.blocks:
            pygame.draw.rect(self.screen, brown, block.rect)
        pygame.display.flip()

if __name__ == '__main__':
    game = MinecraftGame()
    game.run()
    pygame.quit()