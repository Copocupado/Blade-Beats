import sys

import pygame.time

from Backend.RankingDAO import RankingsDAO
from app import Game
from Config.load_assets import AssetLoader
from Config.window_config import *


class Boot:
    def __init__(self, camera):
        self.camera = camera
        self.asset_loader = None

        self.font = pygame.font.Font(None, 100)
        self.text_surface = self.font.render("Blade Beats", True, (255, 255, 255))

    def run(self):
        self.asset_loader = AssetLoader()

        self.image = self.asset_loader.assets['logo']
        self.text_rect = self.image.get_rect(center=(self.camera.internal_surface.get_width() // 2, self.camera.internal_surface.get_height() // 2))

        self.text_rect_blade_beats = self.text_surface.get_rect(center=(self.camera.internal_surface.get_width() // 2, self.text_rect.bottom + 20))

        alpha = 255
        start_time = pygame.time.get_ticks()
        while True:
            CLOCK.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.camera.internal_surface.fill(BLACK)

            elapsed_time = pygame.time.get_ticks() - start_time
            if elapsed_time > 0:
                faded_image_surface = self.image.copy()
                faded_image_surface.set_alpha(alpha)

                faded_text_surface = self.text_surface.copy()
                faded_text_surface.set_alpha(alpha)

                self.camera.internal_surface.blit(faded_image_surface, self.text_rect)
                self.camera.internal_surface.blit(faded_text_surface, self.text_rect_blade_beats)

                if elapsed_time > 2000:
                    alpha = max(0, alpha - 2)

                if alpha == 0 and self.asset_loader is not None:
                    return self.asset_loader

            Game.blit_screen(self.camera)
            pygame.display.flip()
