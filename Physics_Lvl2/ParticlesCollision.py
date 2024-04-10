import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Classes
class Particle(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(center=pos)
        self.velocity = pygame.Vector2(random.uniform(-2, 2), random.uniform(-2, 2))

    def update(self):
        self.rect.move_ip(self.velocity)

        # Collision detection with screen boundaries
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.velocity.x *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.velocity.y *= -1

# Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

particles = pygame.sprite.Group()
for _ in range(20):
    particles.add(Particle((random.randint(0, WIDTH), random.randint(0, HEIGHT))))

# Main loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    particles.update()

    # Collision detection between particles
    for p in particles:
        collisions = pygame.sprite.spritecollide(p, particles, False)
        for other in collisions:
            if other != p:
                distance = pygame.Vector2(other.rect.center) - pygame.Vector2(p.rect.center)
                if distance.length() < 20:
                    direction = distance.normalize()
                    p.velocity += direction
                    other.velocity -= direction

    particles.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
