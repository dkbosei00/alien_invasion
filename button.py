import pygame.font

class Button:
    '''Class for game button'''

    def __init__(self, ai_game, msg) -> None:
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set dimensions for the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Create button rect and center at the middle of the screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Prep button message once
        self._prep_message(msg)

    def _prep_message(self, message):
        # Turn message into rendered image and center text on the button
        self.message_image = self.font.render(message, True, self.text_color, self.button_color)

        self.message_item_rect = self.message_image.get_rect()
        self.message_item_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button then draw message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.message_image, self.message_item_rect)