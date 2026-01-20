import matplotlib.pyplot as plt
import numpy as np
import platform

# 한글 폰트 설정
if platform.system() == 'Windows':
    plt.rcParams['font.family'] = 'Malgun Gothic'
else:
    plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False

# 색상 팔레트
colors = {
    'primary': '#636E72',   # 텍스트 (제목)
    'blue': '#74B9FF',      # 그래프 선 색상
    'bg': '#FFFFFF'         # 배경
}

# 1행 3열 서브플롯 생성
fig, axes = plt.subplots(1, 3, figsize=(10, 4))
plt.subplots_adjust(wspace=0.2) # 그래프 간 간격

# 공통 x축 데이터
x = np.linspace(-2, 2, 400)

# 1. 극값을 갖는 경우 (서로 다른 두 실근을 갖는 도함수)
# y = x^3 - 3x (도함수 y' = 3x^2 - 3 -> x=1, -1에서 극값)
y1 = x**3 - 3*x
axes[0].plot(x, y1, color=colors['blue'], lw=3)

# 2. 극값은 없으나 순간 기울기가 0인 점이 있는 경우 (중근을 갖는 도함수 - 삼중근 형태)
# y = x^3 (도함수 y' = 3x^2 -> x=0에서 기울기 0)
y2 = x**3
axes[1].plot(x, y2, color=colors['blue'], lw=3)

# 3. 극값도 없고 순간 기울기가 0인 점도 없는 경우 (허근을 갖는 도함수)
# y = x^3 + 2x (도함수 y' = 3x^2 + 2 -> 항상 양수)
y3 = x**3 + 2*x
axes[2].plot(x, y3, color=colors['blue'], lw=3)

# 모든 서브플롯 공통 스타일 적용 (축 제거)
for ax in axes:
    ax.axis('off')  # 축, 라벨, 테두리 모두 제거

# 전체 제목 설정
fig.suptitle('삼차방정식 그래프의 개형', fontsize=16, fontweight='bold', color=colors['primary'])

# 레이아웃 설정
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('concept_image_cubic.png', dpi=100, bbox_inches='tight')
plt.close()