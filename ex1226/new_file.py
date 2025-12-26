import pygame
import random
import warnings
import os
import sys
import winsound

# setuptools 경고 무시
warnings.filterwarnings("ignore", category=UserWarning)

# --- 경로 및 파일명 설정 ---
if getattr(sys, 'frozen', False):
    BASE_PATH = sys._MEIPASS
else:
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))
MUSIC_DIR = os.path.join(BASE_PATH, "music")

# BGM 및 효과음 파일명
NORMAL_BGM = "03. A-Type Music (Korobeiniki).mp3"
HIDDEN_BGM = "Suisei's Tetris.mp3"
LEVEL_UP_SOUND_PATH = os.path.join(MUSIC_DIR, "mixkit-game-level-completed-2059.wav")
LINE_CLEAR_SOUND_PATH = os.path.join(MUSIC_DIR, 
    "A quick, ascending chime for a single line clear in Tetris.-edited-2025-12-26T15-09-09.mp3")
HARD_DROP_SOUND_PATH = os.path.join(MUSIC_DIR, 
    "A subtle, percussive thud for a Tetris block landing.-edited-2025-12-26T15-08-00.wav")

# 엔딩 BGM 파일명 (지침 반영)
SND_DEATHMATCH = "18. Game Over.mp3"
SND_ENDING_LV5 = "09. Ending.mp3"
SND_ENDING_LV10 = "15. Ending (Level 9, High 5).mp3"
SND_ENDING_TRUE = "16. True Ending (Level 9, High 5, 100000 Points).mp3"

# --- 음악 관련 함수 ---
def play_game_music():
    is_hidden = random.randint(1, 10) == 1
    bgm_file = HIDDEN_BGM if is_hidden else NORMAL_BGM
    try:
        pygame.mixer.music.load(os.path.join(MUSIC_DIR, bgm_file))
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)
    except:
        pass

def load_sounds():
    sounds = {}
    try:
        sounds['lvl_up'] = pygame.mixer.Sound(LEVEL_UP_SOUND_PATH)
        sounds['clear'] = pygame.mixer.Sound(LINE_CLEAR_SOUND_PATH)
        sounds['drop'] = pygame.mixer.Sound(HARD_DROP_SOUND_PATH)
        for s in sounds.values():
            s.set_volume(0.4)
    except:
        pass
    return sounds

def play_ending_music(level, score):
    pygame.mixer.music.stop()
    
    # 지침에 따른 우선순위 적용
    if score < 5000:
        file = SND_DEATHMATCH
        status = "BSOD"
    elif level >= 11:
        file = SND_ENDING_TRUE
        status = "NORMAL"
    elif level > 5: # 6~10 레벨
        file = SND_ENDING_LV10
        status = "NORMAL"
    else: # 1~5 레벨
        file = SND_ENDING_LV5
        status = "NORMAL"
    
    try:
        path = os.path.join(MUSIC_DIR, file)
        if os.path.exists(path):
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()
        else:
            print(f"Warning: File not found {file}")
    except Exception as e:
        print(f"Music Error: {e}")
        
    return status

# --- 1. 설정 및 환경 변수 ---
BLOCK_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = 10, 20
SIDEBAR_WIDTH = 200
GAME_WIDTH = BLOCK_SIZE * GRID_WIDTH
GAME_HEIGHT = BLOCK_SIZE * GRID_HEIGHT
SCREEN_WIDTH = GAME_WIDTH + SIDEBAR_WIDTH
SCREEN_HEIGHT = GAME_HEIGHT

COLOR_MAIN_BG = (30, 31, 40)
COLOR_SIDEBAR_BG = (45, 46, 60)
COLOR_GRID_LINE = (38, 39, 50)
WHITE = (245, 245, 245)

COLORS = {
    "I": (0, 200, 200), "O": (210, 210, 0), "T": (155, 40, 215), 
    "S": (0, 200, 0), "Z": (215, 0, 0), "J": (0, 85, 220), "L": (220, 130, 0)
}
TETROMINOES = {
    "I": {"shape": [[1,1,1,1]]}, 
    "O": {"shape": [[1,1],[1,1]]}, 
    "T": {"shape": [[0,1,0],[1,1,1]]},
    "S": {"shape": [[0,1,1],[1,1,0]]}, 
    "Z": {"shape": [[1,1,0],[0,1,1]]}, 
    "J": {"shape": [[1,0,0],[1,1,1]]}, 
    "L": {"shape": [[0,0,1],[1,1,1]]}
}

