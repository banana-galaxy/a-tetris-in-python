#!/usr/bin/python
"""
made with pygame module for python gui games

Author: Alexander Patrushin
Big thanks to mom, dad and little brother for helping debugging, giving ideas and breaking conflicts

open source tetris game

https://sites.google.com/site/nice0tetris/home
"""

'''todo:
game over                         done
score                             done
fix bug so shapes appear at top   done
next figure
hold
'''

def game():
    import pygame, random, os
    import numpy as np
    home = os.getenv("HOME")
    path = os.path.dirname(os.path.abspath(__file__))

    field = []
    for i in range(10):
        field.append([])
        for b in range(20):
            field[i].append(0)

    #field[6][10] = 1

    shapes = np.array([[
        [[1, 1, 0, 0],
         [1, 1, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]],
        [[1, 1, 0, 0],
         [1, 1, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]],
        [[1, 1, 0, 0],
         [1, 1, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]],
        [[1, 1, 0, 0],
         [1, 1, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]],

        [[[2, 2, 2, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]],
         [[2, 0, 0, 0],
          [2, 0, 0, 0],
          [2, 0, 0, 0],
          [2, 0, 0, 0]],
         [[2, 2, 2, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]],
         [[2, 0, 0, 0],
          [2, 0, 0, 0],
          [2, 0, 0, 0],
          [2, 0, 0, 0]]],

        [[[0, 3, 3, 0],
          [3, 3, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]],
         [[3, 0, 0, 0],
          [3, 3, 0, 0],
          [0, 3, 0, 0],
          [0, 0, 0, 0]],
         [[0, 3, 3, 0],
          [3, 3, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]],
         [[3, 0, 0, 0],
          [3, 3, 0, 0],
          [0, 3, 0, 0],
          [0, 0, 0, 0]]],

        [[[4, 4, 0, 0],
          [0, 4, 4, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]],
         [[0, 4, 0, 0],
          [4, 4, 0, 0],
          [4, 0, 0, 0],
          [0, 0, 0, 0]],
         [[4, 4, 0, 0],
          [0, 4, 4, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]],
         [[0, 4, 0, 0],
          [4, 4, 0, 0],
          [4, 0, 0, 0],
          [0, 0, 0, 0]]],

        [[[5, 0, 0, 0],
          [5, 0, 0, 0],
          [5, 5, 0, 0],
          [0, 0, 0, 0]],
         [[5, 5, 5, 0],
          [5, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]],
         [[5, 5, 0, 0],
          [0, 5, 0, 0],
          [0, 5, 0, 0],
          [0, 0, 0, 0]],
         [[0, 0, 5, 0],
          [5, 5, 5, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]],

        [[[0, 6, 0, 0],
          [0, 6, 0, 0],
          [6, 6, 0, 0],
          [0, 0, 0, 0]],
         [[6, 0, 0, 0],
          [6, 6, 6, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]],
         [[6, 6, 0, 0],
          [6, 0, 0, 0],
          [6, 0, 0, 0],
          [0, 0, 0, 0]],
         [[6, 6, 6, 0],
          [0, 0, 6, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]],

        [[[0, 7, 0, 0],
          [7, 7, 7, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]],
         [[7, 0, 0, 0],
          [7, 7, 0, 0],
          [7, 0, 0, 0],
          [0, 0, 0, 0]],
         [[7, 7, 7, 0],
          [0, 7, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]],
         [[0, 7, 0, 0],
          [7, 7, 0, 0],
          [0, 7, 0, 0],
          [0, 0, 0, 0]]]])


    class shape():
        def __init__(self):
            self.figure = random.randrange(7)
            self.x_pos = 3
            self.y_pos = 0
            self.rotation = random.randrange(4)

            self.x_new = self.x_pos
            self.y_new = self.y_pos
            self.rotation_new = self.rotation

            self.hold_figure = self.figure
            self.hold_rotation = self.rotation

            self.overlapping = False
            self.too_much_right = False

        def init(self):
            self.figure = self.next_figure
            self.x_pos = 3
            self.y_pos = 0
            self.rotation = self.next_rotation

        def hold(self, replace = True):
            if not replace:
                self.clear()

                space_available = self.check(self.next_figure, self.next_rotation, self.x_pos, self.y_pos)
                if not space_available:
                    self.draw()

                else:
                    self.hold_figure = self.figure
                    self.hold_rotation = self.rotation

                    self.figure = self.next_figure
                    self.rotation = self.next_rotation

                    self.generate_next_shape()
                    self.draw()


            else:
                self.clear()

                space_available = self.check(self.hold_figure, self.hold_rotation, self.x_pos, self.y_pos)
                if not space_available:
                    self.draw()
                else:
                    temp_figure = self.figure
                    temp_rotation = self.rotation

                    self.figure = self.hold_figure
                    self.rotation = self.hold_rotation

                    try:
                        self.draw()
                        self.hold_figure = temp_figure
                        self.hold_rotation = temp_rotation
                    except IndexError:
                        self.clear()
                        self.figure = temp_figure
                        self.rotation = temp_rotation
                        self.draw()
                        return 0

        def draw_hold(self, x, y):
            return shapes[self.hold_figure][self.hold_rotation][y][x]

        def h_color(self):
            hold_color = int(self.hold_figure)
            return hold_color

        def generate_next_shape(self):
            self.next_figure = random.randrange(7)
            while True:
                if self.next_figure == self.figure:
                    self.next_figure = random.randrange(7)
                else:
                    break

            self.next_rotation = random.randrange(4)
            '''self.next_color = random.randrange(7)
            while True:
                if self.next_color == self.color:
                    self.next_color = random.randrange(7)
                else:
                    break'''

        def draw_next_shape(self, x, y):
            return shapes[self.next_figure][self.next_rotation][y][x]

        def n_color(self):
            next_color = int(self.next_figure)
            return next_color

        '''def colourr(self):
            collor = int(self.color)
            return collor'''

        def draw(self):
            for xxx in range(4):
                for yyy in range(4):
                    if shapes[self.figure][self.rotation][yyy][xxx] >= 1:
                        field[self.x_pos + xxx][self.y_pos + yyy] = shapes[self.figure][self.rotation][yyy][xxx]

        def clear(self):
            for xxx in range(4):
                for yyy in range(4):
                    if shapes[self.figure][self.rotation][yyy][xxx] >= 1:
                        field[self.x_pos + xxx][self.y_pos + yyy] = 0

        def clear_line(self):
            clear = True
            count = 0
            for y in range(20):
                for x in range(10):
                    if field[x][y] == 0:
                        clear = False
                if clear:
                    count += 1
                    yy = y
                    while yy > 0:
                        for x in range(10):
                            field[x][yy] = field[x][yy-1]
                        yy -= 1
                clear = True
            return count

        def check(self, figure, rotation, x, y):
            self.too_much_right = False
            for xe in range(4):
                for ye in range(4):
                    try:
                        if shapes[figure][rotation][ye][xe] >= 1:
                            if x+xe > 9:
                                self.too_much_right = True
                            if x+xe > 9 or y+ye > 19 or x+xe < 0 or field[x + xe][y + ye] >= 1:
                                return False
                            else:
                                return True
                    except IndexError:
                        if x + xe > 9:
                            self.too_much_right = True
                        if x + xe > 9 or y + ye > 19 or x + xe < 0 or field[x + xe][y + ye] >= 1:
                            return False

        def move(self):
            moving_down = False
            overlapping = False

            if self.y_new > self.y_pos:
                moving_down = True

            #clearing position
            for xx in range(4):
                for yy in range(4):
                    if shapes[self.figure][self.rotation][yy][xx] >= 1:
                        field[self.x_pos + xx][self.y_pos + yy] = 0
                        '''if not 0 <= self.x_pos + xx <= 9:
                            print "X-balbes!"
                        if not 0 <= self.y_pos + yy <= 19:
                            print "Y-balbes!"'''

            #print("x_new=" + str(self.x_new))
            #checking for available space
            #if self.check(self.figure, self.rotation_new, self.x_new, self.y_new) == False:
            #    overlapping = True
            for xe in range(4):
                for ye in range(4):
                    if shapes[self.figure][self.rotation_new][ye][xe] >= 1:
                        if self.x_new+xe > 9 or self.y_new+ye > 19 or self.x_new+xe < 0 or field[self.x_new + xe][self.y_new + ye] >= 1:
                            overlapping = True

            #if space is available, draw
            if not overlapping:
                self.x_pos = self.x_new
                self.y_pos = self.y_new
                self.rotation = self.rotation_new

            self.draw()
            self.overlapping = overlapping

            if overlapping and self.y_pos == 0 and moving_down:
                return "gameover"
            elif moving_down and overlapping:
                return True
            else:
                return False


        def calc_new_pos(self, d_x, d_y, d_dir = None):
            self.x_new = self.x_pos + d_x
            self.y_new = self.y_pos + d_y

            self.rotation_new = self.rotation

            if d_dir == "left":
                if self.rotation_new == 0:
                    self.rotation_new = 3
                else:
                    self.rotation_new -= 1
            elif d_dir == "right":
                if self.rotation_new == 3:
                    self.rotation_new = 0
                else:
                    self.rotation_new += 1
            #print(self.rotation_new)









    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    #GREEN = (0, 255, 0)
    #RED = (255, 0, 0)
    #BLUE = (0, 0, 255)
    #ORANGE = (255, 122, 0)
    BACK = (66, 182, 244)
    RED = (255, 0, 0)
    ORANGE = (255, 122, 0)
    YELLOW = (255, 212, 0)
    GREEN = (0, 180, 0)
    LIGHT_BLUE = (68, 174, 255)
    BLUE = (0, 0, 255)
    VIOLET = (205, 0, 255)
    colors = [RED, ORANGE, YELLOW, GREEN, LIGHT_BLUE, BLUE, VIOLET]

    pygame.init()

    # Set the width and height of the screen [width, height]
    width = 750 #500 left part
    height = 1000
    size = (width, height)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("TETRIS")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    n = random.randrange(6)

    squar = shape()
    squar.draw()
    squar.generate_next_shape()

    down_tick = 0
    left_tick = 0
    right_tick = 0
    fall_tick = 0
    score = 0
    add_to_score = 0
    speed = 60
    hold_count = 0

    stop = False
    fall = False
    faster = False
    left = False
    right = False
    gameover = False
    replace_hold = False
    win = False
    pause = False

    # -------- Main Program Loop -----------
    while not done:
        down_tick += 1
        left_tick += 1
        right_tick += 1
        fall_tick += 1
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                return True

            elif event.type == pygame.KEYDOWN:
                # Figure out if it was an arrow key. If so
                # adjust speed.
                if event.key == pygame.K_p:
                    if pause:
                        pause = False
                    else:
                        pause = True

                if not pause:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if not stop:
                            left = True

                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if not stop:
                            right = True

                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        faster = True

                    if event.key == pygame.K_c or event.key == pygame.K_w or event.key == pygame.K_UP:
                        squar.calc_new_pos(0,0,"right")
                        squar.move()

                    if event.key == pygame.K_x:
                        squar.calc_new_pos(0,0,"left")
                        squar.move()

                    if event.key == pygame.K_SPACE:
                        fall = True

                    if event.key == pygame.K_h:
                        stayed = 1
                        if hold_count < 1:
                            stayed = squar.hold(replace_hold)
                            replace_hold = True
                        if stayed != 0:
                            hold_count += 1
                else:
                    faster = False
                    left = False
                    right = False

            elif event.type == pygame.KEYUP:
                if not pause:
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        faster = False
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        left = False
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        right = False

        # --- Game logic should go here
        if not pause:
            if fall:
                if fall_tick >= 1:
                    squar.calc_new_pos(0, 1)
                    stop = squar.move()
                    if stop:
                        fall = False
            else:
                if down_tick >= speed:
                    down_tick = 0
                    squar.calc_new_pos(0, 1)
                    stop = squar.move()
            if faster:
                if down_tick >= 5:
                    down_tick = 0
                    squar.calc_new_pos(0, 1)
                    stop = squar.move()
            if stop == True:
                if hold_count >= 1:
                    hold_count = 0
                score += 4
                add_to_score = squar.clear_line()
                if add_to_score >= 1:
                    speed -= add_to_score
                score = score + add_to_score * 10

                file_score = []
                if os.path.exists(path+"/score"):
                    with open("score", 'r') as f:
                        for line in f:
                            file_score.append(int(line))
                else:
                    file_score = [0,0]

                try:
                    if score >= file_score[0]:
                        with open("score", 'w') as f:
                            f.write(str(score))
                        win = True
                except IndexError:
                    with open("score", 'w') as f:
                        f.write(str(score))

                squar.init()
                squar.draw()
                squar.generate_next_shape()
                stop = False
                down_tick = 0
            elif stop == "gameover":
                gameover = True

            if left:
                if left_tick >= 8:
                    left_tick = 0
                    squar.calc_new_pos(-1, 0)
                    squar.move()
            if right:
                if right_tick >= 8:
                    right_tick = 0
                    squar.calc_new_pos(1, 0)
                    squar.move()

        # --- Screen-clearing code goes here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        # If you want a background image, replace this clear with blit'ing the
        # background image.
        screen.fill(WHITE)

        # --- Drawing code should go here
        if gameover:
            # Select the font to use, size, bold, italics
            text_size = 50
            font = pygame.font.SysFont('Calibri', text_size, True, False)

            # Render the text. "True" means anti-aliased text.
            # Black is the color. The variable BLACK was defined
            # above as a list of [0, 0, 0]
            # Note: This line creates an image of the letters,
            # but does not put it on the screen yet.
            text = font.render("GAME OVER", True, RED)

            # Put the image of the text on the screen at 250x250
            screen.blit(text, [137, (height/2)-text_size])
        else:
            tetris_width = width-250
            for x in range(10):
                for y in range(20):
                    if field[x][y] >= 1:
                        pygame.draw.rect(screen, colors[field[x][y]-1], [(tetris_width/10)*(x), (height/20)*(y), tetris_width/10, height/20], 0)
                    else:
                        pygame.draw.rect(screen, WHITE, [(tetris_width/10)*(x), (height/20)*(y), tetris_width/10, height/20], 0)

            for x in range(9):
                pygame.draw.line(screen, BLACK, [(tetris_width / 10) * (x + 1), 0], [(tetris_width / 10) * (x + 1), height], 2)
            for y in range(19):
                pygame.draw.line(screen, BLACK, [0, (height / 20) * (y + 1)], [tetris_width, (height / 20) * (y + 1)], 2)

        pygame.draw.line(screen, BLACK, [(tetris_width / 10) * (9 + 1), 0], [(tetris_width / 10) * (9 + 1), height], 2)

        font = pygame.font.SysFont('Calibri', 40, True, False)
        text = font.render("score: " + str(score), True, BLACK)
        # Put the image of the text on the screen at 250x250
        screen.blit(text, [565, 25])

        font = pygame.font.SysFont('Calibri', 50, False, False)
        text = font.render("next", True, BLACK)
        # Put the image of the text on the screen at 250x250
        screen.blit(text, [590, 110])

        font = pygame.font.SysFont('Calibri', 50, False, False)
        text = font.render("hold", True, BLACK)
        # Put the image of the text on the screen at 250x250
        screen.blit(text, [590, 410])

        for x in range(4):
            for y in range(4):
                if squar.draw_next_shape(x, y) >= 1 and gameover == False:
                    pygame.draw.rect(screen, colors[squar.n_color()], [(50 * x) + 525, (50 * y) + 150, 50, 50], 0)
                else:
                    pygame.draw.rect(screen, WHITE, [(50 * x) + 525, (50 * y) + 150, 50, 50], 0)

        for x in range(5):
            pygame.draw.line(screen, BLACK, [525 + x*50, 150], [525 + x*50, 350], 2)
        for y in range(5):
            pygame.draw.line(screen, BLACK, [525, 150 + y*50], [725, 150 + y*50], 2)

        if pause:
            font = pygame.font.SysFont('Calibri', 200, False, False)
            text = font.render("PAUSE", True, BLACK)
            # Put the image of the text on the screen at 250x250
            screen.blit(text, [20, 400])

        for x in range(4):
                for y in range(4):
                    if replace_hold:
                        if squar.draw_hold(x, y) >= 1 and gameover == False:
                            pygame.draw.rect(screen, colors[squar.h_color()], [(50 * x) + 525, (50 * y) + 450, 50, 50], 0) # 50 525 50 150 50 50
                        else:
                            pygame.draw.rect(screen, WHITE, [(50 * x) + 525, (50 * y) + 450, 50, 50], 0) # "

        for x in range(5):
            pygame.draw.line(screen, BLACK, [525 + x*50, 450], [525 + x*50, 650], 2) # 525 50 150 525 50 350
        for y in range(5):
            pygame.draw.line(screen, BLACK, [525, 450 + y*50], [725, 450 + y*50], 2) # 525 150 50 725 150 50

        if win:
            font = pygame.font.SysFont('Calibri', 25, False, False)
            text = font.render("NEW HIGHSCORE!", True, BLACK)
            screen.blit(text, [550, 800])

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
