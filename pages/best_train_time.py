from __future__ import annotations

from collections import Counter
from datetime import datetime

import pandas as pd
import streamlit as st

from services import init_session, is_authenticated
from ui import render_login_page, render_sidebar_ui, render_streamlit_base_style
from utils.best_train.config import AREA_INFO, SERVICE_KEY
from utils.best_train.training_logic import get_status
from utils.best_train.weather_api import get_weather_data


def _status_chip(label: str) -> str:
    colors = {
        "가능": "#22c55e",
        "주의": "#f59e0b",
        "제한": "#ef4444",
        "중지": "#2563eb",
    }
    color = colors.get(label, "#64748b")
    return f'<span style="display:inline-block;padding:.28rem .62rem;border-radius:999px;background:{color};color:white;font-size:.76rem;font-weight:700;">{label}</span>'


def _prep_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    work = df.copy()
    work["month"] = work["날짜"].str.split("/").str[0].astype(int)
    work["판정"] = [get_status(v, m)[0] for v, m in zip(work["체감온도"], work["month"])]
    return work


def _render_overview(df: pd.DataFrame):
    latest_date = sorted(df["날짜"].unique())[0]
    day_df = df[df["날짜"] == latest_date].copy()
    severity = {"가능": 0, "주의": 1, "제한": 2, "중지": 3}
    summary = []
    for region in AREA_INFO.keys():
        rdf = day_df[(day_df["지역"] == region) & (day_df["시간"].astype(int).between(6, 17))].copy()
        counts = Counter(rdf["판정"].tolist())
        dominant = max(counts, key=lambda x: (counts[x], severity.get(x, -1))) if counts else "-"
        good_hours = int((rdf["판정"] == "가능").sum()) if not rdf.empty else 0
        if not rdf.empty:
            best_rows = rdf[rdf["판정"] == "가능"] if (rdf["판정"] == "가능").any() else rdf.sort_values("판정")
            best_row = best_rows.sort_values(["시간"]).iloc[0]
            best_time = f"{int(best_row['시간']):02d}:00"
        else:
            best_time = "-"
        summary.append({"지역": region, "대표 판정": dominant, "가능 시간": good_hours, "추천 시작": best_time})

    cards = st.columns(len(summary), gap="small")
    for col, row in zip(cards, summary):
        with col:
            st.markdown(
                f"""<div class="wb-panel" style="padding:1rem 1rem .9rem 1rem;min-height:150px;">
                    <div style="font-size:1.02rem;font-weight:800;margin-bottom:.45rem;">{row['지역']}</div>
                    <div style="margin-bottom:.55rem;">{_status_chip(row['대표 판정'])}</div>
                    <div style="color:var(--wb-muted);font-size:.88rem;">주간 가능 시간</div>
                    <div style="font-size:1.5rem;font-weight:800;">{row['가능 시간']}h</div>
                    <div style="margin-top:.3rem;color:var(--wb-muted);font-size:.86rem;">추천 시작 {row['추천 시작']}</div>
                </div>""",
                unsafe_allow_html=True,
            )


def _render_tables(df: pd.DataFrame):
    regions = list(AREA_INFO.keys())
    dates = sorted(df["날짜"].unique())
    c1, c2 = st.columns([1, 1])
    with c1:
        region = st.selectbox("지역", regions, index=0)
    with c2:
        date = st.selectbox("날짜", dates, index=0)

    filtered = df[(df["지역"] == region) & (df["날짜"] == date)].copy().sort_values("시간")
    display = filtered[["시간", "기온", "풍속", "습도", "강수량", "체감온도", "온도지수", "판정"]].copy()
    display["시간"] = display["시간"].astype(str).str.zfill(2) + ":00"
    st.markdown('<div class="section-title" style="margin-top:.35rem;">시간대별 상세</div>', unsafe_allow_html=True)
    st.dataframe(display, use_container_width=True, hide_index=True)

    line_df = filtered[["시간", "체감온도", "기온"]].copy()
    line_df["시간"] = line_df["시간"].astype(str).str.zfill(2) + ":00"
    line_df = line_df.set_index("시간")
    st.markdown('<div class="section-title" style="margin-top:.55rem;">체감온도 요약</div>', unsafe_allow_html=True)
    st.line_chart(line_df)


def render_best_train_page():
    st.markdown(
        """<div class="hero-card">
            <div style="display:flex;align-items:center;gap:14px;">
                <div style="width:56px;height:56px;border-radius:18px;background:linear-gradient(135deg,var(--wb-primary),#38bdf8);display:flex;align-items:center;justify-content:center;font-size:25px;color:white;">🛡️</div>
                <div>
                    <div class="page-title" style="font-size:2rem;margin-bottom:.16rem;">실시간 현황 대시보드</div>
                    <div class="page-subtitle">단기예보 기준으로 지역별 훈련 가능 시간, 추천 시작 시각, 시간대별 기상 지표를 확인합니다.</div>
                </div>
            </div>
        </div>""",
        unsafe_allow_html=True,
    )

    if not SERVICE_KEY:
        st.warning("SHORT_TERM_FORECAST_API_KEY 가 설정되지 않아 best train 실시간 예보를 불러올 수 없습니다.")
        return

    with st.spinner("단기예보 데이터를 불러오는 중입니다."):
        raw = get_weather_data()

    if raw.empty:
        st.error("불러온 예보 데이터가 없습니다.")
        return

    df = _prep_dataframe(raw)
    st.caption(f"기준 시각: {raw.attrs.get('base_date', '-')} {raw.attrs.get('base_time', '-')} · 조회 시각: {datetime.now():%Y-%m-%d %H:%M}")
    _render_overview(df)
    _render_tables(df)


st.set_page_config(page_title="실시간 현황 대시보드", page_icon="🛡️", layout="wide")
render_streamlit_base_style()
init_session()
render_sidebar_ui("best_train_time" if is_authenticated() else None)

if is_authenticated():
    render_best_train_page()
else:
    render_login_page()
