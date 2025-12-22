# a = [1,2,3]
# print(a)

# a,b = 3,0

# try:
#     c = a/b
#     print(c)
# except:
#     print("0으로 나눌수 없습니다.")

# try:
#     a = [1,2]
#     print(a[3])
#     b = 4/0
# except ZeroDivisionError:
#     print("0으로 나눌수 없습니다.")
# except IndexError:
#     print("인덱싱 할수없습니다.")

# try:
#     a = [1,2]
#     print(a[3])
#     b = 4/0
# except ZeroDivisionError as e:
#     print(e)
# except IndexError as e:
#     print(e)

# try:
#     a = [1,2]
#     print(a[3])
#     b = 4/0
# except (ZeroDivisionError, IndexError) as e:
#     print(e)

# try:
#     age = int(input("나이를 입력하세요: "))
# except:
#     print('입력이 정확하지 않습니다.')
# else:
#     if age <19:
#         print('미성년자 출입금지.')
#     else:
#         print('환영합니다.')

# students = ['김철수', '이영희', '박민수', '최유진']

# for s in students:
#     try:
#         with open(f'{s}_성적.txt','r') as f:
#             scope = f.read()
#             print(f'{s}의 성적: {scope}')
#     except FileNotFoundError:
#         print(f'{s}의 성적파일이 없습니다')
#         continue


#     print(f'{s} 성적처리 완료')

# print(all([1,2,3]))
# print(all([1,2,3,0]))
# print(all([1,2,3,-1]))
# print(all('학원수업 피곤해'))

# print(dir([1,2,3]))
# print(dir({'1':'a'}))

# print(divmod(7, 3))

# for i, name in enumerate(['body', 'foo', 'bar']):
#     print(i, name)

# eval('1+2')
# eval("'hi' + 'a'")
# eval('divmod(4, 3)')
# print(eval('1+2'))
# print(eval("'hi' + 'a'"))
# print(eval('divmod(4, 3)'))

# def positive(x):
#     return x > 0

# print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

# print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))

# print(hex(234))
# print(oct(73))
# print(int('11', 2))

class Person: pass

a = Person()
b = 3

print(isinstance(a, Person))
print(isinstance(b, Person))

print(max([1,2,3,4,5]))
print(max('python'))

print(min([1,2,3,4,5]))
print(min('python'))

a = pow(2, 100)
b = pow(10, 64)

