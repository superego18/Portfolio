import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import matplotlib.font_manager as fm
# font_path = 'C:\Windows\Fonts\BAUHS93.ttf'
# fontprop = fm.FontProperties(fname=font_path, size=10)

df1 = pd.read_excel('mbti\mbti.xlsx', sheet_name='output1', index_col=0)

categories1 = df1.columns.tolist()
categories1 = [*categories1, categories1[0]]
grades1 = df1.loc['val']
grades1 = [*grades1, grades1[0]]

label_loc = np.linspace(start=0, stop=2*np.pi, num=len(grades1))

fig=plt.figure(figsize=(8,8), facecolor='black')
# fig.patch.set_alpha(1) ## 투명도 설정

ax = plt.subplot(polar=True)

ax.set_theta_offset(np.pi/2) # 시작점
ax.set_theta_direction(1) # 그려지는 방향: 반시계방향

plt.xticks(label_loc, labels=categories1, fontsize=30)
plt.ylim(50,80)

ax.patch.set_facecolor('black') # axes 배경색
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')

# ax.axvspan(70,80, facecolor='gray', alpha=0.6) # 부분 색칠 - 각도

ax.plot(label_loc, grades1, label='MBTI', linestyle='solid', color='red')
ax.fill(label_loc, grades1, color='red', alpha=0.5) 
ax.legend()
plt.savefig('mbti/mbti1.png')
plt.show(block=False)
plt.pause(3) 
plt.close()

###

df2 = pd.read_excel('mbti\mbti.xlsx', sheet_name='output2', index_col=0)

categories2 = df2.columns.tolist()
categories2 = [*categories2, categories2[0]]
grades2 = df2.loc['val']
grades2 = [*grades2, grades2[0]]

label_loc = np.linspace(start=0, stop=2*np.pi, num=len(grades2))

fig=plt.figure(figsize=(8,8), facecolor='black')
# fig.patch.set_alpha(1) ## 투명도 설정

ax = plt.subplot(polar=True)

ax.set_theta_offset(np.pi/2) # 시작점
ax.set_theta_direction(1) # 그려지는 방향: 반시계방향

plt.xticks(label_loc, labels=categories2, fontsize=30)
plt.ylim(50,80)

ax.patch.set_facecolor('black') # axes 배경색
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')

# ax.axvspan(70,80, facecolor='gray', alpha=0.6) # 부분 색칠 - 각도

ax.plot(label_loc, grades2, label='MBTI', linestyle='solid', color='red')
ax.fill(label_loc, grades2, color='red', alpha=0.5) 
ax.legend()
plt.savefig('mbti/mbti2.png')
plt.show(block=False)
plt.pause(3) 
plt.close()