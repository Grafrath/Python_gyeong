import pygame
import random
import os

# --- 설정 및 자산 로드 ---
pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Blackjack HD - Diagonal Layout")

# 폰트 설정
font = pygame.font.SysFont("malgungothic", 35)
msg_font = pygame.font.SysFont("malgungothic", 60, bold=True)

card_images = {}

def load_assets():
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    for suit in suits:
        for rank in ranks:
            file_name = f"card{suit}{rank}.png"
            full_path = os.path.join(base_path, "PNG", "Cards", file_name)
            if os.path.exists(full_path):
                img = pygame.image.load(full_path).convert_alpha()
                card_images[(suit, rank)] = pygame.transform.scale(img, (130, 182)) # 카드 크기 살짝 키움
    
    back_path = os.path.join(base_path, "PNG", "Cards", "cardBack_red2.png")
    if os.path.exists(back_path):
        back_img = pygame.image.load(back_path).convert_alpha()
        card_images['back'] = pygame.transform.scale(back_img, (130, 182))

def calculate_score(hand):
    score = 0
    ace_count = 0
    values = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
    for _, rank in hand:
        score += values[rank]
        if rank == 'A': ace_count += 1
    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1
    return score

def reset_game():
    new_deck = [(s, r) for s in ['Clubs', 'Diamonds', 'Hearts', 'Spades'] for r in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']]
    random.shuffle(new_deck)
    return new_deck, [new_deck.pop(), new_deck.pop()], [new_deck.pop(), new_deck.pop()], "PLAYER_TURN", ""

load_assets()
deck, player_hand, dealer_hand, game_state, result_text = reset_game()

# --- 버튼 위치 재설정 (화면 하단 중앙부) ---
# 버튼을 찾기 쉽게 화면 아래쪽 중앙에 큼직하게 배치했습니다.
hit_button = pygame.Rect(SCREEN_WIDTH//2 - 160, 600, 150, 70)
stand_button = pygame.Rect(SCREEN_WIDTH//2 + 10, 600, 150, 70)

running = True
while running:
    screen.fill((20, 80, 20)) # 진한 카지노 초록색
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if game_state == "PLAYER_TURN":
                if hit_button.collidepoint(event.pos):
                    player_hand.append(deck.pop())
                    if calculate_score(player_hand) > 21:
                        game_state = "GAME_OVER"
                        result_text = "PLAYER BUST!"
                elif stand_button.collidepoint(event.pos):
                    game_state = "DEALER_TURN"
            elif game_state == "GAME_OVER":
                deck, player_hand, dealer_hand, game_state, result_text = reset_game()

    # --- 딜러 AI ---
    if game_state == "DEALER_TURN":
        if calculate_score(dealer_hand) < 17:
            pygame.time.delay(700)
            dealer_hand.append(deck.pop())
        else:
            p_score = calculate_score(player_hand)
            d_score = calculate_score(dealer_hand)
            if d_score > 21: result_text = "DEALER BUST! WIN!"
            elif p_score > d_score: result_text = "YOU WIN!"
            elif p_score < d_score: result_text = "YOU LOSE!"
            else: result_text = "PUSH (DRAW)"
            game_state = "GAME_OVER"

    # --- 그리기 로직 ---

    # 1. 딜러 카드 (우측 상단)
    d_start_x = SCREEN_WIDTH - 500
    for i, card in enumerate(dealer_hand):
        img = card_images['back'] if i == 1 and game_state == "PLAYER_TURN" else card_images[card]
        screen.blit(img, (d_start_x + i * 40, 50))
    
    # 2. 플레이어 카드 (좌측 하단)
    p_start_x = 100
    for i, card in enumerate(player_hand):
        screen.blit(card_images[card], (p_start_x + i * 40, 400))

    # 3. 점수 텍스트
    p_score_surf = font.render(f"PLAYER: {calculate_score(player_hand)}", True, (255, 255, 255))
    screen.blit(p_score_surf, (p_start_x, 350))
    
    if game_state != "PLAYER_TURN":
        d_score_surf = font.render(f"DEALER: {calculate_score(dealer_hand)}", True, (255, 255, 255))
        screen.blit(d_score_surf, (d_start_x, 240))

    # 4. 버튼 그리기 (플레이어 턴일 때만)
    if game_state == "PLAYER_TURN":
        h_color = (255, 255, 255) if hit_button.collidepoint(mouse_pos) else (200, 200, 200)
        s_color = (255, 255, 255) if stand_button.collidepoint(mouse_pos) else (200, 200, 200)
        
        pygame.draw.rect(screen, h_color, hit_button, border_radius=15)
        pygame.draw.rect(screen, s_color, stand_button, border_radius=15)
        
        # 텍스트가 버튼 중앙에 오도록 조정
        screen.blit(font.render("HIT", True, (0, 0, 0)), (hit_button.x + 45, hit_button.y + 15))
        screen.blit(font.render("STAND", True, (0, 0, 0)), (stand_button.x + 20, stand_button.y + 15))

    # 5. 결과 메시지
    if result_text:
        res_surf = msg_font.render(result_text, True, (255, 215, 0))
        res_rect = res_surf.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        screen.blit(res_surf, res_rect)
        
        hint_surf = font.render("Click anywhere to Restart", True, (200, 200, 200))
        hint_rect = hint_surf.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 80))
        screen.blit(hint_surf, hint_rect)

    pygame.display.flip()

pygame.quit()