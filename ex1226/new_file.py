import pygame
import random
import warnings

# setuptools 경고 무시
warnings.filterwarnings("ignore", category=UserWarning)

# --- 1. 설정 및 환경 변수 ---
BLOCK_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = 10, 20
SIDEBAR_WIDTH = 200
GAME_WIDTH = BLOCK_SIZE * GRID_WIDTH
SCREEN_WIDTH = GAME_WIDTH + SIDEBAR_WIDTH
SCREEN_HEIGHT = BLOCK_SIZE * GRID_HEIGHT

COLOR_MAIN_BG = (30, 31, 40)
COLOR_SIDEBAR_BG = (45, 46, 60)
COLOR_GRID_LINE = (38, 39, 50)
WHITE = (245, 245, 245)

COLORS = {
    "I": (0, 200, 200), "O": (210, 210, 0), "T": (155, 40, 215),
    "S": (0, 200, 0), "Z": (215, 0, 0), "J": (0, 85, 220), "L": (220, 130, 0)
}

TETROMINOES = {
    "I": {"shape": [[1, 1, 1, 1]]}, "O": {"shape": [[1, 1], [1, 1]]},
    "T": {"shape": [[0, 1, 0], [1, 1, 1]]}, "S": {"shape": [[0, 1, 1], [1, 1, 0]]},
    "Z": {"shape": [[1, 1, 0], [0, 1, 1]]}, "J": {"shape": [[1, 0, 0], [1, 1, 1]]},
    "L": {"shape": [[0, 0, 1], [1, 1, 1]]}
}

