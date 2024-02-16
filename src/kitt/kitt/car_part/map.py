import pygame


class Map:
    """
    地图
    """

    def __init__(self, car):
        self.car = car
        self.win = car.win
        self.grid_color = (200, 200, 200)
        self.grid_width, self.grid_height = 50, 50
        pass

    def update(self):
        win_rect = self.win.get_rect()
        world_rect = self.car.win_rect_to_world_rect(win_rect)
        offset_y = world_rect.y % self.grid_height
        row_numbers = win_rect.height // self.grid_height
        for row_number in range(row_numbers + 1):
            row_y = offset_y + row_number * self.grid_height
            pygame.draw.line(
                self.win, self.grid_color, (0, row_y), (win_rect.width, row_y)
            )
        offset_x = world_rect.x % self.grid_width
        column_numbers = win_rect.width // self.grid_width
        for column_number in range(column_numbers + 2):
            column_x = -offset_x + column_number * self.grid_width
            pygame.draw.line(
                self.win, self.grid_color, (column_x, 0), (column_x, win_rect.height)
            )
        pass
