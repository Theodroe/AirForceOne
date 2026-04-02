import streamlit as st

SERVICE_KEY = st.secrets.get("api", {}).get("SHORT_TERM_FORECAST_API_KEY", "")

AREA_INFO: dict[str, dict] = {
    "연천": {"nx": 61, "ny": 138},
    "철원": {"nx": 65, "ny": 139},
    "양구": {"nx": 77, "ny": 139},
    "화천": {"nx": 72, "ny": 139},
    "고성": {"nx": 85, "ny": 145},
}

SUMMER_MONTHS: list[int] = [5, 6, 7, 8, 9]
ALL_HOURS: list[str] = [f"{i:02d}" for i in range(24)]
DAY_HOURS: list[str] = [f"{i:02d}" for i in range(6, 18)]

STATUS_COLOR: dict[str, str] = {
    "go": "#00c853",
    "caution": "#ffd600",
    "restrict": "#ff6d00",
    "stop": "#d50000",
}

API_URL = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst"
API_ROWS = 1000
API_CACHE_TTL = 3600

SUMMER_THRESHOLDS = [
    (32.0, "중지", "stop"),
    (29.5, "제한", "restrict"),
    (26.5, "주의", "caution"),
]
WINTER_THRESHOLDS = [
    (-24.0, "중지", "stop"),
    (-18.0, "제한", "restrict"),
    (-10.0, "주의", "caution"),
]
