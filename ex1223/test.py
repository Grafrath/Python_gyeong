'''
<기본>
- 조회, 입실, 퇴실, 종료 기능을 제공
- 조회시 호실과 투숙객 이름을 2차원으로 배열 (아래 구현 예시 참조)
- 투숙객 현황을 텍스트파일(txt)로 저장하여 프로그램 재시작 시에 로드 가능하도록 구현

<응용>
- 각종 예외 상황 처리 및 안내 문구 구현 
- 코드에 대한 설명을 주석으로 넣으시오
- 디자인의 완성도를 높이시오
 
<가산점>
- 추가 기능을 넣으시오 
 
<주의사항>
텍스트파일 생성 경로는 루트 디렉토리로 설정 -  './hotel.txt' 

<제출>
이름_hotel.py
(압축하여 제출) 

<구현 예시>
101      102     103

----   ----    ----

201      202     203

----    joy     ----

301      302     303

----    ----    kai
'''

import os

FILE_PATH = "./hotel.txt"

# 호텔 룸 현황 세팅
hotel = {
    "101": "----", "102": "----", "103": "----",
    "201": "----", "202": "----", "203": "----",
    "301": "----", "302": "----", "303": "----"
}

if os.path.exists(FILE_PATH):
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        for line in f:
            room, guest = line.strip().split(",")
            hotel[room] = guest

name = input("\n투숙객 이름: ").strip()
hotel[room] = name
with open(FILE_PATH, "w", encoding="utf-8") as f:
        for r, g in sorted(hotel.items()):
              f.write(f"{r},{g}\n")