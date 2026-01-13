# pip install matplotlib

import matplotlib.pyplot as plt
import pandas as pd

from matplotlib import font_manager, rc
# 한글표기
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
# 음수표기
plt.rcParams['axes.unicode_minus'] = False


# ==========================================================

a = [1, 2, 3]
b = [4, 5, 6]

s1 = pd.Series(b, name='score')
print(s1)
print()

# plt.plot(시리즈)
# plt.plot(s1)
# plt.show()

# plt.plot(x축 자료, y축 자료)
# plt.plot([0, 1, 2], [6, 5, 3], color='blue')
# plt.plot(a, b)
# plt.show()


# 옵션 color, label 적용 해보기 (label 띄우려면 plt.legend())
# plt.plot([-1, 1, 3], [8, 6, 4], color='blue', label='파랑')
# plt.legend()  # 범례
# plt.show()


# marker, linestyle 추가
# title, xlabel, ylabel 적용
# plt.plot(s1, marker='o', color='red', linestyle='dotted', label='연습직선')
# plt.title('이것은 직선', size=20)
# plt.xlabel('엑스축', size=20)
# plt.ylabel('와이축', size=20)

# plt.xlim([-2, 5])
# plt.ylim([2, 9])
# plt.xticks([0, 2, 3], ['aaaa', 'bbbb', 'cccc'], rotation=45)

# plt.legend()  
# plt.show()


# 캔버스 크기 설정 figure(figsize=(10, 8)
# plt.figure(figsize=(10, 8)) # 단위 = 인치
# plt.plot([-1, 1, 3], [8, 6, 4], color='blue', label='파란직선')
# plt.title('이거슨직선', size=20)
# plt.xlabel('엑스축', size=20)
# plt.ylabel('와이축', size=20)
# plt.legend()
# plt.show()

df = pd.DataFrame([a, b], index=['철수', '영희'],  columns=['a', 'b', 'c'])
print(df)
print()

# legend()에 바로 label 적기
plt.plot(df.T)
plt.legend(labels=['철수','영희'])
plt.show()