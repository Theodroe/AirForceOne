from __future__ import annotations

import html

import pandas as pd
import streamlit as st

from services import extract_active, fetch_reports, get_latest, load_data, summarize_alerts
from ui.alert_feed_panel import render_alert_feed_panel
from ui.summary_cards import render_summary_cards


def _module_card(title: str, subtitle: str, bullets: list[str], button_label: str, target: str, emoji: str, tone: str) -> None:
    bullet_html = "".join(f"<li>{html.escape(item)}</li>" for item in bullets)
    st.markdown(
        f"""
        <div class="wb-module-card wb-module-card-strong">
            <div class="wb-module-head">
                <div class="wb-module-icon" style="background:{tone};">{emoji}</div>
                <div>
                    <div class="section-title" style="margin-bottom:.2rem;">{html.escape(title)}</div>
                    <div class="page-subtitle">{html.escape(subtitle)}</div>
                </div>
            </div>
            <ul class="wb-module-list">{bullet_html}</ul>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button(button_label, key=f"open::{target}", use_container_width=True):
        st.switch_page(target)


def _brief_card(title: str, value: str, desc: str) -> None:
    st.markdown(
        f"""
        <div class="wb-brief-card">
            <div class="wb-brief-label">{html.escape(title)}</div>
            <div class="wb-brief-value">{html.escape(value)}</div>
            <div class="wb-brief-desc">{html.escape(desc)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_main_dashboard() -> None:
    st.markdown(
        """<div class="hero-card">
            <div style="display:flex;align-items:flex-start;justify-content:space-between;gap:20px;flex-wrap:wrap;">
                <div style="max-width:760px;">
                    <div class="page-eyebrow">MISSION CONTROL</div>
                    <div class="page-title" style="margin-bottom:.25rem;">메인 페이지</div>
                    <div class="page-subtitle">실시간 현황 대시보드와 연간 훈련가용 판정 현황으로 바로 진입해, 현재 운용 상황과 연간 패턴 분석을 한 흐름으로 확인하는 통합 화면입니다.</div>
                </div>
                <div class="wb-hero-chip-wrap">
                    <div class="wb-hero-chip">실시간 현황 대시보드</div>
                    <div class="wb-hero-chip">연간 훈련가용 판정 현황</div>
                    <div class="wb-hero-chip">weather operations</div>
                </div>
            </div>
        </div>""",
        unsafe_allow_html=True,
    )

    reports = fetch_reports()
    latest = get_latest(reports)
    active = extract_active(latest)
    alert_stats = summarize_alerts(active)
    heatmap_df = load_data()

    recent_year = int(heatmap_df["year"].max()) if not heatmap_df.empty else None
    recent_year_df = heatmap_df[heatmap_df["year"] == recent_year].copy() if recent_year is not None else pd.DataFrame()
    station_count = int(heatmap_df["sploc"].nunique()) if not heatmap_df.empty and "sploc" in heatmap_df.columns else 0
    avg_score = f"{recent_year_df['score'].mean():.2f}" if not recent_year_df.empty else "-"
    best_month = "-"
    if not recent_year_df.empty:
        month_scores = recent_year_df.groupby("month", as_index=False)["score"].mean().sort_values("score", ascending=False)
        if not month_scores.empty:
            best_month = f"{int(month_scores.iloc[0]['month'])}월"

    render_summary_cards(
        [
            ("발효 중 특보", len(active)),
            ("경보 / 주의보", f"{alert_stats['warning']} / {alert_stats['advisory']}"),
            ("관측 지역", station_count),
            ("최근 연도 평균 점수", avg_score),
        ]
    )

    st.markdown('<div class="section-title" style="margin-top:.9rem;">핵심 진입 화면</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2, gap="large")
    with c1:
        _module_card(
            "실시간 현황 대시보드",
            "단기예보 기준으로 지역별 훈련 가능 시간과 추천 시작 시각을 빠르게 확인합니다.",
            ["지역별 주간 가능 시간", "추천 시작 시각", "시간대별 기상 지표 테이블"],
            "실시간 현황 대시보드 열기",
            "pages/best_train_time.py",
            "🛡️",
            "linear-gradient(135deg, #2563eb 0%, #38bdf8 100%)",
        )
    with c2:
        _module_card(
            "연간 훈련가용 판정 현황",
            "연간 365일 분포와 특정 날짜 24시간 상세 비교를 한 화면에서 조회합니다.",
            ["연간 가용일수 종합", "연속 가용 구간 추천", "월별·일별 상세 조회"],
            "연간 훈련가용 판정 현황 열기",
            "pages/heatmap.py",
            "🌡️",
            "linear-gradient(135deg, #0f766e 0%, #22c55e 100%)",
        )

    st.markdown('<div class="section-title" style="margin-top:1rem;">운용 브리프</div>', unsafe_allow_html=True)
    b1, b2, b3 = st.columns(3, gap="large")
    with b1:
        _brief_card("권장 진입", "실시간 현황 대시보드", "단기예보 기반으로 즉시 훈련 가능 시간 확인")
    with b2:
        _brief_card("연간 분석", "연간 훈련가용 판정 현황", "365일 패턴과 일별 상세 비교")
    with b3:
        _brief_card("가장 양호한 월", best_month, "최근 연도 기준 평균 점수 상위 월")

    st.markdown('<div class="section-title" style="margin-top:1rem;">실시간 특보 피드</div>', unsafe_allow_html=True)
    render_alert_feed_panel(active)
