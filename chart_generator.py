import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from wordcloud import WordCloud
from collections import Counter
from functools import reduce
import matplotlib.patches as mpatches
# 사용자로부터 선택된 지역 (웹 연동 시 query param 또는 form 값으로 전달됨)
selected_region = "제주"  # 예시 지역 (웹에선 동적으로 바뀔 것)

# 지역 필터링
region_df = df[df["지역"] == selected_region].copy()
region_df["지역_지점"] = region_df["지역"] + " - " + region_df["지점명"]



# Top 5 보유 지점
top5 = region_df.sort_values(by='보유 게임 수', ascending=False).head(5).reset_index(drop=True)

# 5개 미만 시 빈 막대 추가
while len(top5) < 5:
    top5 = pd.concat([top5, pd.DataFrame([{
        '지점명': '',
        '보유 게임 수': 0,
        '미보유 게임 수': 0
    }])], ignore_index=True)

# 차트 생성
fig, ax = plt.subplots(figsize=(10, 6))
x = np.arange(len(top5))
bar_width = 0.35  # 각 막대 너비 줄이기

# 비율 계산
top5["총 게임 수"] = top5["보유 게임 수"] + top5["미보유 게임 수"]
top5["보유 비율"] = (top5["보유 게임 수"] / top5["총 게임 수"] * 100).fillna(0)
top5["미보유 비율"] = (top5["미보유 게임 수"] / top5["총 게임 수"] * 100).fillna(0)

# 색상 설정
colors = {
    '보유': '#FFB3B3',
    '미보유': '#AEDFF7'
}

# 묶은 막대 그리기
bar1 = ax.bar(x - bar_width/2, top5['보유 게임 수'], width=bar_width,
              color=colors['보유'], edgecolor='black', label='보유 게임 비율')
bar2 = ax.bar(x + bar_width/2, top5['미보유 게임 수'], width=bar_width,
              color=colors['미보유'], edgecolor='black', label='미보유 게임 비율')

# 비율 텍스트 표시 (각 막대 위에 표시)
for i in range(len(top5)):
    if top5["지점명"][i] != "":
        ax.text(x[i] - bar_width/2, top5['보유 게임 수'][i] + 3,
                f"{top5['보유 비율'][i]:.1f}%", ha='center', va='bottom', fontsize=11)
        ax.text(x[i] + bar_width/2, top5['미보유 게임 수'][i] + 3,
                f"{top5['미보유 비율'][i]:.1f}%", ha='center', va='bottom', fontsize=11)

# X축 설정
ax.set_xticks(x)
ax.set_xticklabels(top5['지점명'], fontsize=14, fontweight="bold")

# 타이틀 (좌측 정렬)
ax.set_title(f"{selected_region} 지역 Top 5 지점의 보유 게임 비율",
             fontsize=20, fontweight="bold", loc='left', pad=10)

# y축 레이블
ax.set_ylabel("게임 수", fontsize=14, fontweight="bold")

# 범례 (타이틀 오른쪽 우상단)
ax.legend(loc='center left', bbox_to_anchor=(0.815, 1.06), fontsize=10)

fig.tight_layout()
plt.show()

# 차트 저장
file_name = f"{selected_region} 막대 차트.png"
fig.savefig(file_name, dpi=300, bbox_inches='tight')