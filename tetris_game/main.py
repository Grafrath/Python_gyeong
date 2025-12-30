import pygame
import random
import asyncio  # 웹(Pygbag) 실행을 위한 필수 라이브러리

# 기존 모듈 임포트 (경로 설정은 constants.py를 따름)
from constants import *
from utils import Particle, TextManager
from logic import *

# --- 음악 및 연출 함수 (웹 호환성 최적화) ---
def play_game_music():
    """웹 브라우저 보안 정책으로 인해 사용자 클릭/키 입력 후에 호출되어야 함"""
    bgm_file = HIDDEN_BGM if random.randint(1, 10) == 1 else NORMAL_BGM
    try:
        # constants.py에서 정의한 MUSIC_DIR와 bgm_file 사용
        path = f"{MUSIC_DIR}/{bgm_file}"
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)
    except Exception as e:
        print(f"Music load error: {e}")

def load_sounds():
    """효과음 로드 (파일이 없을 경우 대비 예외 처리)"""
    sounds = {}
    try:
        sounds['lvl_up'] = pygame.mixer.Sound(LEVEL_UP_SOUND_PATH)
        sounds['clear'] = pygame.mixer.Sound(LINE_CLEAR_SOUND_PATH)
        sounds['drop'] = pygame.mixer.Sound(HARD_DROP_SOUND_PATH)
        for s in sounds.values():
            s.set_volume(0.4)
    except Exception as e:
        print(f"Sound load error: {e}")
    return sounds

def play_ending_music(level, score):
    """게임 종료 시 상황에 맞는 음악 재생"""
    pygame.mixer.music.stop()
    if score < 5000: file, status = SND_DEATHMATCH, "BSOD"
    elif level >= 11: file, status = SND_ENDING_TRUE, "NORMAL"
    elif level > 5: file, status = SND_ENDING_LV10, "NORMAL"
    else: file, status = SND_ENDING_LV5, "NORMAL"
    try:
        path = f"{MUSIC_DIR}/{file}"
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
    except: pass
    return status

def draw_block(surf, x, y, color, size=BLOCK_SIZE, is_ghost=False):
    """블록 그리기 (그림자 및 테두리 효과)"""
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

async def draw_bsod(screen, score, tm):
    """블루스크린 연출 (한글 깨짐 및 잘림 방지를 위해 영문/중앙정렬 적용)"""
    screen.fill((0, 0, 170))
    
    msgs = [
        (tm.fonts["bsod_lg"], ":(", 60),
        (tm.fonts["bsod_md"], "TALENT_NOT_FOUND_ERROR.", 180),
        (tm.fonts["bsod_sm"], f"ERROR_CODE: TALENT_NOT_FOUND (Score: {score}/5000)", 260),
        (tm.fonts["bsod_sm"], "Your skills are no longer enough", 320),
        (tm.fonts["bsod_sm"], "to keep the system running.", 350),
        (tm.fonts["bsod_sm"], "PLEASE REBOOT YOUR SKILL.", 450),
        (tm.fonts["bsod_sm"], "Press any key to exit.", 480)
    ]
    
    for font, text, y_pos in msgs:
        rendered_text = font.render(text, True, (255, 255, 255))
        text_x = (SCREEN_WIDTH - rendered_text.get_width()) // 2
        screen.blit(rendered_text, (text_x, y_pos))
    
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type in [pygame.KEYDOWN, pygame.QUIT]:
                waiting = False
        await asyncio.sleep(0)

