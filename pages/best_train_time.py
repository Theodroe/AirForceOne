from __future__ import annotations

import os
import sys
from datetime import datetime, timedelta

import pandas as pd
import streamlit as st
from streamlit_folium import st_folium

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from services import init_session
from ui import render_sidebar_ui, render_streamlit_base_style
from utils.best_train.config import ALL_HOURS, SUMMER_MONTHS
from utils.best_train.forecast_pipeline import run_collection_pipeline
from utils.best_train.training_logic import build_today_vals, get_status
from utils.best_train.weather_api import get_weather_data
from utils.realtime.charts import build_altair_chart, build_weather_map
from utils.realtime.loaders import (
    REGIONS,
    SPECIAL_AVAILABLE,
    SPECIAL_ERROR,
    build_area_df,
    build_detail_df,
    build_impact_df,
    build_summary_df,
    build_timeline_df,
    filter_timeline_by_region,
    get_region_worst_alert,
    load_special_report,
    save_special_report,
)
from utils.realtime.utils import DAY_LABELS, REGION_COORDS, apply_alert_to_status, restricted_range_str
from utils.time_utils import fmt_hms, now_kst


st.set_page_config(
    page_title="W-BOSS · 실시간 현황 대시보드",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

METRIC_OPTIONS = ["기온", "풍속", "습도", "강수량", "체감온도", "온도지수"]

init_session()
render_streamlit_base_style()
render_sidebar_ui("best_train_time")

if "region" not in st.session_state:
    st.session_state.region = REGIONS[0]
if "chart_metric" not in st.session_state:
    st.session_state.chart_metric = "기온"


with st.spinner("🌐 기상청 API에서 예보 데이터 수집 중..."):
    weather_df = get_weather_data()

if weather_df is None or weather_df.empty:
    st.error("⛔ 기상 데이터를 불러오지 못했습니다. API 키나 네트워크를 확인하세요.")
    if "api_errors" in st.session_state:
        for err in st.session_state["api_errors"]:
            st.warning(err)
    st.stop()

now = now_kst()
dates = sorted(weather_df["날짜"].unique().tolist())
month = int(dates[0].split("/")[0]) if dates else now.month
is_summer = month in SUMMER_MONTHS
target_col = "온도지수" if is_summer else "체감온도"
use_hr = f"{now.hour:02d}"

today_str = now.strftime("%Y%m%d")
base_date = weather_df.attrs.get("base_date", "")
base_time = weather_df.attrs.get("base_time", "2300")
target_dates = [(now + timedelta(days=i)).strftime("%Y%m%d") for i in range(3)]

if st.session_state.get("pipeline_saved_for") != today_str:
    try:
        run_collection_pipeline(
            weather_df=weather_df,
            base_date=base_date,
            base_time=base_time,
            target_dates=target_dates,
        )
        st.session_state["pipeline_saved_for"] = today_str
    except Exception as exc:
        st.warning(f"⚠️ 단기예보 데이터 저장 실패: {exc}")

enriched_df = pd.DataFrame()
active_df = pd.DataFrame()
alert_stats: dict[str, int] = {}

if SPECIAL_AVAILABLE:
    with st.spinner("📡 특보 데이터 수집 중..."):
        enriched_df, active_df, alert_stats = load_special_report()
    if not enriched_df.empty:
        save_special_report(enriched_df)
else:
    st.sidebar.warning(f"특보 모듈 로드 실패: {SPECIAL_ERROR}")


title_col, region_col, clock_col = st.columns([2, 5, 2])

with title_col:
    st.markdown("### 🌐 W-BOSS")
    st.caption("실시간 현황 대시보드")

with region_col:
    region = st.session_state.region
    try:
        base_dt = datetime.strptime(base_date + base_time[:2], "%Y%m%d%H")
        forecast_label = base_dt.strftime("%Y년 %m월 %d일 %H시 기준")
    except Exception:
        forecast_label = f"{base_date} {base_time}"

    st.write(f"● 현재 선택 지역: **{region}**　　● 예보 기준: **{forecast_label}**")
    btn_cols = st.columns(len(REGIONS))
    for idx, region_name in enumerate(REGIONS):
        with btn_cols[idx]:
            btn_type = "primary" if region_name == region else "secondary"
            if st.button(region_name, key=f"region_btn_{region_name}", width="stretch", type=btn_type):
                st.session_state.region = region_name
                st.rerun()


@st.fragment(run_every=1)
def live_clock() -> None:
    st.caption("현재 시각")
    st.write(f"#### {fmt_hms()}")


with clock_col:
    with st.container():
        _, right_col = st.columns([1, 1])
        with right_col:
            live_clock()

if SPECIAL_AVAILABLE and not active_df.empty:
    region_banner_df = filter_timeline_by_region(active_df, region)
    if not region_banner_df.empty:
        warning_cnt = int((region_banner_df["LVL"] == "3").sum()) if "LVL" in region_banner_df.columns else 0
        advisory_cnt = int((region_banner_df["LVL"] == "2").sum()) if "LVL" in region_banner_df.columns else 0
        st.warning(f"⚠️ [{region}] 발효중인 특보 — 경보 {warning_cnt}건 / 주의보 {advisory_cnt}건")

st.divider()

date_tab_labels = [
    f"{date_value} ({DAY_LABELS[idx]})" if idx < len(DAY_LABELS) else date_value
    for idx, date_value in enumerate(dates[:3])
]

rdf_today = weather_df[(weather_df["지역"] == region) & (weather_df["날짜"] == dates[0])]
avail_hrs = rdf_today["시간"].tolist()
cur_hr = use_hr if use_hr in avail_hrs else (avail_hrs[0] if avail_hrs else "06")
cur_row = rdf_today[rdf_today["시간"] == cur_hr]

region_active_df = filter_timeline_by_region(active_df, region) if SPECIAL_AVAILABLE else pd.DataFrame()

alert_map = (
    {region_name: get_region_worst_alert(region_name, active_df) for region_name in REGIONS}
    if SPECIAL_AVAILABLE and not active_df.empty
    else {region_name: (None, None) for region_name in REGIONS}
)
sel_alert_level, sel_alert_type = alert_map.get(region, (None, None))

map_rows: list[dict[str, object]] = []
for region_name in REGIONS:
    lat, lng = REGION_COORDS[region_name]
    sub = weather_df[
        (weather_df["지역"] == region_name)
        & (weather_df["날짜"] == dates[0])
        & (weather_df["시간"] == cur_hr)
    ]
    alert_level, _alert_type = alert_map.get(region_name, (None, None))

    if sub.empty or target_col not in sub.columns or not pd.notna(sub.iloc[0][target_col]):
        base_status = "데이터없음"
        val = None
        tmp_v = None
        wsd_v = None
        pcp_v = None
        reh_v = None
    else:
        row0 = sub.iloc[0]
        val = float(row0[target_col])
        base_status, _ = get_status(val, month)
        tmp_v = float(row0["기온"]) if pd.notna(row0.get("기온")) else None
        wsd_v = float(row0["풍속"]) if pd.notna(row0.get("풍속")) else None
        pcp_v = float(row0["강수량"]) if pd.notna(row0.get("강수량")) else None
        reh_v = float(row0["습도"]) if pd.notna(row0.get("습도")) else None

    map_rows.append(
        {
            "지역": region_name,
            "lat": lat,
            "lng": lng,
            "status": apply_alert_to_status(base_status, alert_level),
            "value": val,
            "기온": tmp_v,
            "풍속": wsd_v,
            "강수량": pcp_v,
            "습도": reh_v,
        }
    )

map_df = pd.DataFrame(map_rows)

col_map_top, col_live_top = st.columns([1, 1.13], gap="medium")

with col_map_top:
    with st.container(border=True):
        st.subheader("작전지역 기상현황 지도")

        danger_regions = map_df[map_df["status"].isin(["주의", "제한", "중지"])]["지역"].tolist()
        if danger_regions:
            st.warning(f"⚠️ 제한/중지 지역: **{', '.join(danger_regions)}**")
        else:
            st.success("✅ 전 지역 기상 제한요소 없음")

        st_folium(
            build_weather_map(map_df, target_col),
            use_container_width=True,
            height=527,
            returned_objects=[],
        )
        st.caption("🟢 가능　🟡 주의　🟠 제한　🔴 중지")

with col_live_top:
    with st.container(border=True):
        st.subheader(f"실시간 기상 영향 — {region}")

        if not cur_row.empty:
            r_row = cur_row.iloc[0]
            m1, m2, m3, m4, m5 = st.columns(5)
            m1.metric("기온", f"{r_row['기온']:.1f} ℃")
            m2.metric("체감온도", f"{r_row['체감온도']:.1f} ℃")
            m3.metric("풍속", f"{r_row['풍속']:.1f} m/s")
            m4.metric("강수량", f"{r_row['강수량']:.1f} mm")
            m5.metric("습도", f"{r_row['습도']:.0f} %")

            pivot = rdf_today.pivot(index="날짜", columns="시간", values=target_col)
            today_vals = build_today_vals(pivot, dates[0], month)
            restricted_str = restricted_range_str(today_vals)
            if restricted_str:
                st.markdown(f"#### ⚠️ 훈련 제한 시간대 ({target_col} 기준)　　**{restricted_str}**")
            else:
                st.markdown("#### ✅ 우리부대 훈련 제한 시간대가 없습니다")
        else:
            st.warning("현재 시간대 데이터가 없습니다.")

        st.divider()
        st.markdown(f"#### 우리부대 작전/훈련 — {region}")
        st.dataframe(
            build_summary_df(
                weather_df,
                region,
                dates,
                month,
                target_col,
                alert_level=sel_alert_level,
                alert_type=sel_alert_type,
            ),
            width="stretch",
        )
        st.caption("🟢 가능　🟡 주의　🟠 제한　🔴 중지")

        st.divider()
        st.markdown(f"#### 발령중인 특보 — {region}")
        if not SPECIAL_AVAILABLE:
            st.warning("특보 모듈을 불러오지 못했습니다.")
        elif region_active_df.empty:
            st.success(f"{region} 지역에 발효 중인 특보가 없습니다.")
        else:
            a1, a2, a3 = st.columns(3)
            a1.metric("특보 건수", len(region_active_df))
            a2.metric("경보", int((region_active_df["LVL"] == "3").sum()))
            a3.metric("주의보", int((region_active_df["LVL"] == "2").sum()))
            st.dataframe(build_timeline_df(region_active_df), width="stretch", hide_index=True)

with st.container(border=True):
    st.subheader("인접부대 기상 영향")
    col_area, col_impact = st.columns(2, gap="medium")

    with col_area:
        hdr_col, ctrl_col = st.columns([3, 1.4])
        with hdr_col:
            st.markdown("#### 작전/훈련 타임라인")
        with ctrl_col:
            st.write("")
            area_date_sel = st.selectbox(
                "날짜 선택",
                options=date_tab_labels,
                index=0,
                label_visibility="collapsed",
                key="area_date_sel",
            )
        area_date_idx = date_tab_labels.index(area_date_sel)
        area_date = dates[area_date_idx]
        area_next_date = dates[area_date_idx + 1] if area_date_idx + 1 < len(dates) else None
        area_alert = alert_map if area_date == dates[0] else {}
        st.dataframe(
            build_area_df(weather_df, area_date, area_next_date, month, target_col, area_alert),
            width="stretch",
        )
        st.caption("🟢 가능 🟡 주의 🟠 제한 🔴 중지")

    with col_impact:
        st.markdown("#### 특보 영향")
        st.write("")
        if not SPECIAL_AVAILABLE:
            st.warning("특보 모듈을 불러오지 못했습니다.")
        else:
            st.dataframe(build_impact_df(active_df), width="stretch")
            st.caption("경보 / 주의보 / 예비 / - (해당없음)  |  대상: 연천·철원·양구·화천·고성")

with st.container(border=True):
    st.subheader(f"상세 기상 영향 — {region}")
    col_chart, col_detail = st.columns(2, gap="medium")

    with col_chart:
        hdr_c, sel_c = st.columns([3, 1.4])
        with hdr_c:
            st.markdown("#### 기상요소 추이")
        with sel_c:
            st.write("")
            chart_date_sel = st.selectbox(
                "날짜 선택",
                options=date_tab_labels,
                index=0,
                label_visibility="collapsed",
                key="chart_date_sel",
            )
        chart_date = dates[date_tab_labels.index(chart_date_sel)]
        chart_metric = st.radio(
            "지표 선택",
            options=METRIC_OPTIONS,
            index=METRIC_OPTIONS.index(st.session_state.chart_metric),
            horizontal=True,
            label_visibility="collapsed",
            key="chart_metric_radio",
        )
        st.session_state.chart_metric = chart_metric

        chart_rows: list[dict[str, float | str]] = []
        for hr in ALL_HOURS:
            sub = weather_df[
                (weather_df["지역"] == region)
                & (weather_df["날짜"] == chart_date)
                & (weather_df["시간"] == hr)
            ]
            if not sub.empty and chart_metric in sub.columns:
                chart_rows.append({"시간": f"{int(hr):02d}시", chart_metric: float(sub.iloc[0][chart_metric])})

        if chart_rows:
            st.altair_chart(build_altair_chart(pd.DataFrame(chart_rows), chart_metric), width="stretch")
        else:
            st.info("차트 데이터가 없습니다.")

    with col_detail:
        st.markdown("#### 시간대별 상세 기상")
        st.write("")
        st.dataframe(build_detail_df(weather_df, region, dates[0]), width="stretch")
