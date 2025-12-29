# Pygame 초기화, 이벤트 루프, 렌더링 (실행 파일)

import pygame
import random
import os
import sys
import winsound
from constants import *
from utils import Particle, TextManager
from logic import *

# --- 음악 및 연출 함수 ---
def play_game_music():
    bgm_file = HIDDEN_BGM if random.randint(1, 10) == 1 else NORMAL_BGM
    try:
        pygame.mixer.music.load(os.path.join(MUSIC_DIR, bgm_file))
        pygame.mixer.music.set_volume(0.4); pygame.mixer.music.play(-1)
    except: pass

def load_sounds():
    sounds = {}
    try:
        sounds['lvl_up'] = pygame.mixer.Sound(LEVEL_UP_SOUND_PATH)
        sounds['clear'] = pygame.mixer.Sound(LINE_CLEAR_SOUND_PATH)
        sounds['drop'] = pygame.mixer.Sound(HARD_DROP_SOUND_PATH)
        for s in sounds.values(): s.set_volume(0.4)
    except: pass
    return sounds

def play_ending_music(level, score):
    pygame.mixer.music.stop()
    if score < 5000: file, status = SND_DEATHMATCH, "BSOD"
    elif level >= 11: file, status = SND_ENDING_TRUE, "NORMAL"
    elif level > 5: file, status = SND_ENDING_LV10, "NORMAL"
    else: file, status = SND_ENDING_LV5, "NORMAL"
    try:
        path = os.path.join(MUSIC_DIR, file)
        if os.path.exists(path):
            pygame.mixer.music.load(path); pygame.mixer.music.play()
    except: pass
    return status

def draw_block(surf, x, y, color, size=BLOCK_SIZE, is_ghost=False):
    rect = (x, y, size, size)
    if is_ghost:
        pygame.draw.rect(surf, color, rect, 1); return
    bright = [min(c + 75, 255) for c in color]
    dark = [max(c - 75, 0) for c in color]
    bw = size // 8
    pygame.draw.rect(surf, dark, rect)
    pygame.draw.rect(surf, bright, (x, y, size-bw, size-bw))
    pygame.draw.rect(surf, color, (x+bw, y+bw, size-bw*2, size-bw*2))
    pygame.draw.rect(surf, (0,0,0), rect, 1)

