import Variables
import Functions
import pygame
import Snake
import Levels


def pause(snake):
    """
    Displays Pause Screen.

    Args:
        snake (obj):  Object of class Snake.
    """

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Functions.end_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    snake.direction = Variables.resume_dir
                    Variables.Main.game_loop()

        text_surface, text_rect = Functions.text_objects('||', Variables.large_text, Variables.black)
        text_surface2, text_rect2 = \
            Functions.text_objects('Press space to resume', Variables.small_text, Variables.black)
        text_rect.center = ((Variables.game_width / 2), (Variables.game_height / 3))
        text_rect2.center = ((Variables.game_width / 2), (Variables.game_height / 2))

        Variables.screen.blit(text_surface, text_rect)
        Variables.screen.blit(text_surface2, text_rect2)

        Variables.resume_dir = snake.direction

        pygame.display.update()
        Variables.clock.tick(30)


def lost():
    """
    Displays the screen when the snake died. Waits for input from the user what to do next.
    """

    while Variables.is_dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Functions.end_game()

        Variables.screen.blit(Variables.lost, (Variables.block_size * 3, Variables.block_size * 4.5))
        text_surface, text_rect = Functions.text_objects('Best scores: ', Variables.small_text, Variables.orange)
        text_rect.center = (Variables.block_size * 6, int(Variables.block_size * 6.3))
        Variables.screen.blit(text_surface, text_rect)

        scores = 0
        for score in Variables.high_score:
            scores += 1
            if scores < 6:
                text_surface, text_rect = Functions.text_objects("{} points".format(score),
                                                                 Variables.small_text, Variables.orange)
                text_rect = (Variables.block_size * 3.6,
                             int(Variables.block_size * 6.2) + scores * Variables.block_size * 0.5)
                Variables.screen.blit(text_surface, text_rect)

        Functions.button('Start', Variables.block_size * 3.4, Variables.block_size * 9.2,
                         Variables.block_size * 1.6, Variables.block_size * .8, Variables.dark_gray,
                         Variables.orange, Snake.Snake().reset_snake)
        Functions.button('Exit', Variables.block_size * 5.3, Variables.block_size * 9.2,
                         Variables.block_size * 1.6, Variables.block_size * .8, Variables.dark_gray,
                         Variables.orange, Functions.end_game)
        Functions.button('Level', Variables.block_size * 7, Variables.block_size * 9.2,
                         Variables.block_size * 1.6, Variables.block_size * .8, Variables.dark_gray,
                         Variables.orange, Levels.re_level)

        pygame.display.update()
        Variables.clock.tick(30)


def starting():
    """
    Displays the welcome screen. Waits for the user input about chosen level.
    """
    while Variables.starting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Functions.end_game()

        Variables.screen.blit(Variables.welcome, (Variables.block_size * 3, Variables.block_size * 4.5))
        text_surface, text_rect = Functions.text_objects('Choose level: ', Variables.small_text, Variables.orange)
        text_rect.center = (Variables.block_size * 6, int(Variables.block_size * 6.6))
        Variables.screen.blit(text_surface, text_rect)

        Functions.button('Easy', Variables.block_size * 5, Variables.block_size * 6.9,
                         Variables.block_size * 2, Variables.block_size * 1,  Variables.dark_gray,
                         Variables.orange, Levels.easy)
        Functions.button('Medium', Variables.block_size * 5, Variables.block_size * 7.9,
                         Variables.block_size * 2, Variables.block_size * 1, Variables.dark_gray,
                         Variables.orange, Levels.medium)
        Functions.button('Hard', Variables.block_size * 5, Variables.block_size * 8.9,
                         Variables.block_size * 2, Variables.block_size * 1, Variables.dark_gray,
                         Variables.orange, Levels.hard)

        pygame.display.update()
        Variables.clock.tick(30)
