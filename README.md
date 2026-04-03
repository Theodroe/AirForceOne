# 🌩️ W-BOSS (Weather Base Operations Support System)

![Version](https://img.shields.io/badge/version-2.2-blue.svg)
![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.30+-red.svg)

---

## 🧠 시스템 아키텍처

```
        ┌───────────────────────┐
        │     Streamlit UI      │
        │  (app.py, pages/)     │
        └─────────┬─────────────┘
                  │
        ┌─────────▼─────────────┐
        │    Service Layer      │
        │ (services/ business)  │
        └─────────┬─────────────┘
                  │
        ┌─────────▼─────────────┐
        │   Repository Layer    │
        │   (DB 접근 로직)       │
        └─────────┬─────────────┘
                  │
        ┌─────────▼─────────────┐
        │      MySQL DB         │
        └───────────────────────┘

        + 외부 API (기상청)
```

---

## 🔄 데이터 흐름 (Data Flow)

1. 사용자가 Streamlit UI에서 요청 발생  
2. 요청이 Service Layer로 전달됨  
3. Service Layer:
   - 기상청 API 호출 (단기예보, 특보 등)
   - 비즈니스 로직 처리 (훈련 가능 여부 계산 등)
4. 필요 시 Repository Layer 통해 DB 조회/저장  
5. 가공된 데이터 → UI로 반환  
6. Streamlit에서 시각화 (차트, 히트맵, 카드)

---

## 🌟 주요 기능

### ✔ 실시간 기상 분석
- 기온 / 풍속 / 강수 / 습도
- 기상 특보 상태
- 이상 기후 감지

### ✔ 훈련 가능 시간 분석
- 온열지수 / 체감온도 기반
- 색상 단계 표시 (초록/노랑/빨강)

### ✔ 연간 히트맵 분석
- 월별 / 일별 패턴
- 장기 훈련 계획 지원

### ✔ 사용자 관리 시스템
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

```
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

- 계층형 아키텍처 (UI / Service / Repository 분리)
- 외부 API + 내부 DB 혼합 구조
- Streamlit 기반 SPA
- 로그 기반 감사 시스템 (Audit Trail)
- 확장 가능한 모듈 구조

---

**Developed for Air Force 1 · 2026**
