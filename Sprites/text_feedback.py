import pygame.sprite


class TextFeedback(pygame.sprite.Sprite):
    def __init__(self, *groups, position, text, color):
        super().__init__(*groups)

        font = pygame.font.Font(None, 30)

        self.image = font.render(text, True, color)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect(midbottom=position)
        self.alpha = 255

    def update(self, *args, **kwargs):
        self.rect.y -= 1
        self.alpha -= 5
        if self.alpha <= 0:
            self.kill()
        else:
            self.image.set_alpha(self.alpha)
