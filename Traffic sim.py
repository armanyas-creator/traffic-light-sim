import sys
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smart Traffic Signal Simulator")
clock = pygame.time.Clock()

CHANGE_SIGNAL_EVENT = pygame.USEREVENT + 1

class Car(pygame.sprite.Sprite):

  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.Surface((60, 30))
    self.image.fill((255, 0, 0))
    self.rect = self.image.get_rect(topleft=(x, y))
    self.speed = 3

  def update(self):
    self.rect.x += self.speed
    if self.rect.right >= 700 and self.speed > 0:
      self.speed = 0
      pygame.event.post(pygame.event.Event(CHANGE_SIGNAL_EVENT))


car = Car(50, 185)
all_sprites = pygame.sprite.Group(car)

running = True
signal_color = (255, 0, 0)

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == CHANGE_SIGNAL_EVENT:
      car.image.fill((0, 255, 0))
      signal_color = (0, 255, 0)
      car.speed = 3

  screen.fill((50, 50, 50))

  all_sprites.update()
  all_sprites.draw(screen)

  pygame.display.flip()
  clock.tick(60)

pygame.quit()
sys.exit()