def draw_bsod(screen, score, tm):
    info = pygame.display.Info()
    screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.FULLSCREEN)
    winsound.Beep(1000, 500); screen.fill((0, 0, 170))
    msgs = [
        (tm.fonts["bsod_lg"], ":(", 0),
        (tm.fonts["bsod_md"], "재능 부족 에러가 발생했습니다.", 200),
        (tm.fonts["bsod_sm"], f"ERROR_CODE: TALENT_NOT_FOUND (Score: {score}/5000)", 300),
        (tm.fonts["bsod_sm"], "당신의 실력으로는 시스템을 더 이상 가동할 수 없습니다.", 350),
        (tm.fonts["bsod_sm"], "처음부터 다시 배우고 오세요. 아무 키나 누르면 종료합니다.", 550)
    ]
    for f, t, y in msgs: screen.blit(f.render(t, True, WHITE), (info.current_w // 10, info.current_h // 5 + y))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type in [pygame.KEYDOWN, pygame.QUIT]: waiting = False
    pygame.quit(); sys.exit()

# --- 렌더링 ---
def render_all(board, cp, n_queue, hp, score, level, combo, is_game_over, is_paused, flash_alpha, tm, particles):
    temp_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    temp_surf.fill(COLOR_SIDEBAR_BG)
    bg_color = (50, 20, 20) if level >= 15 else COLOR_MAIN_BG
    pygame.draw.rect(temp_surf, bg_color, (0, 0, GAME_WIDTH, SCREEN_HEIGHT))
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            pygame.draw.rect(temp_surf, COLOR_GRID_LINE, (x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
    for y, row in enumerate(board):
        for x, col in enumerate(row):
            if col: draw_block(temp_surf, x*BLOCK_SIZE, y*BLOCK_SIZE, col)
    if not is_game_over:
        gy = get_ghost_y(board, cp)
        for y, row in enumerate(cp["shape"]):
            for x, cell in enumerate(row):
                if cell:
                    draw_block(temp_surf, (cp["x"]+x)*BLOCK_SIZE, (gy+y)*BLOCK_SIZE, cp["color"], is_ghost=True)
                    if cp["y"]+y >= 0: draw_block(temp_surf, (cp["x"]+x)*BLOCK_SIZE, (cp["y"]+y)*BLOCK_SIZE, cp["color"])
    for p in particles: p.draw(temp_surf)
    if flash_alpha > 0:
        f = pygame.Surface((GAME_WIDTH, SCREEN_HEIGHT)); f.fill((255,255,255)); f.set_alpha(flash_alpha); temp_surf.blit(f, (0,0))
    sidebar_x = GAME_WIDTH + 25
    temp_surf.blit(tm.static_labels["NEXT"], (sidebar_x, 20))
    for i in range(3):
        p_next = n_queue[i]; box_y = 45 + (i * 75)
        pygame.draw.rect(temp_surf, (35, 36, 45), (sidebar_x, box_y, 150, 65))
        s, c = p_next["shape"], p_next["color"]
        bx, by = sidebar_x + (150 - len(s[0])*20)//2, box_y + (65 - len(s)*20)//2
        for sy, srow in enumerate(s):
            for sx, scell in enumerate(srow):
                if scell: draw_block(temp_surf, bx+sx*20, by+sy*20, c, size=20)
    temp_surf.blit(tm.static_labels["HOLD"], (sidebar_x, 285))
    pygame.draw.rect(temp_surf, (35, 36, 45), (sidebar_x, 310, 150, 80))
    if hp:
        s, c = TETROMINOES[hp]["shape"], COLORS[hp]
        bx, by = sidebar_x + (150 - len(s[0])*20)//2, 310 + (80 - len(s)*20)//2
        for sy, srow in enumerate(s):
            for sx, scell in enumerate(srow):
                if scell: draw_block(temp_surf, bx+sx*20, by+sy*20, c, size=20)
    sy = 410
    for label, val, col in [("SCORE", score, (0,255,180)), ("LEVEL", level, (255,200,0)), ("COMBO", combo, (255,100,100))]:
        temp_surf.blit(tm.static_labels[label], (sidebar_x, sy))
        temp_surf.blit(tm.get_val_surf(val, col), (sidebar_x, sy+22)); sy += 65
    if is_paused or is_game_over:
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA); overlay.fill((0,0,0,180))
        temp_surf.blit(overlay, (0,0)); txt = "PAUSED" if is_paused else "GAME OVER"
        surf = tm.static_labels[txt]; temp_surf.blit(surf, (SCREEN_WIDTH//2-surf.get_width()//2, SCREEN_HEIGHT//2-30))
    return temp_surf

# --- 메인 루프 ---
def main():
    pygame.init(); screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris: Modular Edition"); clock = pygame.time.Clock()
    tm = TextManager(); sfx = load_sounds(); play_game_music()

    def reset():
        q = get_7_bag() + get_7_bag()
        return (create_board(), q.pop(0), q, None, True, 0, 1, 0, 0, False, 0, 0, 0, 0, False, False, [])

    (board, cp, n_queue, hp, can_hold, score, level, total_l, combo, is_game_over, flash_alpha, drop_time, lock_timer, shake_intensity, is_paused, last_was_rotate, particles) = reset()
    key_time = {"left": 0, "right": 0, "down": 0}

    while True:
        dt = clock.tick(60)
        if not is_paused:
            flash_alpha = max(0, flash_alpha-8); shake_intensity = max(0, shake_intensity-1)
            particles = [p for p in particles if p.age < p.life]
            for p in particles: p.update()

        if not is_game_over and not is_paused:
            fall_speed = max(70, 800 - (level - 1) * 52)
            if is_valid_move(board, cp, adj_y=1):
                drop_time += dt; lock_timer = 0
                if drop_time > fall_speed: cp["y"] += 1; drop_time = 0; last_was_rotate = False
            else:
                lock_timer += dt
                if lock_timer > max(150, 500 - (level-1)*25):
                    is_ts = last_was_rotate and check_t_spin(board, cp)
                    for y, row in enumerate(cp["shape"]):
                        for x, cell in enumerate(row):
                            if cell and cp["y"]+y >= 0: board[cp["y"]+y][cp["x"]+x] = cp["color"]
                    full_l = [i for i, r in enumerate(board) if None not in r]
                    if full_l or is_ts:
                        if is_ts: score += {0:400, 1:800, 2:1200, 3:1600}.get(len(full_l), 400) * level; shake_intensity, flash_alpha = 15, 200
                        if full_l:
                            if sfx.get('clear'): sfx['clear'].play()
                            for ly in full_l:
                                for lx in range(GRID_WIDTH):
                                    for _ in range(2): particles.append(Particle(lx*BLOCK_SIZE+15, ly*BLOCK_SIZE+15, (255,255,255)))
                            score += ({1:100, 2:300, 3:500, 4:800}[len(full_l)] * level) + (combo * 50)
                            combo += 1; total_l += len(full_l)
                            board = [[None]*GRID_WIDTH for _ in range(len(full_l))] + [r for i, r in enumerate(board) if i not in full_l]
                            if (total_l // 15) + 1 > level:
                                level += 1; 
                                if sfx.get('lvl_up'): sfx['lvl_up'].play()
                        else: combo = 0
                    else: combo = 0
                    if any(cell and cp["y"]+y < 0 for y, row in enumerate(cp["shape"]) for x, cell in enumerate(row)):
                        is_game_over = True
                        if play_ending_music(level, score) == "BSOD": draw_bsod(screen, score, tm)
                    cp = n_queue.pop(0)
                    if len(n_queue) <= 7: n_queue.extend(get_7_bag())
                    can_hold, lock_timer, last_was_rotate = True, 0, False

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: is_paused = not is_paused
                if not is_game_over and not is_paused:
                    if event.key in [pygame.K_LSHIFT, pygame.K_c] and can_hold:
                        old = cp["name"]; cp = n_queue.pop(0) if hp is None else get_piece_by_name(hp)
                        hp, can_hold, last_was_rotate = old, False, False
                    if event.key == pygame.K_UP:
                        rot = [list(r) for r in zip(*cp["shape"][::-1])]
                        for ox, oy in [(0,0), (-1,0), (1,0), (0,-1), (-1,-1), (1,-1)]:
                            if is_valid_move(board, cp, ox, oy, rot):
                                cp["x"] += ox; cp["y"] += oy; cp["shape"] = rot; last_was_rotate = True; break
                    if event.key == pygame.K_SPACE:
                        cp["y"] = get_ghost_y(board, cp); lock_timer, shake_intensity = 600, 10
                        if sfx.get('drop'): sfx['drop'].play()
                if is_game_over and event.key == pygame.K_r:
                    (board, cp, n_queue, hp, can_hold, score, level, total_l, combo, is_game_over, flash_alpha, drop_time, lock_timer, shake_intensity, is_paused, last_was_rotate, particles) = reset()
                    play_game_music()

        if not is_game_over and not is_paused:
            keys = pygame.key.get_pressed()
            for kn, ax, ay, kp in [("left", -1, 0, pygame.K_LEFT), ("right", 1, 0, pygame.K_RIGHT), ("down", 0, 1, pygame.K_DOWN)]:
                if keys[kp]:
                    if key_time[kn] == 0 or (key_time[kn] > 150 and (key_time[kn]-150) % 40 < dt):
                        if is_valid_move(board, cp, ax, ay): cp["x"] += ax; cp["y"] += ay; last_was_rotate = False
                    key_time[kn] += dt
                else: key_time[kn] = 0

        s_off = (random.randint(-shake_intensity, shake_intensity), random.randint(-shake_intensity, shake_intensity)) if shake_intensity > 0 else (0,0)
        final_render = render_all(board, cp, n_queue, hp, score, level, combo, is_game_over, is_paused, flash_alpha, tm, particles)
        screen.fill((0, 0, 0)); screen.blit(final_render, s_off); pygame.display.flip()

if __name__ == "__main__":
    main()