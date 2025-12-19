import random

def cal_score(hand):
    score = 0
    ace_count = 0
    
    for card in hand:
        if card in ['J', 'Q', 'K']:
            score += 10
        elif card == 'A':
            score += 11
            ace_count += 1
        else:
            score += int(card)
            
    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1
        
    return score

while True:
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    card_deck = ranks * 4
    random.shuffle(card_deck)

    player = [card_deck.pop(), card_deck.pop()]
    dealer = [card_deck.pop(), card_deck.pop()]

    print(f"\n게임 시작! 딜러의 첫번째 카드: {dealer[0]}")

    while True:
        p_score = cal_score(player)
        print(f"\n당신의 카드: {player} (합계: {p_score})")
        print()
        
        if p_score > 21:
            print("21을 초과했습니다. 패배!")
            break
        if p_score == 21:
            print("카드의 합이 21 입니다. 차례를 마칩니다.")
            break

        choice = input("카드를 더 받으시겠습니까? 1.Draw, 2.Stop: ")
        if choice == '1':
            player.append(card_deck.pop())
        else:
            break

    p_score = cal_score(player)

    if p_score <= 21:
        print("\n-------- 딜러의 차례 --------")
        print(f"딜러의 카드: {dealer} (합계: {cal_score(dealer)})")
        
        while cal_score(dealer) <= 16:
            new_card = card_deck.pop()
            dealer.append(new_card)
            print(f"딜러가 카드를 뽑았습니다: {new_card} (합계: {cal_score(dealer)})")

        d_score = cal_score(dealer)
        print("\n-------- 최종 결과 --------")
        print(f"플레이어: {p_score} | 딜러: {d_score}")

        if d_score > 21:
            print("플레이어 승리!")
        elif p_score > d_score:
            print("플레이어 승리!")
        elif p_score < d_score:
            print("딜러 승리!")
        else:
            print("무승부!")

    print()

    retry = input("한 게임 더 하시겠습니까? (y/n): ").lower()
    if retry != 'y':
        print("게임을 종료합니다. 이용해 주셔서 감사합니다!")
        break