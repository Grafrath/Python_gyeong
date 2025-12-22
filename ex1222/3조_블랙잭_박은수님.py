import random
import time

# ---------- 게임 시작 안내 ----------
print("=" * 100)
print("🎰 블랙잭 게임에 오신 것을 환영합니다!")
print()
print("📜 게임 설명")
print("- 카드는 1 ~ 10 까지 중복없이 지급됩니다.")
print("- 플레이어와 컴퓨터는 기본으로 2장을 받습니다.")
print("- 카드를 더 받을지(y) 스톱할지(n) 선택할 수 있습니다.")
print("- 합이 21에 가장 가까운 쪽이 승리합니다.")
print("- 21을 넘으면 버스트로 패배합니다.")
print("- 둘 다 21을 넘으면 21에 더 가까운 쪽이 승리합니다.")
print("- 시작하자마자 21이면 블랙잭으로 즉시 승리합니다.")
print("=" * 100)
input("▶ Enter를 누르면 게임을 시작합니다...")

win_count = 0  # 연승 카운트

# ---------- 게임 반복 ----------
while True:
    # ---------- 카드 덱 ----------
    deck = list(range(1, 11))
    random.shuffle(deck)

    def draw_card():
        return deck.pop()

    # ---------- 기본 카드 지급 ----------
    player_cards = [draw_card() for i in range(2)]
    computer_cards = [draw_card() for i in range(2)]

    player_sum = sum(player_cards)
    computer_sum = sum(computer_cards)

    game_over = False
    result = None

    player_stopped = False
    computer_stopped = False

    # ---------- 시작 즉시 블랙잭 처리 ----------
    if player_sum == 21 and computer_sum == 21:
        print("\n 더블 블랙잭! 무승부!")
        result = "draw"
        game_over = True
    elif player_sum == 21:
        print("\n BLACK JACK!! 플레이어 즉시 승리!")
        result = "win"
        game_over = True
    elif computer_sum == 21:
        print("\n 컴퓨터 BLACK JACK! 패배...")
        result = "lose"
        game_over = True

    # ---------- 턴제 게임 ----------
    while not game_over:
        # ----- 플레이어 턴 -----
        if not player_stopped:
            player_sum = sum(player_cards)
            print(f"\n 플레이어 카드: {player_cards}")
            print(f" 카드 장수: {len(player_cards)}장 / 합계: {player_sum}")

            if player_sum > 21:
                print(" 플레이어 BURST!")
                result = "lose"
                game_over = True
                break

            choice = input("카드를 더 받으시겠습니까? (y / n): ")
            if choice == 'y':
                if len(deck) == 0:
                    print("덱에 카드가 없습니다.")
                    player_stopped = True
                else:
                    player_cards.append(draw_card())
                    # 여기서 바로 출력
                    print(f" 새로운 카드 지급! 현재 카드: {player_cards} (장수: {len(player_cards)})")
            else:
                player_stopped = True
                print(" 플레이어가 스톱했습니다.")
        # ----- 컴퓨터 턴 -----
        if not computer_stopped and not game_over:
            computer_sum = sum(computer_cards)
            print("\n 컴퓨터 턴...")
            time.sleep(3)

            if computer_sum > 21:
                print(" 컴퓨터 BURST!")
                result = "win"
                game_over = True
                break

            if computer_sum < 17 and len(deck) > 0:
                print(" 컴퓨터가 카드를 뽑습니다...")
                time.sleep(1)
                computer_cards.append(draw_card())
                print(f" 현재 카드 장수: {len(computer_cards)}장")
                time.sleep(0.8)
            else:
                computer_stopped = True
                print(" 컴퓨터는 카드를 뽑지 않습니다.")
                time.sleep(1)

        # ----- 둘 다 스톱이면 종료 -----
        if player_stopped and computer_stopped:
            break

    # ---------- 최종 카드 공개 ----------
    player_sum = sum(player_cards)
    computer_sum = sum(computer_cards)

    print("\n===== 카드 공개 =====")
    print(f" 플레이어 카드: {player_cards} (합: {player_sum})")
    print(f" 컴퓨터 카드: {computer_cards} (합: {computer_sum})")

    # ---------- 승패 판정 ----------
    if not game_over:
        if player_sum > 21 and computer_sum > 21:
            result = "win" if abs(21 - player_sum) < abs(21 - computer_sum) else "lose"
        elif player_sum > 21:
            result = "lose"
        elif computer_sum > 21:
            result = "win"
        else:
            if abs(21 - player_sum) < abs(21 - computer_sum):
                result = "win"
            elif abs(21 - player_sum) > abs(21 - computer_sum):
                result = "lose"
            else:
                result = "draw"

    # ---------- 연승 처리 ----------
    if result == "win":
        win_count += 1
        print(f"\n 승리! 현재 연승: {win_count}연승")
    elif result == "lose":
        win_count = 0
        print("\n 패배… 연승이 초기화되었습니다.")
    else:
        print(f"\n 무승부 (연승 유지: {win_count}연승)")

    # ---------- 다시하기 ----------
    again = input("\n다시 플레이하시겠습니까? (y / n): ")
    if again != 'y':
        print("\n게임을 종료합니다. 플레이해주셔서 감사합니다!")
        break
