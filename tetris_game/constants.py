# 게임 설정, 색상, 경로 등 변하지 않는 값들

import os
import sys

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
LINE_CLEAR_SOUND_PATH = os.path.join(MUSIC_DIR, "A quick, ascending chime for a single line clear in Tetris.-edited-2025-12-26T15-09-09.mp3")
HARD_DROP_SOUND_PATH = os.path.join(MUSIC_DIR, "A subtle, percussive thud for a Tetris block landing.-edited-2025-12-26T15-08-00.wav")

# 엔딩 BGM 파일명
SND_DEATHMATCH = "18. Game Over.mp3"
SND_ENDING_LV5 = "09. Ending.mp3"
SND_ENDING_LV10 = "15. Ending (Level 9, High 5).mp3"
SND_ENDING_TRUE = "16. True Ending (Level 9, High 5, 100000 Points).mp3"

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