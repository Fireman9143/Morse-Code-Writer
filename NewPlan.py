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
            self.convert_morse_code()
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
            self.display_user_input((100, 100))  
        pygame.display.flip()
    
     
    def display_user_input(self, pos):
        """Function to wrap lines"""
        #Take string as arguement and split into list if lists
        user_input = self.user_text.split(" ")
        converted = self.ditdah.split(" ")
        #Sets a space variable as the x dimension of the font size (x=[0], y=[1])
        space = self.settings.text_font.size(" ")[0]
        #Sets the x, y to use for drawing text from the pos arguement
        x,y = pos
        #Looks at each list of words within that part
        for words in user_input:
            #Render the words as a font
            word_surface = self.settings.text_font.render(words, True, 'green')
            #Get the dimensions of the rendered font
            word_width, word_height = word_surface.get_size()
            #Compare the width of the rendered text to the window width (start at x and go until new line or window edge)
            if x + word_width >= self.screen.get_width():
                #If font reaches edge, reset x to the font starting point pos[0] and change y by font height
                x = pos[0]
                y += word_height + 5
            #Draw the rendered font started at the pos x,y
            self.screen.blit(word_surface, (x, y))
            #Next word starting position will be a space after the last word
            x += word_width + space
        if len(self.user_text) > 0:
            a,b = pos
            b = self.screen.get_height()/2
            for dahs in converted:
                #Render the words as a font
                code_surface = self.settings.morse_font.render(dahs, True, 'lightblue')
                #Get the dimensions of the rendered font
                code_width, code_height = code_surface.get_size()
                #Compare the width of the rendered text to the window width (start at x and go until new line or window edge)
                if a + code_width >= self.screen.get_width():
                    #If font reaches edge, reset x to the font starting point pos[0] and change y by font height
                    a = pos[0]
                    b += code_height
                #Draw the rendered font started at the pos x,y
                self.screen.blit(code_surface, (a, b))
                #Next word starting position will be a space after the last word
                a += code_width + space
                

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