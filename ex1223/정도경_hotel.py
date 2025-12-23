import os

FILE_PATH = "./hotel.txt"

# 호텔 룸 현황
hotel = {
    "101": "----", "102": "----", "103": "----",
    "201": "----", "202": "----", "203": "----",
    "301": "----", "302": "----", "303": "----"
}

if os.path.exists(FILE_PATH):
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
            # 두 줄씩 짝을 지어 호텔에 세팅함
            for i in range(0, len(lines), 2):
                roomnums = lines[i].split()
                guestname = lines[i+1].split()
                for r, g in zip(roomnums, guestname):
                    if r in hotel:
                        hotel[r] = g
    except Exception as e:
        print(f"오류: {e}")

# 반복되는 파일 저장을 따로 함수화
def save():
    try:
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            keys = sorted(hotel.keys())
            for i in range(0, 9, 3):
                rooms = keys[i:i+3]
                # 방 번호
                f.write(f"{rooms[0]:<10}{rooms[1]:<10}{rooms[2]:<10}\n")
                # 투숙객 이름
                f.write(f"{hotel[rooms[0]]:<10}{hotel[rooms[1]]:<10}{hotel[rooms[2]]:<10}\n\n")
    except Exception as e:
        print(f"파일 저장 중 오류 발생: {e}")

#기본적으로 계속 반복되는 구조
while True:
    print("\n" + "="*30)
    choice = input("\n[1]조회 [2]입실 [3]퇴실 [4]전체퇴실 [5]종료 선택: ")

    #조회
    if choice == "1":
        print('\n---- 투숙현황 ----\n')
        room_list = sorted(hotel.keys())
        for i in range(0, 9, 3):
            rooms = room_list[i:i+3]
            print(f"{rooms[0]:<10}{rooms[1]:<10}{rooms[2]:<10}")
            print(f"{hotel[rooms[0]]:<10}{hotel[rooms[1]]:<10}{hotel[rooms[2]]:<10}\n")

    # 입실
    elif choice == "2":
        room = input("\n입실할 호실 번호: ")
        if room in hotel:
            if hotel[room] == "----":
                name = input("\n투숙객 이름: ").strip()
                if name:
                    hotel[room] = name
                    save()
                    print(f"\n{room}호 입실 완료.")
                else:
                    print("\n이름을 입력하세요.")
            else:
                print(f"\n{room}호는 이미 투숙 중입니다.")
        else:
            print("\n존재하지 않는 호실입니다.")

    # 퇴실
    elif choice == "3":
        room = input("\n퇴실할 호실 번호: ")
        if room in hotel and hotel[room] != "----":
            hotel[room] = "----"
            save()
            print(f"\n{room}호 퇴실 처리 완료.")
        else:
            print("\n 투숙객이 없습니다.")

    # 전체 한번에 퇴실
    elif choice == "4": 
        allclear = input("\n정말 모든 방을 퇴실 처리하시겠습니까? (y/n): ")
        if allclear.lower() == 'y':
            for r in hotel:
                hotel[r] = "----"
            save()
            print("\n전체 퇴실 처리 완료.")

    elif choice == "5":
        print("\n프로그램을 종료합니다.")
        break

    else:
        print("잘못된 선택입니다.")