<img src="https://capsule-render.vercel.app/api?type=wave&color=ef7070&height=150&section=header&text=RedButton&fontSize=50&fontColor=ffffff" />

## ❓ 주제
RedButton 보드게임 데이터 기반 공급현황 시각화 대시보드
- 지역별 보유 현황 분석을 통한 공급 불균형 해결 인사이트 도출<br><br>
  
## ✋ 개요
보드게임 프랜차이즈이니 RedButton 웹 사이트를 크롤링하여 지역/지점별 보드게임 보유 현황을 시각화하고, 지역/지점별 특징 확인, 공급 불균형 해소 등에 기여할 수 있는 대시보드 형태의 웹 사이트를 구현하는 것을 목표로 함.  
📅 진행기간 : 2025.0418-2025.04.24<br><br> 

## 🙂 주제 선정 배경
- RedButton의 경우, 지역/지점마다 보유한 게임 구성 차이가 큼
- 홈페이지에서는 지점별 보유 게임은 확인할 수 있으나, 지역 전체를 한눈에 파악하거나 비교할 수는 없음
- 소비자 입장에서 출발한 기획이었으나, 회사 입장에서도 필요성이 크다고 판단하여 방향 전환
- 회사 내부 운영자가 지점별 공급 현황을 빠르게 확인할 수 있도록 시각화 대시보드로 기획
- 홈페이지에서 제공되는 데이터에는 한계가 있으나, 주어진 데이터로 최대한 유의미한 인사이트를 제공하고자 함<br><br>

## ✍️ 프로젝트 목적
- 지역/지점별 보유 게임 현황 등의 정보를 시각적으로 요약 → 공급 불균형 파악 및 개선에 기여
- 내부 담당자가 보급률, 고유 게임, 미보유 지점을 빠르게 파악 가능
- 향후 게임 정보/실적/고객 선호도 등과 연계하여 확장 가능성 확보<br><br>

## 🙆 팀원 및 역할 🙆‍♀️

| 팀원   | 담당                  | 내용                                                                                      |
|--------|---------------------|-----------------------------------------------------------------------------------------|
| 최현욱 | 백엔드               | - Django DB에 업데이트 될 보드게임 매장 정보를 바탕으로 모델 생성 <br> - 템플릿에 표시될 통계 데이터 계산/전달코드 구현 <br> - 이달의 게임 리스트 tooltip 구현 |
| 배진현 | 크롤링, 전처리, 시각화 | - 프로젝트 아이디어 도출 및 웹 사이트 UI/UX 프로토타이핑 <br> - 보드게임명, 이 달의 게임명 크롤링, 이 달의 게임 보유 여부 전처리 <br> - 시각화 차트(bar, wordcloud, heatmap) 및 완성본 제작 |
| 최시은 | 크롤링, 전처리, 시각화 | - RedButton 홈페이지 내 지역/지점별 보드게임명 크롤링 <br> - 데이터 전처리(지역/지점별로 게임 목록과 보유 여부 전처리) <br> - 시각화 차트(bar, wordcloud, heatmap) 초안 제작 |
| 차소연 | 프론트엔드            | - 지역별 보드게임 현황 대시보드 구축 <br> - 지점별 보유/미보유 게임 정보를 토글 방식으로 구현 <br> - 파이차트, 막대차트, 워드클라우드, 히트맵 시각화 이미지 연결 |
| 송예준 | 백엔드               | - Django DB에 업데이트 될 이 달의 게임 정보를 바탕으로 모델 생성 <br> - Django DB에서 지역명을 가져오고 중복 제거 및 원하는 순서로 정렬 <br> - 히트맵 가로 스크롤 구현 | <br><br>
<br>