# --- 2. 시각 효과 및 블록 그리기 ---
class Particle:
    def __init__(self, x, y, color, is_tetris=False):
        self.x, self.y = x, y
        self.color = color
        spd = 8 if is_tetris else 4
        self.vx, self.vy = random.uniform(-spd, spd), random.uniform(-spd, spd)
        self.gravity, self.life, self.age = 0.25, random.randint(20, 40), 0
        self.size = random.randint(3, 6)
    def update(self):
        self.x += self.vx; self.y += self.vy; self.vy += self.gravity; self.age += 1
    def draw(self, surf):
        alpha = max(0, 255 - (self.age * 255 // self.life))
        p_surf = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        p_surf.fill((*self.color, alpha))
        surf.blit(p_surf, (int(self.x), int(self.y)))

def draw_block(surf, x, y, color, size=BLOCK_SIZE, is_ghost=False):
    rect = (x, y, size, size)
    if is_ghost:
        pygame.draw.rect(surf, color, rect, 1)
        return
    bright, dark, bw = [min(c + 75, 255) for c in color], [max(c - 75, 0) for c in color], size // 8
    pygame.draw.rect(surf, dark, rect)
    pygame.draw.rect(surf, bright, (x, y, size - bw, size - bw))
    pygame.draw.rect(surf, color, (x + bw, y + bw, size - bw * 2, size - bw * 2))
    pygame.draw.rect(surf, (0, 0, 0), rect, 1)

# --- 3. 렌더링 시스템 ---
def render_all(board, cp, n_queue, hp, score, level, combo, is_game_over, is_paused, particles, flash_alpha, shake_offset, lv_up_timer):
    temp_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    temp_surf.fill(COLOR_SIDEBAR_BG)
    
    # 레벨 15 이상이면 배경색을 어두운 빨강으로 변경하여 경고 느낌 주기
    bg_color = (50, 20, 20) if level >= 15 else COLOR_MAIN_BG
    pygame.draw.rect(temp_surf, bg_color, (0, 0, GAME_WIDTH, SCREEN_HEIGHT))
    
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pygame.draw.rect(temp_surf, COLOR_GRID_LINE, (x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
    
    for y, row in enumerate(board):
        for x, color in enumerate(row):
            if color: draw_block(temp_surf, x * BLOCK_SIZE, y * BLOCK_SIZE, color)
    
    if not is_game_over:
        gy = get_ghost_y(board, cp)
        for y, row in enumerate(cp["shape"]):
            for x, cell in enumerate(row):
                if cell:
                    draw_block(temp_surf, (cp["x"]+x)*BLOCK_SIZE, (gy+y)*BLOCK_SIZE, cp["color"], is_ghost=True)
                    if cp["y"]+y >= 0: draw_block(temp_surf, (cp["x"]+x)*BLOCK_SIZE, (cp["y"]+y)*BLOCK_SIZE, cp["color"])

    for p in particles: p.draw(temp_surf)
    if flash_alpha > 0:
        f_surf = pygame.Surface((GAME_WIDTH, SCREEN_HEIGHT)); f_surf.fill((255,255,255))
        f_surf.set_alpha(flash_alpha); temp_surf.blit(f_surf, (0,0))

    sidebar_x = GAME_WIDTH + 25
    f_title, f_val = pygame.font.SysFont("arial", 16, bold=True), pygame.font.SysFont("consolas", 20, bold=True)

    # NEXT 큐
    temp_surf.blit(f_title.render("NEXT", True, WHITE), (sidebar_x, 20))
    for i, p_next in enumerate(n_queue):
        box_y = 45 + (i * 75)
        pygame.draw.rect(temp_surf, (35, 36, 45), (sidebar_x, box_y, 150, 65))
        shape, color, p_size = p_next["shape"], p_next["color"], 20
        bx, by = sidebar_x + (150 - len(shape[0])*p_size)//2, box_y + (65 - len(shape)*p_size)//2
        for sy, srow in enumerate(shape):
            for sx, scell in enumerate(srow):
                if scell: draw_block(temp_surf, bx+sx*p_size, by+sy*p_size, color, size=p_size)

    # HOLD
    hold_y = 285
    temp_surf.blit(f_title.render("HOLD", True, WHITE), (sidebar_x, hold_y))
    pygame.draw.rect(temp_surf, (35, 36, 45), (sidebar_x, hold_y + 25, 150, 80))
    if hp:
        shape, color, p_size = TETROMINOES[hp]["shape"], COLORS[hp], 20
        bx, by = sidebar_x + (150 - len(shape[0])*p_size)//2, hold_y + 25 + (80 - len(shape)*p_size)//2
        for sy, srow in enumerate(shape):
            for sx, scell in enumerate(srow):
                if scell: draw_block(temp_surf, bx+sx*p_size, by+sy*p_size, color, size=p_size)

    # SCORE & LEVEL
    sy = 410
    for l, v, c in [("SCORE", score, (0, 255, 180)), ("LEVEL", level, (255, 200, 0)), ("COMBO", combo, (255, 100, 100))]:
        temp_surf.blit(f_title.render(l, True, WHITE), (sidebar_x, sy))
        temp_surf.blit(f_val.render(str(v), True, c), (sidebar_x, sy + 22)); sy += 65

    if is_paused:
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA); overlay.fill((0, 0, 0, 180))
        temp_surf.blit(overlay, (0,0))
        txt = pygame.font.SysFont("arial", 50, bold=True).render("PAUSED", True, WHITE)
        temp_surf.blit(txt, (SCREEN_WIDTH//2 - txt.get_width()//2, SCREEN_HEIGHT//2 - 25))
    if is_game_over:
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA); overlay.fill((0, 0, 0, 200))
        temp_surf.blit(overlay, (0,0))
        g_txt = pygame.font.SysFont("arial", 40, bold=True).render("GAME OVER", True, (255, 50, 50))
        r_txt = pygame.font.SysFont("arial", 20).render("Press 'R' to Restart", True, WHITE)
        temp_surf.blit(g_txt, (SCREEN_WIDTH//2 - g_txt.get_width()//2, SCREEN_HEIGHT//2 - 50))
        temp_surf.blit(r_txt, (SCREEN_WIDTH//2 - r_txt.get_width()//2, SCREEN_HEIGHT//2 + 10))

    return temp_surf

# --- 4. 로직 함수 ---
def create_board(): return [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
def get_piece(name=None):
    n = name if name else random.choice(list(TETROMINOES.keys()))
    return {"name": n, "shape": TETROMINOES[n]["shape"], "color": COLORS[n],
            "x": GRID_WIDTH // 2 - len(TETROMINOES[n]["shape"][0]) // 2, "y": -len(TETROMINOES[n]["shape"])}
def is_valid_move(board, piece, adj_x=0, adj_y=0, new_shape=None):
    shape = new_shape if new_shape is not None else piece["shape"]
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                nx, ny = piece["x"] + x + adj_x, piece["y"] + y + adj_y
                if nx < 0 or nx >= GRID_WIDTH or ny >= GRID_HEIGHT: return False
                if ny >= 0 and board[ny][nx] is not None: return False
    return True
def get_ghost_y(board, piece):
    gy = piece["y"]
    while is_valid_move(board, piece, adj_y=(gy - piece["y"] + 1)): gy += 1
    return gy

# --- 5. 메인 루프 ---
def main():
    pygame.init(); screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris: Lv.15 Hell Edition")
    clock = pygame.time.Clock()

    def reset_game():
        return create_board(), get_piece(), [get_piece() for _ in range(3)], None, True, 0, 1, 0, 0, False, [], 0, 0, 0, 0, 0, False

    board, cp, n_queue, hp, can_hold, score, level, total_l, combo, is_game_over, particles, flash_alpha, drop_time, lock_timer, shake_intensity, lv_up_timer, is_paused = reset_game()
    key_time = {"left": 0, "right": 0, "down": 0}

    while True:
        dt = clock.tick(60)
        
        if not is_paused:
            if flash_alpha > 0: flash_alpha -= 8
            if shake_intensity > 0: shake_intensity -= 1
            if lv_up_timer > 0: lv_up_timer -= 1
            particles = [p for p in particles if p.age < p.life]
            for p in particles: p.update()

        if not is_game_over and not is_paused:
            # --- [난이도 핵심 수정] ---
            # 낙하 속도: 레벨 15에서 70ms (초당 약 14칸 낙하)
            fall_speed = max(70, 800 - (level - 1) * 52) 
            
            if is_valid_move(board, cp, adj_y=1):
                drop_time += dt; lock_timer = 0
                if drop_time > fall_speed: cp["y"] += 1; drop_time = 0
            else:
                lock_timer += dt
                # 바닥 유예 시간: 레벨 15에서 150ms (0.15초 안에 회전/이동해야 함)
                current_lock_delay = max(150, 500 - (level - 1) * 25)
                
                if lock_timer > current_lock_delay:
                    temp_b = [r[:] for r in board]
                    for y, row in enumerate(cp["shape"]):
                        for x, cell in enumerate(row):
                            if cell and cp["y"]+y >= 0: temp_b[cp["y"]+y][cp["x"]+x] = cp["color"]
                    
                    full_l = [i for i, r in enumerate(temp_b) if None not in r]
                    if full_l:
                        is_t = len(full_l) == 4
                        flash_alpha, shake_intensity = (180, 15) if is_t else (0, 7)
                        for ly in full_l:
                            for lx in range(GRID_WIDTH):
                                for _ in range(6): particles.append(Particle(lx*BLOCK_SIZE, ly*BLOCK_SIZE, temp_b[ly][lx], is_t))
                        board = [[None]*GRID_WIDTH for _ in range(len(full_l))] + [row for i, row in enumerate(temp_b) if i not in full_l]
                        combo += 1; score += ({1:100,2:300,3:500,4:800}[len(full_l)]*level) + (combo*50)
                        total_l += len(full_l)
                        # 레벨업: 15줄마다
                        if (total_l // 15) + 1 > level: level += 1; lv_up_timer, shake_intensity = 90, 20
                    else:
                        combo, board = 0, temp_b
                        if any(cell and cp["y"]+y < 0 for y, row in enumerate(cp["shape"]) for x, cell in enumerate(row)): is_game_over = True
                    
                    cp, n_queue, can_hold = n_queue.pop(0), n_queue + [get_piece()], True
                    n_queue = n_queue[:3] # 큐 길이 유지
                    if not is_valid_move(board, cp, adj_y=1): is_game_over = True
                    lock_timer = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p and not is_game_over: is_paused = not is_paused
                if not is_game_over and not is_paused:
                    if (event.key in [pygame.K_LSHIFT, pygame.K_c]) and can_hold:
                        old_name = cp["name"]
                        if hp is None:
                            cp, hp = n_queue.pop(0), old_name
                            n_queue.append(get_piece())
                        else:
                            cp, hp = get_piece(hp), old_name
                        can_hold = False
                    if event.key == pygame.K_UP:
                        rot = [list(r) for r in zip(*cp["shape"][::-1])]
                        for off in [0, -1, 1, -2, 2]:
                            if is_valid_move(board, cp, adj_x=off, new_shape=rot):
                                cp["x"] += off; cp["shape"] = rot; break
                    if event.key == pygame.K_SPACE:
                        cp["y"] = get_ghost_y(board, cp); lock_timer, shake_intensity = 600, 8
                if is_game_over and event.key == pygame.K_r:
                    board, cp, n_queue, hp, can_hold, score, level, total_l, combo, is_game_over, particles, flash_alpha, drop_time, lock_timer, shake_intensity, lv_up_timer, is_paused = reset_game()

        if not is_game_over and not is_paused:
            keys = pygame.key.get_pressed()
            for kn, ax, ay, kp in [("left", -1, 0, pygame.K_LEFT), ("right", 1, 0, pygame.K_RIGHT), ("down", 0, 1, pygame.K_DOWN)]:
                if keys[kp]:
                    if key_time[kn] == 0 or (key_time[kn] > 150 and (key_time[kn]-150) % 40 < dt):
                        if is_valid_move(board, cp, ax, ay): cp["x"] += ax; cp["y"] += ay
                    key_time[kn] += dt
                else: key_time[kn] = 0

        s_off = (random.randint(-shake_intensity, shake_intensity), random.randint(-shake_intensity, shake_intensity)) if shake_intensity > 0 else (0,0)
        view = render_all(board, cp, n_queue, hp, score, level, combo, is_game_over, is_paused, particles, flash_alpha, s_off, lv_up_timer)
        screen.fill((0,0,0)); screen.blit(view, s_off); pygame.display.flip()

if __name__ == "__main__": main()