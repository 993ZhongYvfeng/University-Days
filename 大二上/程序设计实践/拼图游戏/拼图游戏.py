import random
import pygame

# 初始化游戏
pygame.init()
# 创建一个屏幕对象并设置窗口大小
screen = pygame.display.set_mode((1200, 600))
# 窗口标题
pygame.display.set_caption('myPuzzle')
#定义背景颜色为浅蓝色
bg_color=(0,191,255)
#定义成功后弹出的窗口

# 绘图地图
imgMap = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

# 判断胜利的地图
winMap = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]


# 游戏的单击事件
def click(x, y, map):
    # 进行上下交换
    if y - 1 >= 0 and map[y - 1][x] == 8:
        map[y][x], map[y - 1][x] = map[y - 1][x], map[y][x]
    elif y + 1 <= 2 and map[y + 1][x] == 8:
        map[y][x], map[y + 1][x] = map[y + 1][x], map[y][x]
    #  进行左右交换
    elif x - 1 >= 0 and map[y][x - 1] == 8:
        map[y][x], map[y][x - 1] = map[y][x - 1], map[y][x]
    elif x + 1 <= 2 and map[y][x + 1] == 8:
        map[y][x], map[y][x + 1] = map[y][x + 1], map[y][x]


# 打乱地图
def randMap(map):
    for i in range(1000):
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        click(x, y, map)


# 加载图片
img = pygame.image.load('./shili.jpg')
# 随机地图
randMap(imgMap)
# 游戏主循环
while True:
    for event in pygame.event.get():
        # 窗口的关闭事件
        if event.type == pygame.QUIT:
            exit()
        # 处理鼠标事件
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 当鼠标左键按下时
            if pygame.mouse.get_pressed() == (1,0,0):
                # 获得当前鼠标坐标
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # 若鼠标在操作范围内
                if mouse_x < 600 and mouse_y < 600:
                    # 判断鼠标点到了哪个图块
                    x = int(mouse_x / 200)
                    y = int(mouse_y / 200)
                    # 调用单击事件，进行图片交换
                    click(x, y, imgMap)
                    # 如果当前地图情况和胜利情况相同,就弹出胜利？？？
                    if imgMap == winMap:
                        #使用弹出图片的方式？？？？？
                        print("胜利了！")
    # 背景颜色填充成之前设定的浅蓝色
    screen.fill(bg_color)
    # 绘图
    for y in range(3):
        for x in range(3):
            i = imgMap[y][x]
            # 8号图块不用绘制
            if i == 8:
                continue
            # 计算绘图偏移量
            dx = (i % 3) * 200
            dy = (int(i / 3)) * 200
            #把原图有选择地切割后，贴到目标区域
            screen.blit(img, (x * 200, y * 200), (dx, dy, 200, 200))
    # 画参考图片
    screen.blit(img, (600, 0))
    # 刷新界面
    pygame.display.flip()

