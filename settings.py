import sys
import pygame

class Settings:
    """A class to manage game settings"""


    def __init__(self) -> None:
        """Initialize game settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.text_font = pygame.font.Font(None, 120)
        self.morse_font = pygame.font.Font(None, 100)
        