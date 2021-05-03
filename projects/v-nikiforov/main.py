#!/usr/bin/env python3.9

import sys
import pygame

SIZE = WIDTH, HEIGHT = 1000, 750
CELL_SIZE = (25, 25)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (130, 130, 130)
GRID_WIDTH = 1
SIMULATION_SPEED = 9
FPS = 40


assert SIMULATION_SPEED <= 10, "SIMULATION_SPEED can't be more than 10"


def fill_rects(screen, pos_array):
    """
    Function that colors specified array of rectangles on screen
    :param screen: screen to draw on
    :param pos_array: array of tuples with coordinates
    :return: None
    """
    for pos in pos_array:
        pygame.draw.rect(screen, (255, 242, 0), pygame.Rect(pos[0], pos[1], *CELL_SIZE))


def init_game():
    """
    Some basic steps to initialize the game
    :return: screen to work on and clock for the FPS regulation
    """
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Nikiforov – Game of life")
    return screen, pygame.time.Clock()


def draw_grid(screen, dx, dy):
    """
    Draw grid on a screen
    :param screen: screen to draw greed on
    :param dx: offset by x
    :param dy: offset by y
    :return: None
    """
    dx = dx % CELL_SIZE[0]
    dy = dy % CELL_SIZE[1]
    for i in range(WIDTH // CELL_SIZE[0] + 1):
        pygame.draw.line(
            screen,
            WHITE,
            (CELL_SIZE[0] * i - dx, 0),
            (CELL_SIZE[0] * i - dx, HEIGHT),
            GRID_WIDTH,
        )
    for i in range(HEIGHT // CELL_SIZE[1] + 1):
        pygame.draw.line(
            screen,
            WHITE,
            (0, CELL_SIZE[1] * i - dy),
            (WIDTH, CELL_SIZE[1] * i - dy),
            GRID_WIDTH,
        )


def get_rect_corner(pos, dx, dy):
    """
    Get rectangle top left corner coordinates
    :param pos: coordinates of some rectangle point
    :param dx: offfset by x
    :param dy: offset by y
    :return: tuple of coordinates
    """
    return (
        ((pos[0] + dx % CELL_SIZE[0]) // CELL_SIZE[0]) * CELL_SIZE[0]
        - dx % CELL_SIZE[0],
        ((pos[1] + dy % CELL_SIZE[1]) // CELL_SIZE[1]) * CELL_SIZE[1]
        - dy % CELL_SIZE[1],
    )


def update_life(rects):
    """
    Perform one step of the game (main logic)
    :param rects: rectangles to make interaction
    :return: living rectangles after the step
    """
    all_neighbors = {}
    sx, sy = CELL_SIZE[0], CELL_SIZE[1]
    for i in rects:
        all_neighbors.setdefault(i, 0)
        curr_neighbors = (
            (i[0] + sx, i[1]),
            (i[0], i[1] + sy),
            (i[0] - sx, i[1]),
            (i[0], i[1] - sy),
            (i[0] + sx, i[1] + sy),
            (i[0] + sx, i[1] - sy),
            (i[0] - sx, i[1] - sy),
            (i[0] - sx, i[1] + sy),
        )
        for j in curr_neighbors:
            all_neighbors.setdefault(j, 0)
            all_neighbors[j] += 1
    for i in rects.copy():
        if all_neighbors[i] > 3 or all_neighbors[i] < 2:
            rects.remove(i)
    for k in all_neighbors:
        if all_neighbors[k] == 3:
            rects.add(k)
    return rects


def draw_text(screen, running):
    """
    Draw some text for user comfort
    :param screen: screen to draw on
    :param running: is simulation running or not
    :return: None
    """
    font_size = 20
    font = pygame.font.Font("static/fonts/Monaco.ttf", font_size)
    guide1 = font.render("SPACE to start simulation", False, (0, 0, 0))
    guide2 = font.render("ENTER to make one step", False, (0, 0, 0))
    guide3 = font.render("BACKSPACE to clear", False, (0, 0, 0))
    running_text1 = font.render(f"Running: ", False, (0, 0, 0))
    if running:
        running_text2 = font.render(" " * 9 + "yes", False, (11, 102, 35))
    else:
        running_text2 = font.render(" " * 9 + "no", False, (184, 15, 10))
    screen.blit(running_text1, (5, 5))
    screen.blit(running_text2, (5, 5))
    screen.blit(guide1, (5, HEIGHT - (font_size + 5) * 3 - 5))
    screen.blit(guide2, (5, HEIGHT - (font_size + 5) * 2 - 5))
    screen.blit(guide3, (5, HEIGHT - (font_size + 5) * 1 - 5))


def shifted_rects(rects, dx, dy):
    """
    Get rectangles coordinates with respect to shift
    :param rects: input rectangles
    :param dx: offset by x
    :param dy: offset by y
    :return: shifted rectangles set
    """
    return set([(i - dx, j - dy) for i, j in rects])


def main():
    """
    Main method of the game
    :return: None
    """
    screen, clock = init_game()
    # set of rectangles
    rects = set()
    # simulating or not
    running = False
    speed_counter = 0
    holding_mouse = False
    initial_mouse_pos = None
    shifted = False
    grid_dx, grid_dy = 0, 0
    while ...:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                holding_mouse = True
                initial_mouse_pos = pygame.mouse.get_pos()
            # draw rectangle or end dragging
            if event.type == pygame.MOUSEBUTTONUP:
                holding_mouse = False
                if not shifted:
                    pos = pygame.mouse.get_pos()
                    corner = get_rect_corner(pos, grid_dx, grid_dy)
                    if corner in rects:
                        rects.remove(corner)
                    else:
                        rects.add(corner)
                else:
                    shifted = False
            # user controls (buttons)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    update_life(rects)
                if event.key == pygame.K_SPACE:
                    running = not running
                if event.key == pygame.K_BACKSPACE:
                    rects = set()
        # dragging screen
        if holding_mouse:
            pos = pygame.mouse.get_pos()
            dx, dy = initial_mouse_pos[0] - pos[0], initial_mouse_pos[1] - pos[1]
            # figure out if it was click or drag
            if abs(dx) > 3 or abs(dy) > 3:
                shifted = True
            if shifted:
                grid_dx += dx
                grid_dy += dy
                rects = shifted_rects(rects, dx, dy)
                initial_mouse_pos = pos

        # steps' speed regulation
        # after a long time, I came up with this great (no) formula
        if running and speed_counter >= (1000 - (9 + SIMULATION_SPEED / 10) * 100):
            speed_counter = 0
            update_life(rects)
        speed_counter += 1

        # rendering
        screen.fill(GREY)
        fill_rects(screen, rects)
        draw_grid(screen, grid_dx, grid_dy)
        draw_text(screen, running)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
