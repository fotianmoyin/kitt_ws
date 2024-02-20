import pygame
import os
from importlib.resources import files


class Model:
    """
    汽车模型
    """
    def __init__(self, car) -> None:
        self.car = car
        self.win = car.win
        self.share_path = car.share_path
        self._load_model_image()

    def _load_model_image(self):
        model_path = os.path.join(self.share_path, "images/model.png")
        print(model_path)
        # 加载汽车图片
        model_image = pygame.image.load(model_path)
        model_rect = model_image.get_rect()
        self.model_image = pygame.transform.smoothscale(
            model_image, (model_rect.width / 6, model_rect.height / 6)
        )

    def update(self):
        model_image = pygame.transform.rotate(self.model_image, -self.car.world_angle)
        # 获取图片尺寸
        model_rect = model_image.get_rect()
        # 获取窗口尺寸，让图片居中显示
        win_rect = self.win.get_rect()
        model_rect.x = (win_rect.width - model_rect.width) / 2
        model_rect.y = (win_rect.height - model_rect.height) / 2
        # 在窗口的指定位置上绘制图片
        self.win.blit(model_image, model_rect)
