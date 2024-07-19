import sys
import pygame
from settings import Settings
from button import Button
from morse import morse_code


class MainGame:
    """Overall class to manage game assets"""

    def __init__(self):
        """Initialize the game"""
        #Initiatlize Pygame
        pygame.init()
        #Set frame rate to work same on most systems
        self.clock = pygame.time.Clock()
        #Create settings class instance
        self.settings = Settings()
        #Create game window  
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Learn Morse Code")
        #Start game in inactive state
        self.game_active = False
        #make a play button
        self.play_button = Button(self, "Play")
        #User input variable
        self.user_text = ""
        #import morse dictionary
        self.morse = morse_code
        self.ditdah = ""

        
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
                    elif self.game_active == True:
                        pass
                elif event.key == pygame.K_BACKSPACE:
                    self.user_text = self.user_text[:-1]
                else:
                    self.user_text += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_button.rect.collidepoint(pygame.mouse.get_pos()):
                    self.game_active = True


    def run_game(self):
        """Start game play"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)


    def _update_screen(self):
        """Update the screen"""
        #Redraw the screen each time through the loop
        self.screen.fill(self.settings.bg_color)
        #Draw the play button
        if not self.game_active:
            self.play_button.draw_button()
        if self.game_active:
            self.display_user_input()  
        pygame.display.flip()
    
     
    def display_user_input(self):
        """Draw the box, add text, resize the box to width of text"""
        #Setup text font and render text based on user_text init variable
        text_surface = self.settings.text_font.render(self.user_text, True, ("green"))
        #Setup code font and render morse based on ditdah init variable
        morse_surface = self.settings.morse_font.render(self.ditdah, True, ("white"))
        #Check width of morse code line then move box based on line
        self.text_rect, self.morse_rect = self.make_line(morse_surface.get_width())
        #Draw text and resize box
        self.screen.blit(text_surface, (self.text_rect.x + 5, self.text_rect.y + 5))
        self.text_rect.w = max(10, text_surface.get_width() + 10)
        #Convert morse code so self.ditdah list is converted to string for next part
        self.convert_morse_code()
        #Draw morse code and resize box
        self.screen.blit(morse_surface, (self.morse_rect.x + 5, self.morse_rect.y + 5))
        self.morse_rect.w = max(10, morse_surface.get_width() + 10)
        #Draw each instance
        pygame.draw.rect(self.screen, pygame.Color("lightskyblue"), self.text_rect, 2)
        pygame.draw.rect(self.screen, pygame.Color("lightskyblue"), self.morse_rect, 4)

    def make_line(self, line_width):
        """Check for line and make new lines if screen edge reached"""
        #Set the box x, y coordinates
        self.text_rect_x, self.text_rect_y = 100, 200
        self.morse_rect_x, self.morse_rect_y = 100, self.text_rect_y + 120
        #Make the text boxes
        if line_width < self.screen.get_width():
            self.text_rect = pygame.Rect(self.text_rect_x, self.text_rect_y, 140, 80)
            self.morse_rect = pygame.Rect(self.morse_rect_x, self.morse_rect_y, 140, 80)
        elif line_width > self.screen.get_width():
            self.text_rect_x, self.morse_rect_x = 100, 100
            self.text_rect_y, self.morse_rect_y = self.text_rect_y + 200, self.morse_rect_y + 200
            self.text_rect = pygame.Rect(self.text_rect_x, self.text_rect_y, 140, 80)
            self.morse_rect = pygame.Rect(self.morse_rect_x, self.morse_rect_y, 140, 80)
        return self.text_rect, self.morse_rect

    def convert_morse_code(self):
        """Take user text, convert to morse"""
        character_pos = []
        morse_letters = []
        #Sort through user input, comparing to dictionary which is all caps
        for num, character in enumerate(self.user_text.upper()):
            #Check to see if the text is already displayed, if not then update lists
            if character in self.morse and num not in character_pos:
                morse_letters.append(self.morse[character])
                morse_letters.append("  ")
                character_pos.append(num)
            #Handle spaces that are not in dictionary and add spacing for readability
            elif character == " ":
                morse_letters.append("   ")
                character_pos.append(num)
            #Skip anything that's not morse code or a space
            else:
                pass
        #Convert morse code list into a string that can be rendered in pygame
        self.ditdah = "".join(morse_letters)


if __name__ == "__main__":
    game = MainGame()
    game.run_game()