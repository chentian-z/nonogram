import pygame
import sys
from build import build_matrix, row_index, column_index, print_matrix


# 初始化界面
pygame.init()
screen = pygame.display.set_mode((960, 640))
pygame.display.set_caption('nonogram')


def draw_background():
    # white background
    screen.fill((255, 255, 255))

    # 画网格
    pos = 210
    while pos <=600 :
        pygame.draw.line(screen, (192,192,192), (280, pos), (730, pos),3)
        if pos == 300 or pos == 450:
            pos += 60
        else:
            pos += 30
    pos = 310
    while pos <= 700:
        pygame.draw.line(screen, (192, 192, 192), (pos, 180), (pos, 630), 3)
        if pos == 400 or pos == 550:
            pos += 60
        else:
            pos += 30

    pygame.draw.rect(screen, (0, 0, 0), (280, 180, 450, 150), 3)
    pygame.draw.rect(screen, (0, 0, 0), (280, 330, 450, 150), 3)
    pygame.draw.rect(screen, (0, 0, 0), (280, 480, 450, 150), 3)
    pygame.draw.rect(screen, (0, 0, 0), (280, 180, 150, 450), 3)
    pygame.draw.rect(screen, (0, 0, 0), (430, 180, 150, 450), 3)
    pygame.draw.rect(screen, (0, 0, 0), (580, 180, 150, 450), 3)
    pygame.draw.rect(screen, (0, 0, 0), (280, 180, 454, 454), 5)


def draw_row_index():
    for i in range(15):
        j = 0
        for index in row_indexs[i][::-1]:
            txt = index_font.render(str(index), True, (0, 0, 0))
            x, y = 250 - 30*j, 180 + 30*i
            j += 1
            screen.blit(txt, (x, y))


def draw_column_index():
    for i in range(15):
        j = 0
        for index in column_indexs[i][::-1]:
            txt = index_font.render(str(index), True, (0, 0, 0))
            x, y = 290 + 30*i, 150 - 30*j
            j += 1
            screen.blit(txt, (x,y))


# 计算鼠标所在坐标值在第几行第几列个方块上
def get_cub_index(x, y):
    cub_j = int((x - 280) / 30)
    cub_i = int((y - 180) / 30)
    return cub_j, cub_i


def draw_choose():
    j, i = cub_j, cub_i
    if _matrix[j][i] == 0:
        pygame.draw.rect(screen, (255, 255, 255), (cub_j * 30 + 282, cub_i * 30 + 182, 27, 27), 0)
    elif _matrix[cub_j][cub_i] == 2:
        pygame.draw.rect(screen, (255, 255, 255), (cub_j * 30 + 282, cub_i * 30 + 182, 27, 27), 0)
        point1 = (cub_j * 30 + 280 + 5, cub_i * 30 + 180 + 5)
        point2 = (cub_j * 30 + 280 - 5 + 30, cub_i * 30 + 180 + 5)
        point3 = (cub_j * 30 + 280 + 5, cub_i * 30 + 180 - 5 + 30)
        point4 = (cub_j * 30 + 280 - 5 + 30, cub_i * 30 + 180 - 5 + 30)
        pygame.draw.line(screen, (8,46,84), point1, point4, 3)
        pygame.draw.line(screen, (8,46,84), point2, point3, 3)
    elif _matrix[cub_j][cub_i] == 1:
        pygame.draw.rect(screen, (8, 46, 84), (cub_j * 30 + 282, cub_i * 30 + 182, 27, 27), 0)


def draw_switch(switch_status):
    pos = (80, 100)
    if switch_status == 1:
        screen.blit(switch_on, pos)
    elif switch_status == 0:
        screen.blit(switch_off, pos)


def get_switch_status(switch_status):
    if switch_status == 1:
        return 0
    elif switch_status == 0:
        return 1


def get_value(j, i):
    if _matrix[j][i] == 0:
        if switch_status == 1:
            _matrix[j][i] = 1
        elif switch_status == 0:
            _matrix[j][i] =2
    elif _matrix[j][i] == 1:
        if switch_status == 0:
            _matrix[j][i] = 2
        elif switch_status == 1:
            _matrix[j][i] = 0
    elif _matrix[j][i] == 2:
        if switch_status == 1:
            _matrix[j][i] = 1
        elif switch_status == 0:
            _matrix[j][i] = 0
    return _matrix[j][i]


