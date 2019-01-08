import Variables
import Snake


def easy():
    """
    Sets values of the variables according to EASY level.
    """

    Variables.fps = 6
    Variables.score_multi = 2
    Variables.starting = False
    Snake.Snake().reset_snake()


def medium():
    """
    Sets values of the variables according to MEDIUM level.
    """

    Variables.fps = 9
    Variables.score_multi = 3
    Variables.starting = False
    Snake.Snake().reset_snake()


def hard():
    """
    Sets values of the variables according to HARD level.
    """

    Variables.fps = 12
    Variables.score_multi = 4
    Variables.starting = False
    Snake.Snake().reset_snake()


def re_level():
    """
    Calls the starting screen, if the snake died and user wants to change the level of the game.
    """

    Variables.starting = True
    Variables.Screens.starting()

