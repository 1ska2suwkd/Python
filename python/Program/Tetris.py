import pygame
import random

# 초기화
pygame.init()

# 게임판 크기
GRID_WIDTH = 10  # 게임판의 블록 수 (가로)
GRID_HEIGHT = 20  # 게임판의 블록 수 (세로)

# 블록 크기 및 화면 크기
BLOCK_SIZE = 30
WIDTH = GRID_WIDTH * BLOCK_SIZE + 150  # 킵 영역 포함
HEIGHT = GRID_HEIGHT * BLOCK_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)  # 블록 테두리 색상
COLORS = {
    "I": (0, 255, 255),
    "O": (255, 255, 0),
    "T": (128, 0, 128),
    "S": (0, 255, 0),
    "Z": (255, 0, 0),
    "L": (255, 165, 0),
    "J": (0, 0, 255),
}

SHAPES = {
    "I": [[1, 1, 1, 1]],
    "O": [[1, 1], [1, 1]],
    "T": [[0, 1, 0], [1, 1, 1]],
    "S": [[0, 1, 1], [1, 1, 0]],
    "Z": [[1, 1, 0], [0, 1, 1]],
    "L": [[1, 0, 0], [1, 1, 1]],
    "J": [[0, 0, 1], [1, 1, 1]],
}

# 게임 속도
clock = pygame.time.Clock()
FPS = 60  # 화면 업데이트 속도
FONT = pygame.font.SysFont("Arial", 24)

# 최고 점수 저장
high_score = 0


