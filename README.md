# Morse-Code-Writer
Type text and get the morse code translation *work in progress

learn_morse is the first attempt to get text from the user , display it in a text box, and display the morse code translation.  The text box is a rectangle object, and I haven't figured out how to end the object and text where it is when the text hits the edge of the screen, then start both lines below the last two.
NewPlan is a second attempt that uses another youtube tutorial for wrapping text.  After reducing to a 1D list instead of a 2D list, it works to convert and wrap, but the lines wrap independently and write over each other.  This needs some clean up for spacing.
morse is the morse code dictionary
button and settings are classes that I made for the Python Crash Course alien invasion tutorial and then adapted copies for this project

Future plans are to add pygame sound effects for the dits and dahs, create and play common morse code messages to try to interperet, and reverse functionality to try to input dits and dahs and have text displayed.
Way down the road would be to have a paddle provide GPIO to raspberry pi to input dits and dahs
