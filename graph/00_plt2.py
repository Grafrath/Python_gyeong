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

# 더 구체적인 설정 
# fig(figure) = 전체 캔버스
# ax(axes) = (실제 그래프가 그려지는 영역) Axes 객체
# axis → 축 한 줄 (x축, y축)
# axes → x축 + y축 + 그래프 영역 전체
# fig, ax = plt.subplots(1, 1, figsize=(8,6))
# ax.plot(range(1, 10), range(11, 29, 2), marker='D', label='내그래프')
# ax.set_title('엄청난그래프')
# ax.set_xlabel('대단한가로축')
# ax.set_ylabel('놀라운와이축')
# ax.legend()
# plt.show()


# 여러 그래프 그리기 subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# 0,0 그래프
axes[0,0].plot(range(1, 10), range(11, 20), marker='s')
axes[0,0].set_title('일번그래프')
axes[0,0].set_xlabel('일번엑스축')
axes[0,0].set_ylabel('일번와이축')
axes[0,0].legend(labels=['일번레전드'])

# 0,1 그래프
a = [7,8,9]
sr1 = pd.Series(a)
axes[0,1].plot(sr1, marker='d')

# 1,0 그래프 (또 다른 방법 그리기)
b = [8, 9, 10]
sr2 = pd.Series(b)

sr2.plot(ax=axes[1,0], color='orange')
# axes[1,0].set_xticks(range(0, 11, 1), [1,2,3,3,2,5,76,9,0,-1,-100])
axes[1,0].set_xticks([1, 2, 5], [5, 4, 'a'])
axes[1,0].set_yticks(range(0, 101, 10))


# 1,1 그래프
c = range(10, 101, 10) # 파이썬 배열

import numpy as np
d = np.arange(100, 9, -10) # 넘피 배열

df = pd.DataFrame({'숫자1':c, '숫자2':d}, index=range(10, 101, 10))
print(df)

axes[1,1].plot(df)
axes[1,1].annotate('엑스맨', xy=(45, 80), size=20)

# fig 활용 예시
fig.suptitle('여러 그래프들', size=20) 
plt.show()