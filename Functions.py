import pygame

import Variables
import Snake
import Food


def end_game():
    """
    Ends the game.
    """

    pygame.quit()
    Variables.sys.exit()


def check_eat(snake, food):
    """
    Checks if snake ate the food. Calls generation of new position if food is eaten.

    Args:
        snake (obj): Object of class Snake
        food (obj): Object of class Food
    """

    if snake.get_head_position() == food.position:
        snake.length += 1
        snake.points += Variables.score_multi
        Variables.is_eaten = True
        Food.Food().generate_food_pos()



def text_objects(text, font, color):
    """
    Function for creating text and it's surrounding rectangle.

    Args:
        text (str): Text to be rendered.
        font (Font): Type of font to be used.
        color ((int, int, int)): Color to be used. Values should be in range 0-255.
    Returns:
        Text surface and it's surrounding rectangle.
    """

    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()



def load_img(img, scale):
    """
    Function for loading and scaling images.

    Args:
        img (str): Path where the image is saved.
        scale (float): Scale factor with which the image should be scaled.

    Returns:
        Loaded and scaled image.
    """

    image = pygame.image.load(img).convert_alpha()
    image = pygame.transform.scale(image, (int(scale * Variables.body_size), int(scale * Variables.body_size)))
    return image


def button(text, x, y, width, height, hover_color, text_color, click_function=None):
    """
    Custom button creation.

    Args:
        text (str): Text to be displayed on the button.
        x (int): X position where the button should be placed.
        y (int Y):  position where the button should be placed.
        width (int): Width of the button.
        height (int): Height of the button.
        hover_color ((int, int, int)): Color of the button when the mouse hoovers over it.
        text_color ((int, int, int)): Color of the displayed text.
        click_function (str): Function to be called when button is clicked.
    """

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # hoovering over the button
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(Variables.screen, hover_color, (x, y, width, height))
        if click[0] == 1 and click_function is not None:
            click_function()

    text_surface, text_rect = text_objects(text, Variables.small_text, text_color)
    text_rect.center = ((x + (width/2)), (y + (height/2)))
    Variables.screen.blit(text_surface, text_rect)


def score(value):
    """
    Displaying the score on the screen.

    Args:
        value (int): Actual score of the player.
    """

    text = Variables.small_text.render("Score:        " + str(value), True, Variables.orange)
    Variables.screen.blit(text, [Variables.block_size * 8, Variables.block_size * 13.4])


def length(value):
    """
    Displaying the length on the screen.

    Args:
        value (int): Actual length of the snake.
    """

    text = Variables.small_text.render("Length:     " + str(value), True, Variables.orange)
    Variables.screen.blit(text, [Variables.block_size * 8, Variables.block_size * 14])


def died():
    """
    This happens if snake dies.
    """

    Variables.is_dead = True
    Snake.Snake().direction = Variables.PAUSE
    Variables.points = Snake.Snake().points
    Variables.high_score.append(Variables.points)
    Variables.high_score = sorted(Variables.high_score, reverse=True)




