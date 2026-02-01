"""Ship sprite for the Aliens game."""

from pathlib import Path

import pygame


class Ship:
    def __init__(self, screen: pygame.Surface) -> None:
        """Load the ship image and set its starting position."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        base_path = Path(__file__).parent / "images"
        img_path = base_path / "ship-640-548.png"
        fallback_bmp = base_path / "ship-640-548.bmp"

        try:
            loaded = pygame.image.load(str(img_path)).convert_alpha()
        except pygame.error:
            loaded = pygame.image.load(str(fallback_bmp)).convert_alpha()

        # Scale down to a small footprint (keep aspect ratio).
        target_width = 80
        scale = target_width / loaded.get_width()
        target_height = int(loaded.get_height() * scale)
        self.image = pygame.transform.smoothscale(loaded, (target_width, target_height))

        self.rect = self.image.get_rect()

        # Start each new ship near the bottom center of the screen with a small margin.
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 10

    def blitme(self) -> None:
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