class Tetris:
    def __init__(self):
        self.grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]  # 게임판 크기에 맞게 설정
        self.current_block = self.new_block()
        self.hold_block = None  # 킵된 블록
        self.hold_used = False  # 한 턴에 한 번만 킵 가능
        self.game_over = False
        self.score = 0

    def new_block(self):
        shape_name = random.choice(list(SHAPES.keys()))
        shape = SHAPES[shape_name]
        color = COLORS[shape_name]
        return {"shape": shape, "color": color, "name": shape_name, "x": GRID_WIDTH // 2 - len(shape[0]) // 2, "y": 0}

    def draw_background(self):
        """화면의 블록 이동 불가 영역을 흰색으로 설정"""
        # 킵 영역을 포함한 오른쪽 영역 흰색으로 표시
        pygame.draw.rect(screen, WHITE, (GRID_WIDTH * BLOCK_SIZE, 0, WIDTH - GRID_WIDTH * BLOCK_SIZE, HEIGHT))

    def draw_grid(self):
        """고정된 블록 그리기"""
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x]:  # 격자에 색상이 저장되어 있으면
                    rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                    pygame.draw.rect(screen, self.grid[y][x], rect)  # 블록 내부
                    pygame.draw.rect(screen, GRAY, rect, 2)  # 블록 테두리

    def draw_block(self):
        """현재 움직이는 블록 그리기"""
        for y, row in enumerate(self.current_block["shape"]):
            for x, cell in enumerate(row):
                if cell:
                    rect = pygame.Rect(
                        (self.current_block["x"] + x) * BLOCK_SIZE,
                        (self.current_block["y"] + y) * BLOCK_SIZE,
                        BLOCK_SIZE, BLOCK_SIZE
                    )
                    pygame.draw.rect(screen, self.current_block["color"], rect)  # 블록 내부
                    pygame.draw.rect(screen, GRAY, rect, 2)  # 블록 테두리

    def draw_hold_block(self):
        """킵된 블록을 검은색 선 상자로 표시"""
        hold_area_x = GRID_WIDTH * BLOCK_SIZE + 20  # 킵 영역 시작 X 위치
        hold_area_y = 80  # 킵 영역 시작 Y 위치
        hold_area_width = 4 * BLOCK_SIZE  # 킵 영역 너비
        hold_area_height = 4 * BLOCK_SIZE  # 킵 영역 높이

        # 킵 영역 배경 (흰색) 및 검은색 테두리
        pygame.draw.rect(screen, WHITE, (hold_area_x, hold_area_y, hold_area_width, hold_area_height))
        pygame.draw.rect(screen, BLACK, (hold_area_x, hold_area_y, hold_area_width, hold_area_height), 3)

        # 킵된 블록 표시
        if self.hold_block:
            start_x = hold_area_x + BLOCK_SIZE  # 중앙 정렬을 위한 x 시작점
            start_y = hold_area_y + BLOCK_SIZE  # 중앙 정렬을 위한 y 시작점
            for y, row in enumerate(self.hold_block["shape"]):
                for x, cell in enumerate(row):
                    if cell:
                        rect = pygame.Rect(start_x + x * BLOCK_SIZE, start_y + y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                        pygame.draw.rect(screen, self.hold_block["color"], rect)  # 블록 내부
                        pygame.draw.rect(screen, GRAY, rect, 2)  # 블록 테두리

    def move_block(self, dx, dy):
        self.current_block["x"] += dx
        self.current_block["y"] += dy
        if self.check_collision():
            self.current_block["x"] -= dx
            self.current_block["y"] -= dy
            return False
        return True

    def check_collision(self):
        """블록이 게임판 경계나 다른 블록과 충돌하는지 확인"""
        for y, row in enumerate(self.current_block["shape"]):
            for x, cell in enumerate(row):
                if cell:
                    grid_x = self.current_block["x"] + x
                    grid_y = self.current_block["y"] + y
                    # 벽 충돌 확인
                    if grid_x < 0 or grid_x >= GRID_WIDTH or grid_y >= GRID_HEIGHT:
                        return True
                    # 다른 블록과의 충돌 확인
                    if grid_y >= 0 and self.grid[grid_y][grid_x]:
                        return True
        return False

    def rotate_block(self):
        """현재 블록을 회전"""
        shape = self.current_block["shape"]
        rotated = [list(row) for row in zip(*shape[::-1])]  # 블록을 오른쪽으로 90도 회전
        original_x = self.current_block["x"]
        original_shape = self.current_block["shape"]

        # 회전 적용
        self.current_block["shape"] = rotated

        # 충돌이 발생하면 회전 취소
        if self.check_collision():
            self.current_block["shape"] = original_shape
            self.current_block["x"] = original_x

    def lock_block(self):
        """현재 블록을 게임판에 고정"""
        for y, row in enumerate(self.current_block["shape"]):
            for x, cell in enumerate(row):
                if cell:
                    grid_x = self.current_block["x"] + x
                    grid_y = self.current_block["y"] + y
                    if grid_y >= 0:
                        self.grid[grid_y][grid_x] = self.current_block["color"]
        self.clear_lines()
        self.current_block = self.new_block()
        self.hold_used = False  # 블록 고정 후 다시 킵 가능
        if self.check_collision():  # 새 블록이 충돌하면 게임 오버
            self.game_over = True

    def clear_lines(self):
        """완성된 줄을 제거"""
        lines_to_clear = [i for i, row in enumerate(self.grid) if all(row)]
        num_lines = len(lines_to_clear)

        if num_lines > 0:
            for i in lines_to_clear:
                self.grid.pop(i)
                self.grid.insert(0, [0] * GRID_WIDTH)

            # 점수 계산
            if num_lines == 1:
                self.score += 5
            else:
                self.score += 10 + (num_lines - 2) * 5

    def hard_drop(self):
        """블록을 즉시 아래로 떨어뜨림"""
        while self.move_block(0, 1):
            pass  # 블록이 더 이상 내려갈 수 없을 때까지 이동
        self.lock_block()

    def hold_current_block(self):
        """현재 블록을 킵하거나 교체"""
        if self.hold_used:
            return  # 한 턴에 한 번만 킵 가능
        if self.hold_block is None:
            # 킵된 블록이 없을 경우 현재 블록을 킵
            self.hold_block = self.current_block
            self.current_block = self.new_block()
        else:
            # 킵된 블록과 현재 블록을 교체
            self.hold_block, self.current_block = self.current_block, self.hold_block
            self.current_block["x"] = GRID_WIDTH // 2 - len(self.current_block["shape"][0]) // 2
            self.current_block["y"] = 0
        self.hold_used = True


def game_over_screen(score, high_score):
    """게임 오버 화면"""
    screen.fill(BLACK)
    game_over_text = FONT.render("GAME OVER", True, WHITE)
    score_text = FONT.render(f"Your Score: {score}", True, WHITE)
    high_score_text = FONT.render(f"High Score: {high_score}", True, WHITE)
    restart_text = FONT.render("Press R to Restart", True, WHITE)

    screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 100))
    screen.blit(score_text, (WIDTH // 2 - 80, HEIGHT // 2 - 50))
    screen.blit(high_score_text, (WIDTH // 2 - 80, HEIGHT // 2))
    screen.blit(restart_text, (WIDTH // 2 - 100, HEIGHT // 2 + 50))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False


def main():
    global high_score
    running = True

    while running:
        tetris = Tetris()
        last_fall_time = pygame.time.get_ticks()
        fall_speed = 500  # 블록이 떨어지는 간격(ms)

        while not tetris.game_over:
            screen.fill(BLACK)

            # 배경 및 킵 영역 그리기
            tetris.draw_background()
            tetris.draw_grid()
            tetris.draw_block()
            tetris.draw_hold_block()


            # 점수 표시
            score_text = FONT.render(f"Score: {tetris.score}", True, BLACK)
            high_score_text = FONT.render(f"High Score: {high_score}", True, BLACK)
            score_x = WIDTH - 150  # 오른쪽 여백을 고려한 X 위치
            screen.blit(score_text, (score_x, 10))  # 오른쪽 상단에 출력
            screen.blit(high_score_text, (score_x, 40))  # 오른쪽 상단에 출력


            # 현재 시간
            current_time = pygame.time.get_ticks()

            # 블록 자동 낙하
            if current_time - last_fall_time > fall_speed:
                if not tetris.move_block(0, 1):
                    tetris.lock_block()
                last_fall_time = current_time

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    tetris.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        tetris.move_block(-1, 0)
                    if event.key == pygame.K_RIGHT:
                        tetris.move_block(1, 0)
                    if event.key == pygame.K_DOWN:
                        if not tetris.move_block(0, 1):
                            tetris.lock_block()
                    if event.key == pygame.K_UP:  # 회전
                        tetris.rotate_block()
                    if event.key == pygame.K_SPACE:  # 하드 드롭
                        tetris.hard_drop()
                    if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:  # 블록 킵
                        tetris.hold_current_block()

            pygame.display.flip()
            clock.tick(FPS)

        # 게임 오버 처리
        high_score = max(high_score, tetris.score)
        game_over_screen(tetris.score, high_score)


if __name__ == "__main__":
    main()
    pygame.quit()
