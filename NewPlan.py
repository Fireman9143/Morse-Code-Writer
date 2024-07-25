import sys
from os import path
import pygame
from button import Button
from morse import morse_code


class MainGame:
    """Overall class to manage game assets"""

    def __init__(self):
        """Initialize the game"""
        pygame.init()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.bg_color = (0, 0, 0)
        
        #Create game window  
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Learn Morse Code")
        
        self.game_active = False
        self.play_button = Button(self, "Play")
        self.user_text = ""
        self.ditdah = ""
        self.text_font = pygame.font.SysFont("notomono", self.screen_height//20)
        self.morse_font = pygame.font.SysFont("freeserif", self.screen_height//40)
        
    def _check_events(self):
        """Check for key presses to start, enter text, or exit"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    if event.mod & pygame.KMOD_CTRL:
                        sys.exit()
                elif event.key == pygame.K_RETURN:
                    if self.game_active == False:
                        self.game_active = True
                elif event.key == pygame.K_BACKSPACE:
                    self.user_text = self.user_text[:-2]
                elif event.key != pygame.K_SPACE:
                    self.user_text += event.unicode + " "
                    letter = event.unicode.upper()
                    if letter in morse_code and len(morse_code[letter]) > 1:
                            pygame.mixer.Sound(morse_code[letter][1]).play()
                elif event.key == pygame.K_SPACE:
                    self.user_text += " "
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_button.rect.collidepoint(pygame.mouse.get_pos()):
                    self.game_active = True


    def run_game(self):
        """Start game play"""
        while True:
            self._check_events()
            self.convert_morse_code()
            self._update_screen()
            self.clock.tick(60)


    def _update_screen(self):
        """Update the screen"""
        self.screen.fill(self.bg_color)
        if not self.game_active:
            self.play_button.draw_button()
        if self.game_active:
            self.display_user_input((100, 100))  
        pygame.display.flip()
    
     
    def display_user_input(self, pos):
        """Function to wrap lines"""
        user_input = self.user_text.split(" ")
        converted = self.ditdah.split(" ")
        font_x, font_y = self.text_font.size(" ")
        font_x = font_x + 15
        morse_x, morse_y = self.morse_font.size(" ")
        morse_x = morse_x + 6

        x,y = pos
        
        for words in user_input:
            word_surface = self.text_font.render(words, True, 'green')
            word_width, word_height = word_surface.get_size()
            if x + word_width >= self.screen.get_width():
                #If font reaches edge, reset x to the font starting point pos[0] and change y by font height
                x = pos[0]
                y += word_height * 2
            self.screen.blit(word_surface, (x, y))
            x += word_width + font_x

        if len(self.user_text) > 0:
            a,b = pos
            b = word_height + 100
            for dahs in converted:
                code_surface = self.morse_font.render(dahs, True, 'lightblue')
                code_width, _ = code_surface.get_size()
                if a + code_width >= self.screen.get_width():
                    #If font reaches edge, reset x to the font starting point pos[0] and change y by font height
                    a = pos[0]
                    b += word_height * 2
                self.screen.blit(code_surface, (a, b))
                a += code_width + morse_x
                

    def convert_morse_code(self):
        """Take user text, convert to morse"""
        character_pos = []
        morse_letters = []
        
        for num, character in enumerate(self.user_text.upper()):
            #Check to see if the text is already displayed, if not then update lists
            if character in morse_code and num not in character_pos:
                morse_letters.append(morse_code[character][0])
                morse_letters.append(" ")
                character_pos.append(num)
            #Handle spaces that are not in dictionary and add spacing for readability
            elif character == " " and morse_letters[:-2] != " ":
                morse_letters.append("  ")
                character_pos.append(num)
            #Skip anything that's not morse code or a space
            else:
                pass
            
        self.ditdah = "".join(morse_letters)


if __name__ == "__main__":
    game = MainGame()
    game.run_game()