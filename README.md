# 🌩️ W-BOSS (Weather Base Operations Support System)

![Version](https://img.shields.io/badge/version-2.2-blue.svg)
![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.30+-red.svg)

---

## 📌 프로젝트 개요

**W-BOSS (기상 기반 작전 지원 시스템)**은  
대한민국 공군의 훈련 및 작전 통제를 지원하기 위해 개발된 **기상 통합 분석 대시보드**입니다.

기상청 API + 내부 DB를 동시에 활용하여  
👉 실시간 기상 분석 + 훈련 가능 여부 판단을 수행하는 **의사결정 지원 시스템**입니다.

---

## 🧠 시스템 아키텍처 (계층 구조)

```
        ┌────────────────────────────┐
        │        UI Layer            │
        │  Streamlit (app.py, pages)│
        └─────────────┬──────────────┘
                      │
        ┌─────────────▼──────────────┐
        │      Service Layer         │
        │   (비즈니스 로직 처리)      │
        │ - 훈련 가능 여부 계산       │
        │ - 기상 데이터 가공          │
        └─────────────┬──────────────┘
                      │
        ┌─────────────▼──────────────┐
        │    Repository Layer        │
        │      (DB 접근 계층)        │
        └─────────────┬──────────────┘
                      │
        ┌─────────────▼──────────────┐
        │         MySQL DB           │
        └────────────────────────────┘

            + 외부 API (기상청)
```

---

## 🔄 데이터 흐름 (API + DB 구조 포함)

```
[ 사용자 요청 ]
        │
        ▼
[ Streamlit UI ]
        │
        ▼
[ Service Layer ]
        │
        ├── 외부 API 호출 (기상청)
        │       └─ 단기예보 / 특보 / 실시간 데이터
        │
        ├── 내부 DB 조회 (MySQL)
        │       └─ 사용자 / 로그 / 통계 데이터
        │
        ▼
[ 데이터 가공 및 판단 로직 ]
        │
        ▼
[ 결과 반환 (UI) ]
        │
        ▼
[ 시각화 (차트 / 히트맵 / 카드) ]
```

👉 핵심 특징:
- API + DB를 동시에 사용하는 **하이브리드 데이터 구조**
- 단순 조회가 아닌 **계산/판단 중심 서비스**

---

## 🌟 주요 기능

### 1. 종합 기상 대시보드
- 실시간 기온, 풍속, 강수량, 습도
- 기상 특보 상태
- 이상 기후 탐지
- 시간 흐름 분석

### 2. 훈련 가능 시간 분석
- 단기예보 기반
- 온열지수 / 체감온도 적용
- 색상 단계 (초록 / 노랑 / 빨강)

### 3. 체감온도 히트맵 분석
- 연간 / 월간 패턴
- 훈련 계획 지원

### 4. 사용자 시스템
- 로그인 / 권한 관리
- 마이페이지
- 감사 로그 시스템

---

## 📂 프로젝트 구조

```
AirForceOne/
├── app.py
├── pages/
│   ├── best_train_time.py
│   ├── heatmap.py
│   ├── my_page.py
│   ├── login.py
│   └── register.py
├── services/       # 비즈니스 로직
├── repositories/   # DB 접근
└── utils/          # 공통 유틸
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

## 🏆 설계 특징 (A+ 포인트)

- 계층형 아키텍처 (UI / Service / Repository)
- API + DB 결합 구조 (Hybrid Data Flow)
- 실시간 + 통계 분석 통합
- Audit Log 기반 추적 시스템
- 확장 가능한 모듈 구조

---

**Developed for Air Force 1 · 2026**