def render_all(board, cp, n_queue, hp, score, level, combo, is_game_over, is_paused, flash_alpha, tm, particles):
    """전체 게임 화면 렌더링"""
    temp_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    temp_surf.fill(COLOR_SIDEBAR_BG)
    bg_color = (50, 20, 20) if level >= 15 else COLOR_MAIN_BG
    pygame.draw.rect(temp_surf, bg_color, (0, 0, GAME_WIDTH, SCREEN_HEIGHT))
    
    # 그리드 그리기
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            pygame.draw.rect(temp_surf, COLOR_GRID_LINE, (x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
    
    # 쌓인 블록
    for y, row in enumerate(board):
        for x, col in enumerate(row):
            if col: draw_block(temp_surf, x*BLOCK_SIZE, y*BLOCK_SIZE, col)
            
    # 현재 블록 및 고스트
    if not is_game_over:
        gy = get_ghost_y(board, cp)
        for y, row in enumerate(cp["shape"]):
            for x, cell in enumerate(row):
                if cell:
                    draw_block(temp_surf, (cp["x"]+x)*BLOCK_SIZE, (gy+y)*BLOCK_SIZE, cp["color"], is_ghost=True)
                    if cp["y"]+y >= 0:
                        draw_block(temp_surf, (cp["x"]+x)*BLOCK_SIZE, (cp["y"]+y)*BLOCK_SIZE, cp["color"])
    
    for p in particles: p.draw(temp_surf)
    
    # 라인 클리어 효과
    if flash_alpha > 0:
        f = pygame.Surface((GAME_WIDTH, SCREEN_HEIGHT))
        f.fill((255,255,255))
        f.set_alpha(flash_alpha)
        temp_surf.blit(f, (0,0))
        
    # 사이드바 (Next, Hold, Score 등)
    sidebar_x = GAME_WIDTH + 25
    temp_surf.blit(tm.static_labels["NEXT"], (sidebar_x, 20))
    for i in range(3):
        p_next = n_queue[i]
        box_y = 45 + (i * 75)
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
        temp_surf.blit(tm.get_val_surf(val, col), (sidebar_x, sy+22))
        sy += 65
        
    # 일시정지 및 게임오버 오버레이
    if is_paused or is_game_over:
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0,0,0,180))
        temp_surf.blit(overlay, (0,0))
        
        if is_paused:
            msg_list = ["PAUSED"]
        else:
            msg_list = ["GAME OVER", "Press 'R' to Restart"]
        
        for i, text in enumerate(msg_list):
            surf = tm.static_labels.get(text, tm.fonts["bsod_sm"].render(text, True, (255,255,255)))
            text_x = SCREEN_WIDTH // 2 - surf.get_width() // 2
            text_y = SCREEN_HEIGHT // 2 - 50 + (i * 70) # 줄간격 70으로 조정
            temp_surf.blit(surf, (text_x, text_y))
            
    return temp_surf

