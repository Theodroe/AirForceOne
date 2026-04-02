from __future__ import annotations

import os
import sys

import streamlit as st

from services import init_session, is_authenticated
from ui import render_login_page, render_sidebar_ui, render_streamlit_base_style

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from utils.heatmap.bar_graph_function_sp import CSV_PATH, load_data
from utils.heatmap.config import LOCATION_MAPPING, EXCLUDED_SPLOCS
from utils.heatmap.ui_components import (
    init_session_state,
    render_header,
    render_filter_bar,
    render_yearly_stats,
    render_heatmap,
    render_schedule_panel,
    render_monthly_table,
    render_daily_detail,
)

st.set_page_config(
    page_title="연간 훈련가용 판정 현황",
    page_icon="🌡️",
    layout="wide",
    initial_sidebar_state="expanded",
)
render_streamlit_base_style()
init_session()
render_sidebar_ui("연간 훈련가용 판정 현황" if is_authenticated() else None)

if is_authenticated():
    df = load_data(CSV_PATH)
    splocs = sorted([s for s in df["sploc"].unique() if s not in EXCLUDED_SPLOCS])
    init_session_state()
    render_header()
    render_filter_bar(splocs)
    st.write("")
    disp_name = LOCATION_MAPPING.get(st.session_state.sel_sploc, st.session_state.sel_sploc)

    col_stat, col_heatmap, col_schedule = st.columns([3.3, 7.5, 3.4])
    with col_stat:
        m_normal, m_total = render_yearly_stats(df)
    with col_heatmap:
        render_heatmap(df, disp_name)
    with col_schedule:
        render_schedule_panel(df)

    st.write("")
    col_monthly, col_detail = st.columns([2, 3])
    with col_monthly:
        render_monthly_table(m_normal, m_total)
    with col_detail:
        render_daily_detail(df)
else:
    render_login_page()
