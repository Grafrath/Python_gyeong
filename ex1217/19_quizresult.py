# 장바구니에 있는 물품 총 금액 계산

cart = [
    ("신발", 89000),
    ("셔츠", 39000),
    ("청바지", 69000),
    ("모자", 19000)
]
total = cart[0][1] + cart[1][1] + cart[2][1] + cart[3][1]
print("총 금액: ", total)

# 아이디 부분 (@ 압부분만) 추출하기  
# 스플릿 사용 해보기

email = "hello_python@naver.com"
id_part = email.split("@")[0]   # ['hello_python', 'naver.com']
print(id_part)


# 중복을 제거한 메뉴 리스트로 만들기

menu = ["김치찌개", "된장찌개", "비빔밥", "김치찌개", "불고기", "비빔밥"]
food_menu = list(set(menu))
print(food_menu)

# 이름과 나이만 따로 변수에 저장하기

member = {
    "id": "user001",
    "name": "홍길동",
    "age": 30,
    "email": "gil@example.com"
}
name = member['name']
age = member['age']
print(f"이름: {name}, 나이: {age}")

# "치즈"가 있는지 없는지 확인하기
# in 

cart = ["우유", "빵", "달걀", "치즈"]

print("치즈" in cart)