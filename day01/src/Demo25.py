# py游戏库，完成一个进度条   观察while循环

import pygame
import sys
import time

pygame.init()

screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("10秒进度条")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 120, 255)
GREEN = (0, 255, 0)

# 尝试使用中文字体
try:
    font = pygame.font.SysFont("simhei", 36)  # 黑体
    small_font = pygame.font.SysFont("simhei", 24)
except:
    font = pygame.font.Font(None, 36)
    small_font = pygame.font.Font(None, 24)

# 进度条参数
progress_bar_x = 100
progress_bar_y = 180
progress_bar_width = 400
progress_bar_height = 30
current_progress = 0

start_time = time.time()
duration = 10

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    elapsed_time = time.time() - start_time
    current_progress = min(elapsed_time / duration * 100, 100)

    screen.fill(WHITE)

    # 绘制进度条
    pygame.draw.rect(screen, BLACK, (progress_bar_x, progress_bar_y, progress_bar_width, progress_bar_height), 2)
    progress_width = int(progress_bar_width * current_progress / 100)
    pygame.draw.rect(screen, BLUE, (progress_bar_x, progress_bar_y, progress_width, progress_bar_height))

    # 显示中文文本
    progress_text = font.render(f"进度: {int(current_progress)}%", True, BLACK)
    screen.blit(progress_text, (progress_bar_x + progress_bar_width // 2 - 50, progress_bar_y - 40))

    time_text = small_font.render(f"时间: {min(elapsed_time, duration):.1f}/{duration}秒", True, BLACK)
    screen.blit(time_text, (progress_bar_x + progress_bar_width // 2 - 70, progress_bar_y + progress_bar_height + 20))

    if current_progress >= 100:
        complete_text = font.render("完成!", True, GREEN)
        screen.blit(complete_text,
                    (progress_bar_x + progress_bar_width // 2 - 30, progress_bar_y + progress_bar_height + 60))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

print("跳出循环...")

pygame.quit()
sys.exit()