import Variables


class Snake:
    """
    A class used to represent a Snake. Class is a singleton.

    Attributes:
        length (int): Length of the snake as an integer value.
        snake_arr ([(int, int), ...]): Array with locations of all body parts of the snake.
        direction ((int, int)): Tuple with coordinates for snake movement.
        points (int): Number of points user collected


    Methods:
        get_head_position(self)
            Returns the position of the head.
        start_val(self)
            Setting the start values for the snake.
        reset_snake(self)
            Calls the function for setting start values and restart the game.
         change_direction(self, point)
            Sets the new direction, unless it is not opposite to actual one. Uses queue for saving moves.
        def move(self)
            Implements movement of the snake. Checks if after the movement snake did not die.
            Removes moves from the queue, when move is done.
        def draw(self, surface)
            Draws snake's head and body on to the canvas.
    """

    _singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(Snake, cls).__new__(cls, *args, **kwargs)
        return cls._singleton

    def init(self):
        self.start_val()

    def get_head_position(self):
        """
        Returns the position of the head.

        Returns:
            Position of the head.
        """

        return self.snake_arr[0]

    def start_val(self):
        """
        Setting the start values for the snake.
        """

        Variables.is_dead = False
        Variables.starting = False
        self.length = 3
        self.snake_arr = [(3 * Variables.block_size, 3 * Variables.block_size),
                          (3 * Variables.block_size - Variables.body_size , 3 * Variables.block_size),
                          (3 * Variables.block_size - 2 * Variables.body_size , 3 * Variables.block_size)]
        self.direction = Variables.RIGHT
        Variables.x_tmp = 1
        Variables.y_tmp = 0
        self.points = 0

    def reset_snake(self):
        """
        Calls the function for setting start values and restart the game.
        """

        Snake.start_val(self)
        Variables.Main.game_loop()

    def change_direction(self, point):
        """
        Sets the new direction, unless it is not opposite to actual one. Uses queue for saving moves.

        Args:
            point ((int, int)): Tuple with coordinates for snake movement.

        Returns:
            In case given direction is opposite to current one - does nothing
        """

        # checking if given direction is not opposite to actual one
        if (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point
            Variables.q.put(point)

    def move(self):
        """
        Implements movement of the snake. Checks if after the movement snake did not die.
        Removes moves from the queue, when move is done.
        """

        head_pos = self.snake_arr[0]
        if not Variables.q.empty():
            x,y = Variables.q.get()
            Variables.x_tmp = x
            Variables.y_tmp = y
        else:
            x = Variables.x_tmp
            y = Variables.y_tmp
        # implementing movement
        moved_head_x = head_pos[0] + x * Variables.body_size
        moved_head_y = head_pos[1] + y * Variables.body_size

        # checking collision with borders
        if ((moved_head_x >= Variables.block_size * 11)
            and (Variables.block_size * 5 <= moved_head_y < Variables.block_size * 10)) \
            or ((moved_head_x < Variables.block_size)
                and (Variables.block_size * 5 <= moved_head_y < Variables.block_size * 10)) \
            or ((moved_head_y >= 12.5 * Variables.block_size) and (moved_head_x < 5 * Variables.block_size))\
            or ((moved_head_y < 2.5 * Variables.block_size) and (moved_head_x < 5 * Variables.block_size)):
                Variables.Functions.died()
        elif moved_head_x >= Variables.block_size * 11 \
                and (moved_head_y < Variables.block_size * 5 or moved_head_y >= Variables.block_size * 10):
            moved_head_x -= Variables.block_size * 10
        elif moved_head_x < Variables.block_size \
                and (moved_head_y < Variables.block_size * 5 or moved_head_y >= Variables.block_size * 10):
            moved_head_x += Variables.block_size * 10
        elif moved_head_y < Variables.block_size * 2.5 and moved_head_x >= Variables.block_size * 5:
            moved_head_y += Variables.block_size * 10
        elif moved_head_y >= Variables.block_size * 12.5 and moved_head_x >= Variables.block_size * 5:
            moved_head_y -= Variables.block_size * 10

        # assigning new head position to head
        moved_head_pos = (moved_head_x, moved_head_y)

        # self intersection - loosing
        if moved_head_pos in self.snake_arr[1:]:
            Variables.Functions.died()
        else:
            # adding new head
            self.snake_arr.insert(0, moved_head_pos)
            if len(self.snake_arr) > self.length:
                # removing old tail
                self.snake_arr.pop()

    def draw(self, surface):
        """
        Draws snake's head and body on to the canvas.

        Args:
            surface: Element to be drawn on to the canvas.
        """

        for p in self.snake_arr[1:]:
            Variables.pygame.draw.circle(surface, Variables.orange, (p[0] + int(Variables.body_size / 2), p[1] + int(Variables.body_size / 2)), int(Variables.body_size / 2))
        if not Variables.is_dead:
            if not Variables.is_eaten:
                Variables.screen.blit(Variables.head, self.snake_arr[0])
            elif Variables.is_eaten:
                Variables.screen.blit(Variables.head_eat, self.snake_arr[0])
        else:
            Variables.screen.blit(Variables.head_dead, self.snake_arr[0])