# --- 2. 시각 효과 및 벌칙 연출 ---
class Particle:
    def __init__(self, x, y, color, is_tetris=False):
        self.x, self.y, self.color = x, y, color
        spd = 8 if is_tetris else 4
        self.vx = random.uniform(-spd, spd)
        self.vy = random.uniform(-spd, spd)
        self.gravity, self.life, self.age = 0.25, random.randint(20, 40), 0
        self.size = random.randint(3, 6)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += self.gravity
        self.age += 1

    def draw(self, surf):
        alpha = max(0, 255 - (self.age * 255 // self.life))
        p_surf = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        p_surf.fill((*self.color, alpha))
        surf.blit(p_surf, (int(self.x), int(self.y)))

def draw_bsod(screen, score):
    info = pygame.display.Info()
    screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN)
    winsound.Beep(1000, 500)
    screen.fill((0, 0, 170))
    f_name = "malgungothic"
    f_lg = pygame.font.SysFont(f_name, 120, bold=True)
    f_md = pygame.font.SysFont(f_name, 40, bold=True)
    f_sm = pygame.font.SysFont(f_name, 25)
    
    msgs = [
        (f_lg, ":(", 0),
        (f_md, "재능 부족 에러가 발생했습니다.", 200),
        (f_sm, f"ERROR_CODE: TALENT_NOT_FOUND (Score: {score}/5000)", 300),
        (f_sm, "당신의 실력으로는 시스템을 더 이상 가동할 수 없습니다.", 350),
        (f_sm, "처음부터 다시 배우고 오세요. 게임을 강제 종료합니다.", 550)
    ]
    for f, t, y in msgs:
        screen.blit(f.render(t, True, WHITE), (info.current_w // 10, info.current_h // 5 + y))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

def draw_block(surf, x, y, color, size=BLOCK_SIZE, is_ghost=False):
    rect = (x, y, size, size)
    if is_ghost:
        pygame.draw.rect(surf, color, rect, 1)
        return
    bright = [min(c + 75, 255) for c in color]
    dark = [max(c - 75, 0) for c in color]
    bw = size // 8
    pygame.draw.rect(surf, dark, rect)
    pygame.draw.rect(surf, bright, (x, y, size-bw, size-bw))
    pygame.draw.rect(surf, color, (x+bw, y+bw, size-bw*2, size-bw*2))
    pygame.draw.rect(surf, (0,0,0), rect, 1)

# --- 3. 로직 함수 ---
def create_board():
    return [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

def get_7_bag():
    bag = list(TETROMINOES.keys())
    random.shuffle(bag)
    return [get_piece_by_name(name) for name in bag]

def get_piece_by_name(name):
    shape = TETROMINOES[name]["shape"]
    return {
        "name": name, 
        "shape": shape, 
        "color": COLORS[name], 
        "x": GRID_WIDTH // 2 - len(shape[0]) // 2, 
        "y": -len(shape)
    }

def is_valid_move(board, piece, adj_x=0, adj_y=0, new_shape=None):
    shape = new_shape if new_shape is not None else piece["shape"]
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                nx, ny = piece["x"] + x + adj_x, piece["y"] + y + adj_y
                if nx < 0 or nx >= GRID_WIDTH or ny >= GRID_HEIGHT:
                    return False
                if ny >= 0 and board[ny][nx] is not None:
                    return False
    return True

def get_ghost_y(board, piece):
    gy = piece["y"]
    while is_valid_move(board, piece, adj_y=(gy - piece["y"] + 1)):
        gy += 1
    return gy

def check_t_spin(board, piece):
    if piece["name"] != "T":
        return False
    cx, cy = piece["x"] + 1, piece["y"] + 1
    corners = [(cx-1, cy-1), (cx+1, cy-1), (cx-1, cy+1), (cx+1, cy+1)]
    count = 0
    for x, y in corners:
        if x < 0 or x >= GRID_WIDTH or y >= GRID_HEIGHT or (y >= 0 and board[y][x] is not None):
            count += 1
    return count >= 3

# --- 4. 렌더링 시스템 ---
def render_all(board, cp, n_queue, hp, score, level, combo, 
               is_game_over, is_paused, particles, flash_alpha, s_off, lv_up_timer):
    temp_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    temp_surf.fill(COLOR_SIDEBAR_BG)
    
    bg_color = (50, 20, 20) if level >= 15 else COLOR_MAIN_BG
    pygame.draw.rect(temp_surf, bg_color, (0, 0, GAME_WIDTH, SCREEN_HEIGHT))
    
    # 그리드 선
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            pygame.draw.rect(temp_surf, COLOR_GRID_LINE, 
                             (x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
    
    # 보드 블록
    for y, row in enumerate(board):
        for x, color in enumerate(row):
            if color: draw_block(temp_surf, x*BLOCK_SIZE, y*BLOCK_SIZE, color)
            
    # 현재 블록 및 고스트
    if not is_game_over:
        gy = get_ghost_y(board, cp)
        for y, row in enumerate(cp["shape"]):
            for x, cell in enumerate(row):
                if cell:
                    draw_block(temp_surf, (cp["x"]+x)*BLOCK_SIZE, 
                               (gy+y)*BLOCK_SIZE, cp["color"], is_ghost=True)
                    if cp["y"]+y >= 0:
                        draw_block(temp_surf, (cp["x"]+x)*BLOCK_SIZE, 
                                   (cp["y"]+y)*BLOCK_SIZE, cp["color"])
                                   
    # 파티클 및 플래시
    for p in particles: p.draw(temp_surf)
    if flash_alpha > 0:
        f = pygame.Surface((GAME_WIDTH, SCREEN_HEIGHT))
        f.fill((255,255,255)); f.set_alpha(flash_alpha)
        temp_surf.blit(f, (0,0))
        
    # 사이드바 UI
    sidebar_x = GAME_WIDTH + 25
    f_title = pygame.font.SysFont("arial", 16, bold=True)
    f_val = pygame.font.SysFont("consolas", 20, bold=True)
    
    # NEXT
    temp_surf.blit(f_title.render("NEXT", True, WHITE), (sidebar_x, 20))
    for i in range(3):
        p_next = n_queue[i]
        box_y = 45 + (i * 75)
        pygame.draw.rect(temp_surf, (35, 36, 45), (sidebar_x, box_y, 150, 65))
        s, c, ps = p_next["shape"], p_next["color"], 20
        bx = sidebar_x + (150 - len(s[0])*ps) // 2
        by = box_y + (65 - len(s)*ps) // 2
        for sy, srow in enumerate(s):
            for sx, scell in enumerate(srow):
                if scell: draw_block(temp_surf, bx+sx*ps, by+sy*ps, c, size=ps)
                
    # HOLD
    temp_surf.blit(f_title.render("HOLD", True, WHITE), (sidebar_x, 285))
    pygame.draw.rect(temp_surf, (35, 36, 45), (sidebar_x, 310, 150, 80))
    if hp:
        s, c, ps = TETROMINOES[hp]["shape"], COLORS[hp], 20
        bx = sidebar_x + (150 - len(s[0])*ps) // 2
        by = 310 + (80 - len(s)*ps) // 2
        for sy, srow in enumerate(s):
            for sx, scell in enumerate(srow):
                if scell: draw_block(temp_surf, bx+sx*ps, by+sy*ps, c, size=ps)
                
    # Stats
    sy = 410
    stats = [("SCORE", score, (0,255,180)), ("LEVEL", level, (255,200,0)), ("COMBO", combo, (255,100,100))]
    for l, v, col in stats:
        temp_surf.blit(f_title.render(l, True, WHITE), (sidebar_x, sy))
        temp_surf.blit(f_val.render(str(v), True, col), (sidebar_x, sy+22))
        sy += 65
        
    if is_paused or is_game_over:
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0,0,0,180))
        temp_surf.blit(overlay, (0,0))
        txt = "PAUSED" if is_paused else "GAME OVER"
        surf = pygame.font.SysFont("arial", 45, bold=True).render(txt, True, WHITE)
        temp_surf.blit(surf, (SCREEN_WIDTH//2 - surf.get_width()//2, SCREEN_HEIGHT//2 - 30))
        
    return temp_surf

# --- 5. 메인 루프 ---
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris: 7-Bag Edition")
    clock = pygame.time.Clock()
    play_game_music()
    sfx = load_sounds()

    def reset(): 
        q = get_7_bag() + get_7_bag()
        return (create_board(), q.pop(0), q, None, True, 0, 1, 0, 0, 
                False, [], 0, 0, 0, 0, 0, False, False)

    (board, cp, n_queue, hp, can_hold, score, level, total_l, combo, 
     is_game_over, particles, flash_alpha, drop_time, lock_timer, 
     shake_intensity, lv_up_timer, is_paused, last_was_rotate) = reset()
    
    key_time = {"left": 0, "right": 0, "down": 0}

    while True:
        dt = clock.tick(60)
        if not is_paused:
            flash_alpha = max(0, flash_alpha-8)
            shake_intensity = max(0, shake_intensity-1)
            lv_up_timer = max(0, lv_up_timer-1)
            particles = [p for p in particles if p.age < p.life]
            for p in particles: p.update()

        if not is_game_over and not is_paused:
            fall_speed = max(70, 800 - (level - 1) * 52) 
            if is_valid_move(board, cp, adj_y=1):
                drop_time += dt; lock_timer = 0
                if drop_time > fall_speed:
                    cp["y"] += 1; drop_time = 0; last_was_rotate = False
            else:
                lock_timer += dt
                if lock_timer > max(150, 500 - (level-1)*25):
                    is_ts = last_was_rotate and check_t_spin(board, cp)
                    temp_b = [r[:] for r in board]
                    for y, row in enumerate(cp["shape"]):
                        for x, cell in enumerate(row):
                            if cell and cp["y"]+y >= 0:
                                temp_b[cp["y"]+y][cp["x"]+x] = cp["color"]
                    
                    full_l = [i for i, r in enumerate(temp_b) if None not in r]
                    num_l = len(full_l)
                    
                    if num_l > 0 or is_ts:
                        if is_ts:
                            ts_bonus = {0: 400, 1: 800, 2: 1200, 3: 1600}.get(num_l, 400)
                            score += ts_bonus * level
                            shake_intensity, flash_alpha = 10, 150
                        if num_l > 0:
                            if sfx.get('clear'): sfx['clear'].play()
                            score += ({1:100, 2:300, 3:500, 4:800}[num_l] * level) + (combo * 50)
                            combo += 1; total_l += num_l
                            board = [[None]*GRID_WIDTH for _ in range(num_l)] + \
                                    [r for i, r in enumerate(temp_b) if i not in full_l]
                            if (total_l // 15) + 1 > level:
                                level += 1; lv_up_timer = 90
                                if sfx.get('lvl_up'): sfx['lvl_up'].play()
                        else: combo = 0; board = temp_b
                    else: combo = 0; board = temp_b

                    # 종료 조건 및 블록 교체
                    if any(cell and cp["y"]+y < 0 for y, row in enumerate(cp["shape"]) 
                           for x, cell in enumerate(row)) or not is_valid_move(board, n_queue[0], adj_y=1):
                        is_game_over = True
                        if play_ending_music(level, score) == "BSOD": draw_bsod(screen, score)
                    
                    cp = n_queue.pop(0)
                    if len(n_queue) <= 7: n_queue.extend(get_7_bag())
                    can_hold, lock_timer, last_was_rotate = True, 0, False

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: is_paused = not is_paused
                if not is_game_over and not is_paused:
                    if event.key in [pygame.K_LSHIFT, pygame.K_c] and can_hold:
                        old = cp["name"]
                        cp = n_queue.pop(0) if hp is None else get_piece_by_name(hp)
                        if len(n_queue) <= 7: n_queue.extend(get_7_bag())
                        hp, can_hold, last_was_rotate = old, False, False
                    if event.key == pygame.K_UP:
                        rot = [list(r) for r in zip(*cp["shape"][::-1])]
                        for off in [0, -1, 1, -2, 2]:
                            if is_valid_move(board, cp, adj_x=off, new_shape=rot):
                                cp["x"] += off; cp["shape"] = rot; last_was_rotate = True; break
                    if event.key == pygame.K_SPACE:
                        cp["y"] = get_ghost_y(board, cp); lock_timer, shake_intensity = 600, 8
                        if sfx.get('drop'): sfx['drop'].play()
                if is_game_over and event.key == pygame.K_r:
                    (board, cp, n_queue, hp, can_hold, score, level, total_l, combo, 
                     is_game_over, particles, flash_alpha, drop_time, lock_timer, 
                     shake_intensity, lv_up_timer, is_paused, last_was_rotate) = reset()
                    play_game_music()

        if not is_game_over and not is_paused:
            keys = pygame.key.get_pressed()
            move_map = [("left", -1, 0, pygame.K_LEFT), ("right", 1, 0, pygame.K_RIGHT), 
                        ("down", 0, 1, pygame.K_DOWN)]
            for kn, ax, ay, kp in move_map:
                if keys[kp]:
                    if key_time[kn] == 0 or (key_time[kn] > 150 and (key_time[kn]-150) % 40 < dt):
                        if is_valid_move(board, cp, ax, ay):
                            cp["x"] += ax; cp["y"] += ay; last_was_rotate = False
                    key_time[kn] += dt
                else: key_time[kn] = 0

        s_off = (random.randint(-shake_intensity, shake_intensity), 
                 random.randint(-shake_intensity, shake_intensity)) if shake_intensity > 0 else (0,0)
        
        final_render = render_all(board, cp, n_queue, hp, score, level, combo, 
                                  is_game_over, is_paused, particles, flash_alpha, 
                                  s_off, lv_up_timer)
        screen.blit(final_render, s_off)
        pygame.display.flip()

if __name__ == "__main__":
    main()