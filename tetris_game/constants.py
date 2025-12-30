# --- 경로 및 파일명 설정 (웹 최적화) ---
# 웹 환경에서는 상대 경로를 직접 사용하는 것이 가장 안전합니다.
MUSIC_DIR = "music"

# [중요] 실제 폴더 안의 파일명을 아래와 같이 공백 없이 영어로 바꾸는 것을 강력 권장합니다.
# 파일명을 바꾸셨다면 아래 변수값도 똑같이 맞춰주세요.
NORMAL_BGM = "bgm_type_a.mp3"              # 03. A-Type... 수정본
HIDDEN_BGM = "suisei_tetris.mp3"            # Suisei's... 수정본
LEVEL_UP_SOUND_PATH = "music/lvl_up.wav"
LINE_CLEAR_SOUND_PATH = "music/clear.mp3"
HARD_DROP_SOUND_PATH = "music/drop.wav"

# 엔딩 BGM 파일명 (공백 제거 추천)
SND_DEATHMATCH = "gameover.mp3"
SND_ENDING_LV5 = "ending_lv5.mp3"
SND_ENDING_LV10 = "ending_lv10.mp3"
SND_ENDING_TRUE = "ending_true.mp3"

# --- 환경 변수 ---
BLOCK_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = 10, 20
SIDEBAR_WIDTH = 200
GAME_WIDTH, GAME_HEIGHT = BLOCK_SIZE * GRID_WIDTH, BLOCK_SIZE * GRID_HEIGHT
SCREEN_WIDTH, SCREEN_HEIGHT = GAME_WIDTH + SIDEBAR_WIDTH, GAME_HEIGHT

COLOR_MAIN_BG, COLOR_SIDEBAR_BG = (30, 31, 40), (45, 46, 60)
COLOR_GRID_LINE, WHITE = (38, 39, 50), (245, 245, 245)

COLORS = {
    "I": (0, 200, 200), "O": (210, 210, 0), "T": (155, 40, 215), 
    "S": (0, 200, 0), "Z": (215, 0, 0), "J": (0, 85, 220), "L": (220, 130, 0)
}
TETROMINOES = {
    "I": {"shape": [[1,1,1,1]]}, "O": {"shape": [[1,1],[1,1]]}, 
    "T": {"shape": [[0,1,0],[1,1,1]]}, "S": {"shape": [[0,1,1],[1,1,0]]}, 
    "Z": {"shape": [[1,1,0],[0,1,1]]}, "J": {"shape": [[1,0,0],[1,1,1]]}, 
    "L": {"shape": [[0,0,1],[1,1,1]]}
}