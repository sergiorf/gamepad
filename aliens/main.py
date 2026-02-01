"""Minimal Pygame window for the Aliens project from *Crash Course in Python*.

Run with `python main.py`. Closes when you press the close box or Escape.
"""

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

from settings import Settings


def run() -> None:
    settings = Settings()

    pygame.init()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Aliens")

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

        screen.fill(settings.bg_color)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    run()
