import pygame
import sys
import os
import getopt
from ament_index_python.packages import get_package_share_directory

def run_as_debug() -> bool:
    """
    是否传递了参数debug
    """
    debug = False
    # 获取文件名（含后缀）
    name = os.path.basename(__file__)
    try:
        """
        options, args = getopt.getopt(args, shortopts, longopts=[])

        参数args：一般是sys.argv[1:]。过滤掉sys.argv[0]，它是执行脚本的名字，不算做命令行参数。
        参数shortopts：短格式分析串。例如："hp:i:"，h后面没有冒号，表示后面不带参数；p和i后面带有冒号，表示后面带参数。
        参数longopts：长格式分析串列表。例如：["help", "ip=", "port="]，help后面没有等号，表示后面不带参数；ip和port后面带等号，表示后面带参数。

        返回值options是以元组为元素的列表，每个元组的形式为：(选项串, 附加参数)，如：('-i', '192.168.0.1')
        返回值args是个列表，其中的元素是那些不含'-'或'--'的参数。
        """
        opts, args = getopt.getopt(sys.argv[1:], "hd:", ["help", "debug"])
        # 处理 返回值options是以元组为元素的列表。
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print(f"{name} -d")
                print(f"or: {name} --debug")
                sys.exit()
            elif opt in ("-d", "--debug"):
                debug = True
        if debug:
            print("debug模式")

        # 打印 返回值args列表，即其中的元素是那些不含'-'或'--'的参数。
        for i in range(0, len(args)):
            print("参数 %s 为：%s" % (i + 1, args[i]))
    except getopt.GetoptError:
        print(f"Error: {name} -d")
        print(f"   or: {name} --debug")
    return debug

if run_as_debug():
    from car_part.model import Model
    from car_part.map import Map
else:
    from kitt.car_part.model import Model
    from kitt.car_part.map import Map

class Car:
    def __init__(self) -> None:
        """初始化窗口并加载显示资源"""
        pygame.init()

        if run_as_debug():
            self.share_path = os.path.join(os.path.dirname(__file__), "../resource")
        else:
            self.share_path = get_package_share_directory("kitt")

        # 设置窗口大小
        self.win = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
        # 设置窗口标题
        pygame.display.set_caption("Car")
        self.world_x = float(0)  # 车世界坐标x
        self.world_y = float(0)  # 车世界坐标y
        self.model = Model(self)
        self.map = Map(self)
        pass

    def run(self):
        """运行模拟器"""
        while True:
            self._check_events()
            self._update_win()

    def _check_events(self):
        """监视键盘、鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_win(self):
        """更新窗口显示"""
        color = (150, 150, 150)
        # 给窗口填充背景色
        self.win.fill(color=color)
        # 更新地图
        self.map.update()
        # 更新汽车模型
        self.model.update()
        # 让最近绘制的窗口可见
        pygame.display.flip()

    def winx_to_worldx(self, win_x: int) -> int:
        """
        窗口坐标x转换为世界坐标x
        参数：
            win_x：窗口坐标x
        返回：
            世界坐标x
        """
        win_width = self.win.get_rect().width
        world_left = int(self.world_x - win_width / 2)
        world_x = world_left + win_x
        return world_x

    def winy_to_worldy(self, win_y) -> int:
        """
        窗口坐标y转换为世界坐标y
        参数：
            win_y：窗口坐标y
        返回：
            世界坐标y
        """
        win_height = self.win.get_rect().height
        world_top = int(self.world_y + win_height / 2)
        world_y = world_top + win_y
        return world_y

    def win_rect_to_world_rect(self, win_rect) -> pygame.Rect:
        """
        窗口坐标矩形转换为世界坐标矩形
        参数：
            win_rect：窗口坐标矩形
        返回：
            世界坐标矩形
        """
        world_x = self.winx_to_worldx(win_rect.x)
        world_y = self.winy_to_worldy(win_rect.y)
        world_rect = pygame.Rect(world_x, world_y, win_rect.width, win_rect.height)
        return world_rect

def main():
    """创建模拟器，并运行"""
    car = Car()
    car.run()


if __name__ == '__main__':
    main()