# --- 메인 루프 (asyncio 적용) ---
async def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris: Web Edition")
    clock = pygame.time.Clock()
    tm = TextManager()
    sfx = load_sounds()
    
    music_started = False # 음악 재생 여부 체크

    def reset():
        q = get_7_bag() + get_7_bag()
        return (create_board(), q.pop(0), q, None, True, 0, 1, 0, 0, False, 0, 0, 0, 0, False, False, [])

    (board, cp, n_queue, hp, can_hold, score, level, total_l, combo, is_game_over, flash_alpha, drop_time, lock_timer, shake_intensity, is_paused, last_was_rotate, particles) = reset()
    key_time = {"left": 0, "right": 0, "down": 0}

    while True:
        dt = clock.tick(60)
        
        if not is_paused:
            flash_alpha = max(0, flash_alpha-8)
            shake_intensity = max(0, shake_intensity-1)
            particles = [p for p in particles if p.age < p.life]
            for p in particles: p.update()

        # 하강 로직
        if not is_game_over and not is_paused:
            fall_speed = max(70, 800 - (level - 1) * 52)
            if is_valid_move(board, cp, adj_y=1):
                drop_time += dt
                lock_timer = 0
                if drop_time > fall_speed:
                    cp["y"] += 1
                    drop_time = 0
                    last_was_rotate = False
            else:
                lock_timer += dt
                if lock_timer > max(150, 500 - (level-1)*25):
                    # 블록 고정 및 라인 체크
                    is_ts = last_was_rotate and check_t_spin(board, cp)
                    for y, row in enumerate(cp["shape"]):
                        for x, cell in enumerate(row):
                            if cell and cp["y"]+y >= 0:
                                board[cp["y"]+y][cp["x"]+x] = cp["color"]
                    
                    full_l = [i for i, r in enumerate(board) if None not in r]
                    if full_l or is_ts:
                        if is_ts:
                            score += {0:400, 1:800, 2:1200, 3:1600}.get(len(full_l), 400) * level
                            shake_intensity, flash_alpha = 15, 200
                        if full_l:
                            if sfx.get('clear'): sfx['clear'].play()
                            score += ({1:100, 2:300, 3:500, 4:800}[len(full_l)] * level) + (combo * 50)
                            combo += 1
                            total_l += len(full_l)
                            board = [[None]*GRID_WIDTH for _ in range(len(full_l))] + [r for i, r in enumerate(board) if i not in full_l]
                            if (total_l // 15) + 1 > level:
                                level += 1
                                if sfx.get('lvl_up'): sfx['lvl_up'].play()
                        else: combo = 0
                    else: combo = 0
                    
                    if any(cell and cp["y"]+y < 0 for y, row in enumerate(cp["shape"]) for x, cell in enumerate(row)):
                        is_game_over = True
                        if play_ending_music(level, score) == "BSOD":
                            await draw_bsod(screen, score, tm)
                    
                    cp = n_queue.pop(0)
                    if len(n_queue) <= 7: n_queue.extend(get_7_bag())
                    can_hold, lock_timer, last_was_rotate = True, 0, False

        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            # 브라우저 보안 정책 대응: 첫 입력 시 음악 재생
            if not music_started and event.type in [pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN]:
                play_game_music()
                music_started = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: 
                    is_paused = not is_paused
                
                if not is_game_over and not is_paused:
                    if event.key in [pygame.K_LSHIFT, pygame.K_c] and can_hold:
                        old = cp["name"]
                        cp = n_queue.pop(0) if hp is None else get_piece_by_name(hp)
                        hp, can_hold, last_was_rotate = old, False, False
                    if event.key == pygame.K_UP:
                        rot = [list(r) for r in zip(*cp["shape"][::-1])]
                        for ox, oy in [(0,0), (-1,0), (1,0), (0,-1), (-1,-1), (1,-1)]:
                            if is_valid_move(board, cp, ox, oy, rot):
                                cp["x"] += ox; cp["y"] += oy; cp["shape"] = rot; last_was_rotate = True; break
                    if event.key == pygame.K_SPACE:
                        cp["y"] = get_ghost_y(board, cp)
                        lock_timer, shake_intensity = 600, 10
                        if sfx.get('drop'): sfx['drop'].play()
                
                if is_game_over and event.key == pygame.K_r:
                    (board, cp, n_queue, hp, can_hold, score, level, total_l, combo, is_game_over, flash_alpha, drop_time, lock_timer, shake_intensity, is_paused, last_was_rotate, particles) = reset()
                    play_game_music()

        # 연속 키 입력 처리 (DAS)
        if not is_game_over and not is_paused:
            keys = pygame.key.get_pressed()
            for kn, ax, ay, kp in [("left", -1, 0, pygame.K_LEFT), ("right", 1, 0, pygame.K_RIGHT), ("down", 0, 1, pygame.K_DOWN)]:
                if keys[kp]:
                    if key_time[kn] == 0 or (key_time[kn] > 150 and (key_time[kn]-150) % 40 < dt):
                        if is_valid_move(board, cp, ax, ay): cp["x"] += ax; cp["y"] += ay; last_was_rotate = False
                    key_time[kn] += dt
                else: key_time[kn] = 0

        # 화면 출력
        s_off = (random.randint(-shake_intensity, shake_intensity), random.randint(-shake_intensity, shake_intensity)) if shake_intensity > 0 else (0,0)
        final_render = render_all(board, cp, n_queue, hp, score, level, combo, is_game_over, is_paused, flash_alpha, tm, particles)
        screen.fill((0, 0, 0))
        screen.blit(final_render, s_off)
        pygame.display.flip()

        # 브라우저에 제어권 양보 (필수)
        await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())