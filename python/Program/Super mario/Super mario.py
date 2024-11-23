import pygame
import sys
import random
import os

# 현재 작업 디렉토리를 'Super mario' 폴더로 변경
os.chdir(r"C:\Users\chaeheon\Desktop\vs code 프로젝트\python\python\Program\Super mario")

# Pygame 초기화
pygame.init()

# 화면 크기 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Infinite Super Mario")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# FPS 설정
clock = pygame.time.Clock()
FPS = 120

# 중력 및 점프 설정
gravity = 1  # 중력
jump_height = 15  # 점프 높이

# 폰트 설정
pygame.font.init()
font = pygame.font.SysFont("Arial", 36)  # 기본 폰트
game_over_font = pygame.font.SysFont("Arial", 50, bold=True)  # 게임 오버 폰트

# 이미지 로드
mario_image = pygame.image.load("mario.png")
mario_image = pygame.transform.scale(mario_image, (50, 50))
background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
enemy_image = pygame.image.load("enemy.png")
enemy_image = pygame.transform.scale(enemy_image, (40, 40))
coin_image = pygame.image.load("coin.png")
coin_image = pygame.transform.scale(coin_image, (30, 30))

# 전역 변수
player_width, player_height = 50, 50
platform_width = 200
platform_gap = 300
score = 0
high_score = 0  # 최고 기록
game_active = True  # 게임 활성화 여부

def reset_game():
    """게임 초기화"""
    global player_x, player_y, player_speed, player_velocity_y, jump_count
    global camera_x, platforms, enemies, coins, score, game_active
    
    # 캐릭터 초기 설정
    player_x = 100
    player_y = HEIGHT - 200
    player_speed = 5
    player_velocity_y = 0
    jump_count = 2  # 이단 점프 가능 횟수 초기화

    # 카메라 초기화
    camera_x = 0

    # 플랫폼, 적, 코인 초기화
    platforms = [pygame.Rect(0, HEIGHT - 50, platform_width, 10)]  # 바닥 플랫폼
    enemies = []
    coins = []
    score = 0
    game_active = True
    generate_random_platforms(200, count=7)

def generate_random_platforms(start_x, count=5):
    """랜덤 플랫폼과 적/코인 생성"""
    for i in range(count):
        # 플랫폼 생성
        platform_x = start_x + i * platform_gap
        platform_y = random.randint(300, HEIGHT - 100)
        platforms.append(pygame.Rect(platform_x, platform_y, platform_width, 10))
        
        # 적 생성
        if random.random() < 0.5:  # 50% 확률로 적 생성
            enemies.append({"rect": pygame.Rect(platform_x + platform_width // 2, platform_y - 40, 40, 40), "direction": -1})
        
        # 코인 생성
        if random.random() < 0.7:  # 70% 확률로 코인 생성
            coins.append(pygame.Rect(platform_x + platform_width // 4, platform_y - 30, 30, 30))

def game_over():
    """게임 오버 화면"""
    global score, high_score, game_active

    # 최고 기록 업데이트
    if score > high_score:
        high_score = score

    # 게임 활성화 상태를 False로 설정
    game_active = False

    # 화면 표시
    screen.fill(WHITE)
    game_over_text = game_over_font.render("GAME OVER", True, RED)
    score_text = font.render(f"Score: {score}", True, BLACK)
    high_score_text = font.render(f"High Score: {high_score}", True, BLACK)
    restart_text = font.render("Press R to Restart", True, BLACK)

    # 화면에 텍스트 표시
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 100))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - 30))
    screen.blit(high_score_text, (WIDTH // 2 - high_score_text.get_width() // 2, HEIGHT // 2 + 30))
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 90))
    pygame.display.flip()

# 게임 초기화
reset_game()

# 게임 루프
running = True
while running:
    screen.blit(background_image, (0, 0))  # 배경 그리기

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not game_active and event.type == pygame.KEYDOWN and event.key == pygame.K_r:  # R 키로 게임 재시작
            reset_game()
        if game_active and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and jump_count > 0:  # 점프 키 처리
                player_velocity_y = -jump_height
                jump_count -= 1  # 점프 횟수 감소

    if game_active:
        # 키 입력 처리 (이동)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        # 중력 적용
        player_velocity_y += gravity
        player_y += player_velocity_y

        # 플랫폼 충돌
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        on_ground = False
        for platform in platforms:
            if player_rect.colliderect(platform) and player_velocity_y > 0:
                player_y = platform.top - player_height
                player_velocity_y = 0
                jump_count = 2  # 점프 횟수 초기화
                on_ground = True
                break

        # 바닥 충돌 (떨어지면 게임 오버)
        if player_y > HEIGHT:
            game_over()

        # 화면 경계 처리
        player_x = max(0, player_x)

        # 카메라 이동
        if player_x > camera_x + WIDTH // 2:
            camera_x += player_speed

        # 새로운 플랫폼 생성 (무한맵 구현)
        while camera_x + WIDTH > platforms[-1].x:
            generate_random_platforms(platforms[-1].x + platform_gap, count=1)

        # 적 이동 및 제거
        for enemy in enemies[:]:
            enemy["rect"].x += enemy["direction"] * 2
            if enemy["rect"].x < camera_x or enemy["rect"].x > camera_x + WIDTH:
                enemy["direction"] *= -1

            # 적 충돌 처리
            if player_rect.colliderect(enemy["rect"]):
                if player_y + player_height <= enemy["rect"].y + 10:  # 캐릭터가 위에서 적을 밟음
                    enemies.remove(enemy)
                    score += 20  # 점수 추가
                    player_velocity_y = -jump_height // 2  # 점프 효과
                else:
                    game_over()  # 적과 부딪히면 게임 오버

        # 코인 충돌 처리
        for coin in coins[:]:
            if player_rect.colliderect(coin):
                coins.remove(coin)
                score += 10

        # 화면에 그리기
        # 캐릭터
        screen.blit(mario_image, (player_x - camera_x, player_y))

        # 플랫폼
        for platform in platforms:
            pygame.draw.rect(screen, BLACK, (platform.x - camera_x, platform.y, platform.width, platform.height))

        # 적
        for enemy in enemies:
            screen.blit(enemy_image, (enemy["rect"].x - camera_x, enemy["rect"].y))

        # 코인
        for coin in coins:
            screen.blit(coin_image, (coin.x - camera_x, coin.y))

        # 점수 표시
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

    # 게임 오버 화면 표시
    if not game_active:
        game_over()

    # 화면 업데이트
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
