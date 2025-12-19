import os

path = './ex1219'

if not os.path.exists(path) :
    os.makedirs(path)

# f = open('./ex1219/새파일.txt', 'w', encoding='utf-8')
# for i in range(1,11) :
#     data = f'{i}번째 줄입니다.\n'
#     f.write(data)
# f.close()

# print('/n======== 한줄 읽기 ========\n')
# f = open('./ex1219/새파일.txt', 'r', encoding='utf-8')
# line = f.readline()
# print(line)
# f.close()

# print('/n======== while 읽기 ========\n')
# f = open('./ex1219/새파일.txt', 'r', encoding='utf-8')
# while True :
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

# print('/n======== for리스트 읽기 ========\n')
# f = open('./ex1219/새파일.txt', 'r', encoding='utf-8')
# lines = f.readlines()
# print(lines)

# for line in lines :
#     line = line.strip()
#     print(line)
# f.close()

# print('/n======== read 읽기 ========\n')

# f = open('./ex1219/새파일.txt', 'r', encoding='utf-8')
# data = f.read()
# print(data)
# f.close()

# print('/n======== 추가하기 ========\n')
# f = open('./ex1219/새파일.txt', 'a', encoding='utf-8')
# for i in range(11,21) :
#     data = f'{i}번째 줄입니다.\n'
#     f.write(data)
# f.close()

# f = open('./ex1219/새파일.txt', 'r', encoding='utf-8')
# data = f.read()
# print(data)
# f.close()

# print('/n======== with 으로 추가하기 ========\n')
# f = open('./ex1219/새파일.txt', 'w', encoding='utf-8')
# f.write("Life is too short, you need python")
# f.close()
# f = open('./ex1219/새파일.txt', 'r', encoding='utf-8')
# line = f.readline()
# print(line)
# f.close()

# 위와 동일하게 작동, close 자동 처리
# with open('./ex1219/새파일.txt', 'w', encoding='utf-8') as f:
#     f.write("Life is too short, you need python")

# f = open('./ex1219/새파일.txt', 'r', encoding='utf-8')
# line = f.readline()
# print(line)
# f.close()

# print('/n======== os.path.exists ========\n')
# file_path = './poo.txt'
# if not os.path.exists(file_path) :
#     with open(file_path, 'w', encoding='utf-8') as f:
#         f.write("Life is too short, you need python")

# f = open(file_path, 'r', encoding='utf-8')
# line = f.readline()
# print(line)
# f.close()

'''
21이거나 가까우면 우승
플레이어는 카드를 원할경우 더 받을수 있다.
원하지 않을경우 스톱
21을 넘어가면 무조건 패배
단 둘다 21을 넘어가면 21에 가까운 사람이 승리
둘다 스톱시 카드 공개

카드는 1~10
기본으로 3장 받음

1:1이라 카드 중복없음 (셋)
'''