import pygame
import random

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Définition des constantes pour la fenêtre
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Classe pour le poisson
class Fish(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 20])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(SCREEN_HEIGHT - self.rect.height)
        self.speed_x = random.randrange(1, 5)
        self.speed_y = random.randrange(1, 5)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.right > SCREEN_WIDTH or self.rect.left < 0:
            self.speed_x = -self.speed_x
        if self.rect.bottom > SCREEN_HEIGHT or self.rect.top < 0:
            self.speed_y = -self.speed_y

# Classe pour la nourriture
class Food(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([5, 5])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_y = -2

    def update(self):
        self.rect.y += self.speed_y

# Initialisation de la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Aquarium")

all_sprites = pygame.sprite.Group()
fish_sprites = pygame.sprite.Group()
food_sprites = pygame.sprite.Group()

# Création des poissons
for i in range(5):
    fish = Fish()
    all_sprites.add(fish)
    fish_sprites.add(fish)

clock = pygame.time.Clock()
running = True

# Boucle principale
while running:
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Ajout de la nourriture au clic de la souris
            food = Food(event.pos[0], event.pos[1])
            all_sprites.add(food)
            food_sprites.add(food)

    # Mise à jour et affichage des poissons et de la nourriture
    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
