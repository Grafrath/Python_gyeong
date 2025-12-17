
# 리스트는 [], 튜플은 ()
# 리스트는 요솟값의 생성, 삭제, 수정이 가능하지만, 튜플은 요솟값을 바꿀 수 없다.

t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

# del t3[0]  -- 튜플은 삭제 불가  TypeError: 'tuple' object doesn't support item deletion



print("\n======= 인덱싱/슬라이싱 =======")

t1 = (1, 2, 'a', 'b')
print(t1)
print(t1[0])
print(t1[3])
print(t1[1:])


print("\n======= 더하기/곱하기 =======")

t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t3 = t1 + t2
print(t3)
print()

t3 = t2 * 3
print(t3)  # (3, 4, 3, 4, 3, 4)
print()

# t3[0] = 1  -- 수정 불가 TypeError: 'tuple' object does not support item assignment



print("\n======= 튜플 길이 구하기 =======")
print(len(t3))
print()


student = [
    ("지민", 16, 1),
    ("태현", 17, 2),
    ("윤기", 16, 1)
]

# 학생 리스트에 남준/18/3 추가하기
# 태현이 전학갔으므로 삭제하기
print()
print()

new = ("남준", 18, 3)
print("새로운 전학생 : ", new[0])
student.append(new)

print("떠난 학생 : ", student[1][0])
del student[1]
print()

print(student)
print()


student_list = f"""
이름\t나이\t학년
====================
{student[0][0]}\t{student[0][1]}\t {student[0][2]}
{student[1][0]}\t{student[1][1]}\t {student[1][2]}
{student[2][0]}\t{student[2][1]}\t {student[2][2]}
====================
"""
print(student_list)


