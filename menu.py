#!/usr/bin/python
"""
made with pygame module for python gui games

Author: Alexander Patrushin
Big thanks to mom, dad and little brother for helping debugging, giving ideas and breaking conflicts

open source tetris game

https://sites.google.com/site/nice0tetris/home
"""

import pygame, tetris, settings

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 250, 0)

pygame.init()

# Set the width and height of the screen [width, height]
width = 750
height = 1000
size = (width, height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False
play = False
set_up = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    mouse = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()
    if pos[0] > 250 and pos[0] < 500:
        if pos[1] > 200 and pos[1] < 300:
            if mouse[0] == 1:
                play = True
        elif pos[1] > 350 and pos[1] < 450:
            if mouse[0] == 1:
                set_up = True

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # --- Drawing code should go here
    pygame.draw.rect(screen, BLUE, [250, 200, 250, 100], 0)
    pygame.draw.rect(screen, BLACK, [250, 200, 250, 100], 2)
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 100, True, False)

    # Render the text. "True" means anti-aliased text.
    # Black is the color. The variable BLACK was defined
    # above as a list of [0, 0, 0]
    # Note: This line creates an image of the letters,
    # but does not put it on the screen yet.
    text = font.render("PLAY", True, ORANGE)

    # Put the image of the text on the screen at 250x250
    screen.blit(text, [275, 215])

    pygame.draw.rect(screen, BLUE, [250, 350, 250, 100], 0)
    pygame.draw.rect(screen, BLACK, [250, 350, 250, 100], 2)
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 50, True, False)

    # Render the text. "True" means anti-aliased text.
    # Black is the color. The variable BLACK was defined
    # above as a list of [0, 0, 0]
    # Note: This line creates an image of the letters,
    # but does not put it on the screen yet.
    text = font.render("SETTINGS", True, ORANGE)

    # Put the image of the text on the screen at 250x250
    screen.blit(text, [275, 380])

    pygame.draw.rect(screen, BLACK, [325, 900, 100, 50], 2)
    font = pygame.font.SysFont('Calibri', 50, False, False)
    text = font.render("quit", True, BLUE)
    # Put the image of the text on the screen at 250x250
    screen.blit(text, [340, 910])
    mouse = pygame.mouse.get_pressed()
    pos = pygame.mouse.get_pos()
    if pos[0] > 325 and pos[0] < 425:
        if pos[1] > 900 and pos[1] < 950:
            if mouse[0] == 1:
                done = True

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
    if play:
        play = False
        done = tetris.game()
    elif set_up:
        set_up = False
        done = settings.setting()

# Close the window and quit.
pygame.quit()