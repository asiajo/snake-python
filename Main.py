"""
Simple 2D Snake game.

The game was written using PyGame.
While playing you need to watch out for the stones - they are sharp and kill.
The game counts points and create (right now only) in session score rank.
The speed while playing increases, so watch out!
"""
import time

import Variables
import Snake
import Food


def game_loop():
    """
    The main loop of the game. It creates the snake, calls functions for drawing elements and checks key events.
    """

    snake = Snake.Snake()
    food = Food.Food()

    while True:
        for event in Variables.pygame.event.get():
            if event.type == Variables.pygame.QUIT:
                Variables.Functions.end_game()
            elif event.type == Variables.pygame.KEYDOWN:
                if event.key == Variables.pygame.K_UP:
                    snake.change_direction(Variables.UP)
                elif event.key == Variables.pygame.K_DOWN:
                    snake.change_direction(Variables.DOWN)
                elif event.key == Variables.pygame.K_LEFT:
                    snake.change_direction(Variables.LEFT)
                elif event.key == Variables.pygame.K_RIGHT:
                    snake.change_direction(Variables.RIGHT)
                elif event.key == Variables.pygame.K_SPACE:
                    Variables.Screens.pause(snake)

        Variables.screen.blit(Variables.surface, [0, 0])
        snake.move()
        Variables.Functions.check_eat(snake, food)
        food.draw()
        snake.draw(Variables.screen)
        Variables.Functions.score(snake.points)
        Variables.Functions.length(snake.length)
        Variables.pygame.display.update()
        if Variables.is_eaten:
            # that you can see the open mouth!
            time.sleep(.1)
            Variables.is_eaten = False
        if Variables.is_dead:
            Variables.Screens.lost()
        # it's getting harder and harder...
        Variables.clock.tick(Variables.fps + snake.length / 3)


if __name__ == '__main__':
    Variables.Screens.starting()
