"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

def setting():
    import pygame, os
    home = os.getenv("HOME")
    path = os.path.dirname(os.path.abspath(__file__))

    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    ORANGE = (255, 122, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 180, 0)
    LIGHT_BLUE = (0, 255, 255)
    BLUE = (0, 0, 255)
    VIOLET = (205, 0, 255)
    colors = [RED, ORANGE, YELLOW, GREEN, LIGHT_BLUE, BLUE, VIOLET]
    mouse_colors_x = [325, 375, 425, 475, 525, 575, 625, 675]

    pygame.init()

    # Set the width and height of the screen [width, height]
    width = 750
    height = 1000
    size = (width, height)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("My Game")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                return True

        # --- Game logic should go here
        mouse = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        if pos[0] > 250 and pos[0] < 520:
            if pos[1] > 100 and pos[1] < 150:
                if mouse[0] == 1:
                    if os.path.exists(path+"/score"):
                        os.remove("score")




        # --- Screen-clearing code goes here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        # If you want a background image, replace this clear with blit'ing the
        # background image.
        screen.fill(WHITE)

        # --- Drawing code should go here
        file_score = []
        if os.path.exists(path+"/score"):
            with open(path+"/score") as f:
                for line in f:
                    file_score.append(line)
        else:
            file_score = [0]
        font = pygame.font.SysFont('Calibri', 50, False, False)
        text = font.render("highscore: "+str(file_score[0]), True, BLACK)
        screen.blit(text, [150, 110])

        pygame.draw.rect(screen, BLACK, [450, 100, 100, 50], 2)
        font = pygame.font.SysFont('Calibri', 50, False, False)
        text = font.render("reset", True, BLACK)
        screen.blit(text, [460, 110])


        pygame.draw.rect(screen, BLACK, [575, 900, 100, 50], 2)
        font = pygame.font.SysFont('Calibri', 50, False, False)
        text = font.render("back", True, BLUE)
        # Put the image of the text on the screen at 250x250
        screen.blit(text, [585, 910])
        mouse = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        if pos[0] > 575 and pos[0] < 675:
            if pos[1] > 900 and pos[1] < 950:
                if mouse[0] == 1:
                    done = True
                    return False

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)