import pandas as pd
import matplotlib.pyplot as plt
import locale

locale.setlocale(locale.LC_ALL, 'korean')
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 500)


from matplotlib import font_manager, rc
#한글표기
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
# 음수표기
plt.rcParams['axes.unicode_minus'] = False

# a = [1, 2, 3]
# b = [10, 20, 30]

# plt.plot([0,1,2],[6,5,3])
# plt.show()

# plt.plot([-1,1,3], [8,6,4], color='blue', label='파랑')
# plt.show()

# plt.figure(figsize=(10, 8))
# plt.plot([-1,1,3], [8,6,4], color='blue', label='파랑')
# plt.title('직선', size=20)
# plt.xlabel('엑스축', size=20)
# plt.ylabel('와이축', size=20)
# plt.legend()
# plt.show()

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0, 0].plot(range(1, 10), range(11, 20), marker='s')
axes[0, 0].set_title('일번 그래프')
axes[0, 0].set_xlabel('일번 엑스축')
axes[0, 0].set_ylabel('일번 와이축')
axes[0, 0].legend(labels=['일번 레전드'])
