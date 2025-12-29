# 테트리스 블록 생성, 충돌 체크 등 핵심 물리 로직

import random
from constants import GRID_WIDTH, GRID_HEIGHT, TETROMINOES, COLORS

def create_board(): 
    return [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

def get_piece_by_name(name):
    shape = TETROMINOES[name]["shape"]
    return {
        "name": name, "shape": shape, "color": COLORS[name], 
        "x": GRID_WIDTH // 2 - len(shape[0]) // 2, "y": -len(shape)
    }

def get_7_bag():
    bag = list(TETROMINOES.keys())
    random.shuffle(bag)
    return [get_piece_by_name(n) for n in bag]

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

def check_t_spin(board, piece):
    if piece["name"] != "T": return False
    cx, cy = piece["x"] + 1, piece["y"] + 1
    count = 0
    for x, y in [(cx-1, cy-1), (cx+1, cy-1), (cx-1, cy+1), (cx+1, cy+1)]:
        if x < 0 or x >= GRID_WIDTH or y >= GRID_HEIGHT or (y >= 0 and board[y][x] is not None): count += 1
    return count >= 3