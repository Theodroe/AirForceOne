# 🌩️ W-BOSS (Weather Base Operations Support System)

![Version](https://img.shields.io/badge/version-2.2-blue.svg)
![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.30+-red.svg)

W-BOSS는 기상 기반 훈련/작전 지원을 위한 Streamlit 대시보드입니다.  
기상 데이터와 내부 DB를 기반으로 실시간 분석, 훈련 가능 여부 판단, 사용자 관리 기능을 제공합니다.

---

## 🧠 시스템 아키텍처

- **UI Layer**: Streamlit (`app.py`, `pages/`)
- **Service Layer**: `services/` (비즈니스 로직)
- **Data Layer**: `repositories/` (DB 접근)
- **Utility Layer**: `utils/` (설정 및 공통 기능)

---

## 🌟 주요 기능

### 1. 메인 대시보드 (`app.py`)
- 주요 기능 진입 허브
- 실시간 현황 / 연간 분석 페이지 이동
- 요약 카드 기반 UI

### 2. 실시간 현황 (`heatmap.py`)
- 기상 데이터 기반 현황 분석
- 시간대별 상세 조회
- 시각화 (라인/히트맵 등)

### 3. 훈련 가능 시간 분석 (`best_train_time.py`)
- 단기예보 기반 훈련 가능 여부 계산
- 시간대별 위험도 표시

### 4. 마이페이지 (`my_page.py`)
- 사용자 정보 조회
- 계급 수정
- 비밀번호 변경
- 계정 탈퇴
- 접속 로그 / 감사 로그 조회

---

## 📂 디렉토리 구조

```text
project/
├── app.py
├── requirements.txt
├── README.md
│
├── pages/
│   ├── home.py
│   ├── best_train_time.py
│   ├── heatmap.py
│   ├── my_page.py
│   ├── login.py
│   ├── register.py
│   └── delete.py
│
├── services/
├── repositories/
├── utils/
```

---

## ⚙️ 실행 방법

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔑 환경 설정

```toml
[api]
SHORT_TERM_FORECAST_API_KEY="..."

[db]
host="..."
user="..."
password="..."
database="..."
```

---

*AirForceOne Project · 2026*