def check_matrix():
    for i in _matrix:
        for j in i:
            if i[j] == 2:
                i[j] = 0
    if matrix == Matrix or _matrix == Matrix:
        # victory()
        return True
    else: return False


def victory():
    screen.fill((255, 255, 255))
    font1 = pygame.font. SysFont('Arial', 60)
    font2 = pygame.font. SysFont('Algerian', 80)
    txt1 = font1.render('COMPLETE', True, (0, 0, 0))
    txt2 = font2.render('CONGRATULATIONS!', True, (0, 0, 0))
    x1, y1 = 350, 200
    x2, y2 = 115, 340
    # pos1 = 375, 450
    pos2 = 375, 550
    screen.blit(txt1,(x1, y1))
    screen.blit(txt2,(x2, y2))
    # screen.blit(play_again, pos1)
    screen.blit(quit_game, pos2)


# def debug():
#     on = pygame.image.load('blank.png').convert_alpha()
#     screen.blit(on, (0,0))
#     font1 = pygame.font. SysFont('Times', 10)
#     txt1 = font1.render(str(check_matrix()), True, (0, 0, 0))
# #     j, i = cub_j, cub_i
# #     block = _matrix[j][i]
# #     txt2 = font1.render(str(block), True, (0, 0, 0))
#     x1,y1 = 10, 10
# #     x2,y2 = 30, 10
#     screen.blit(txt1, (x1, y1))
#     screen.blit(txt2, (x2, y2))
#     txt2 = font1.render(str(_matrix), )


if __name__ == "__main__":
    Matrix = build_matrix()                         # 生成谜题
    row_indexs = row_index(Matrix)                  # 计算矩阵行系数
    column_indexs = column_index(Matrix)            # 计算矩阵列系数
    index_font = pygame.font.SysFont('times', 20)
    matrix = [[0] * 15 for i in range(15)]          # 记录格的状态 0为空白， 1为涂黑， 2为划叉
    _matrix = [[0] * 15 for i in range(15)]         # 初始化解题矩阵填入的答案

    cub_i, cub_j = -1000, -10000                    # 初始化鼠标位置
    switch_on = pygame.image.load('switch_on.png').convert_alpha()
    switch_off = pygame.image.load('switch_off.png').convert_alpha()
    quit_game = pygame.image.load('quit.png').convert_alpha()
    switch_status = 1                               # 初始化开关状态，置为1
    block_status = 0                                # 初始化状态方块，置为0

    draw_background()                               #绘制网格背景
    draw_row_index()                                # 绘制行系数
    draw_column_index()                             # 绘制列系数
    print_matrix(Matrix)                            # 在控制台上打印谜题矩阵，即答案

    # 主循环
    isRuning = True
    while isRuning:
        for event in pygame.event.get():
            # 关闭程序窗口则程序停止
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                isRuning = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:      # 获取鼠标点击操作
                success = check_matrix()                    # 检查游戏是否胜利
                if success:                                 # 如果游戏胜利，则显示胜利界面，
                    victory()       # victory 放在这里则正确后再点击一下达到胜利页面
                    #如果鼠标点击结束游戏按钮，则程序结束
                    if 370 < event.pos[0] < 370+228 and 550 < event.pos[1] < 550+68:
                        pygame.quit()
                        sys.exit()
                else:
                    # 如果还没有胜利， 则通过鼠标点击的方块位置方块状态和开关状态进行游戏操作
                    if 80 < event.pos[0] < 180 and 100 < event.pos[1] < 165:
                        # 点击开关图标则切换开关状态
                        switch_status = get_switch_status(switch_status)
                    if 280 < event.pos[0] < 730 and 180 < event.pos[1] < 630 and \
                            event.pos[0] - 280 % 30 != 0 and (event.pos[1] - 180) % 30 != 0:
                        # 点击方块范围则对该方块进行相应操作
                        # 获取鼠标所在方块坐标
                        cub_j, cub_i = get_cub_index(event.pos[0], event.pos[1])
                        matrix[cub_i][cub_j] = switch_status            # 更新开关状态矩阵
                        _matrix[cub_j][cub_i] = get_value(cub_j, cub_i) # 更新解题矩阵
                        draw_choose()                                   # 绘制此次操作
                        # debug()
        cub_i, cub_j = -1000, -10000
        draw_switch(switch_status)                                      # 绘制开关图标
        success = check_matrix()                                        # 判断是否胜利
        # if(success): victory() #victory 放在这里则正确后立即达到胜利页面
        pygame.display.flip()                                           # 更新绘制屏幕

