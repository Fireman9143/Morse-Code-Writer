import pygame.font

class Button:
    """A class to build game buttons"""

    def __init__(self, morse_game, msg) -> None:
        """Initialize button attributes"""
        self.screen = morse_game.screen
        self.screen_rect = self.screen.get_rect()
        self.screen_width, self.screen_height = self.screen.get_size()
        #Set dimensions and properties of button
        self.width, self.height = self.screen_width/3, self.screen_height/3
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 200)
        #Build buttons rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        #The button only needs to be pressed once
        self._prep_msg(msg)


    def _prep_msg(self, msg):
        """Turn text into rendered image and center on button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        """Draw blank button then draw message"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)