## 💟 결과 💟
![image](https://github.com/user-attachments/assets/bd2d2e0a-57a8-42f5-9668-4525a52d562c)
![image (1)](https://github.com/user-attachments/assets/cd2a56ed-8649-41c1-93d0-eceef4be40cb)

**1. 지역별 Top 5 지점의 보유/미보유 게임 현황 - 막대차트**
- 지점별 보유 게임 수와 미보유 게임 수를 나란히 보여주는 묶은 막대차트
- 각 지점의 보유율(%)도 함께 표시하여 상대적인 공급 수준을 시각화<br><br>
![image (2)](https://github.com/user-attachments/assets/b2aecf52-b0cd-4159-a2e2-cf4b7b3fd98b)

**2. 지역별 고유 보드게임 - 워드클라우드**
- 해당 지역에서만 보유하고 있는 보드게임을 시각적으로 표현
- 단어 크기는 지역 내에서 해당 게임을 보유한 지점 수에 따라 결정<br><br>
![image (3)](https://github.com/user-attachments/assets/004ef8ba-6419-4005-8e41-1f6a31e18648)

**3. 전체 지점 보유/미보유 게임 현황 - 히트맵**
- 모든 지점의 보유 게임 수, 미보유 게임 수를 색 대비를 활용한 격자형 히트맵으로 표현
- 지점 간 편차를 색상 강도로 명확히 보여줌<br><br>
![image (4)](https://github.com/user-attachments/assets/63977266-7f77-4a4a-9c53-15baffc7247c)

**4. “이 달의 게임” 보유/미보유 지점 비율 - 파이 차트**
- “이 달의 게임” 10종을 기준으로, 해당 지역 지점들의 전체 보유 여부 비율을 시각화
- 하나라도 보유하지 않은 지점은 미보유로 처리됨<br><br>
![image (5)](https://github.com/user-attachments/assets/58385a30-f1e4-4a6b-978d-11af237f5f07)<br><br>


## 💡 기대효과 💡
**활용 가능성**
- 지역/지점별 보유 게임 수와 미보유 현황을 한눈에 확인할 수 있어 지점별 공급 전략 수립에 도움
- "이달의 게임" 보유 여부와 같은 기준을 활용해 인기 게임의 실제 공급률을 파악 가능
- 특정 지역에서만 보유 중인 고유 보드게임 파악을 통해 지점의 큐레이션 특성 분석 및 마케팅 활용 가능
- 내부 운영자가 쉽게 활용할 수 있는 비전문가 친화적인 웹 대시보드로 구현되어, 실무 적용성 높음

**확장 가능성**
- 실적 데이터와 연계할 경우, 게임 구성과 매출 간의 상관관계 분석 가능
- 추천인원, 플레이시간, 난이도 등 게임 메타데이터를 연동하여 점포 맞춤형 추천 시스템으로 확장 가능
- 고객 선호도 및 리뷰 등 외부 데이터를 연결하면 수요 예측 기반 공급 추천 시스템으로 발전 가능
- 관리자 권한 기능을 추가해 신규 게임 추가, 공급 요청 등의 관리 기능으로 확장 가능<br><br>

## 💫 Tech Stack 💫

<div style="display: flex; gap: 8px;">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/html5r-E34F26?style=flat-square&logo=Jupyter&logoColor=white"/>
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=Jupyter&logoColor=white"/>
  <img src="https://img.shields.io/badge/selenium-43B02A?style=flat-square&logo=Jupyter&logoColor=white"/>
</div>
<div style="display: flex; gap: 8px;">
  <img src="https://img.shields.io/badge/django-092E20?style=flat-square&logo=Jupyter&logoColor=white"/>
  <img src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=Jupyter&logoColor=white"/>
  <img src="https://img.shields.io/badge/numpy-013243?style=flat-square&logo=Jupyter&logoColor=white"/>
  <img src="https://img.shields.io/badge/css-663399?style=flat-square&logo=Jupyter&logoColor=white"/>
</div>
<img src="https://capsule-render.vercel.app/api?type=wave&color=ef7070&height=150&section=footer&text=Bulk-Up&fontSize=30&fontColor=ffffff" />
