import Variables
import Snake


class Food:
    """
    A class used to represent a food. Class is a singleton.

    Parameters:
    position ((int, int)):
        Tuple with position where food should appear.

    Methods:
    generate_food_pos(self)
        generates new food position. Makes sure that the position is not inside snake's body.
    """

    _singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(Food, cls).__new__(cls, *args, **kwargs)
        return cls._singleton

    def __init__(self):
        Food.generate_food_pos(self)

    def generate_food_pos(self):
        """
        generate_food_pos(self)
            Generates new food position. Makes sure that the position is not inside snake's body.

        Returns:
            position: Tuple with position where food should appear.
        """

        self.position = (
            Variables.random.randint(0, 10 * Variables.scale_factor - 1) * Variables.body_size + Variables.block_size,
            Variables.random.randint(0, 10 * Variables.scale_factor - 1) * Variables.body_size + int(
                Variables.block_size * 2.5))

        # checking if position of food do not overlap with body of snake. if it does - creating new food position
        for item in Snake.Snake().snake_arr:
            if item == self.position:
                return Food.generate_food_pos(self)
        return self.position

    def draw(self):
        """
        Function for drawing the food on the screen.
        """

        Variables.screen.blit(Variables.food, self.position)
