from __future__ import annotations

import html

import pandas as pd
import streamlit as st

from services import (
    change_password,
    delete_user,
    get_all_access_logs,
    get_all_audit_logs,
    get_current_user,
    get_my_access_logs,
    get_my_audit_logs,
    get_user_fresh,
    update_rank,
)
from ui.table_views import render_access_logs_table, render_audit_logs_table

RANK_OPTIONS = [
    "미설정", "이병", "일병", "상병", "병장",
    "하사", "중사", "상사", "원사",
    "소위", "중위", "대위", "소령", "중령", "대령",
]


def _safe(value: object) -> str:
    return html.escape(str(value if value not in (None, "") else "-"))


def _info_item(label: str, value: object) -> str:
    return f"""
    <div class="wb-info-item">
        <div class="wb-info-label">{html.escape(label)}</div>
        <div class="wb-info-value">{_safe(value)}</div>
    </div>
    """


def render_mypage_dashboard() -> None:
    user = get_current_user() or {}
    if user.get("service_number"):
        fresh = get_user_fresh(user["service_number"])
        if fresh:
            fresh.pop("password", None)
            st.session_state["user"] = {k: v for k, v in fresh.items() if k != "password"}
            user = st.session_state["user"]

    st.markdown(
        """
        <div class="hero-card">
            <div class="page-eyebrow">OPERATOR PROFILE</div>
            <div class="page-title" style="font-size:1.9rem;">마이페이지</div>
            <div class="page-subtitle">기본 정보, 계급, 비밀번호, 접속 로그를 한 곳에서 관리합니다.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not user:
        st.info("로그인이 필요합니다.")
        return

    left, right = st.columns([1.2, 0.8], gap="large")

    with left:
        st.markdown('<div class="section-title">기본 정보</div>', unsafe_allow_html=True)
        info_html = "".join(
            [
                _info_item("이름", user.get("username")),
                _info_item("군번", user.get("service_number")),
                _info_item("부대", user.get("unit_id")),
                _info_item("권한", user.get("role")),
                _info_item("계급", user.get("military_rank") or "미설정"),
            ]
        )
        st.markdown(
            f'<div class="wb-panel wb-info-panel"><div class="wb-info-grid">{info_html}</div></div>',
            unsafe_allow_html=True,
        )

    with right:
        st.markdown('<div class="section-title">계급 변경</div>', unsafe_allow_html=True)
        current_rank = user.get("military_rank") or "미설정"
        idx = RANK_OPTIONS.index(current_rank) if current_rank in RANK_OPTIONS else 0

        with st.container():
            st.markdown('<div class="wb-panel wb-action-panel">', unsafe_allow_html=True)
            with st.form("rank_update_form", clear_on_submit=False):
                new_rank = st.selectbox("계급", RANK_OPTIONS, index=idx)
                rank_submit = st.form_submit_button("계급 저장", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        if rank_submit:
            ok, msg = update_rank(user["service_number"], None if new_rank == "미설정" else new_rank)
            (st.success if ok else st.error)(msg)
            if ok:
                st.switch_page("pages/my_page.py")

    st.markdown('<div class="section-title" style="margin-top:1rem;">비밀번호 변경</div>', unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="wb-panel wb-action-panel">', unsafe_allow_html=True)
        with st.form("change_password_form", clear_on_submit=True):
            p1, p2 = st.columns(2, gap="large")
            with p1:
                cur = st.text_input("현재 비밀번호", type="password")
            with p2:
                new = st.text_input("새 비밀번호", type="password")
            pw_submit = st.form_submit_button("비밀번호 변경", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    if pw_submit:
        ok, msg = change_password(user["service_number"], cur, new)
        (st.success if ok else st.error)(msg)

    st.markdown('<div class="section-title" style="margin-top:1rem;">계정 관리</div>', unsafe_allow_html=True)
    with st.expander("탈퇴하기", expanded=False):
        with st.container():
            st.markdown('<div class="wb-panel wb-action-panel">', unsafe_allow_html=True)
            with st.form("delete_account_form", clear_on_submit=True):
                st.caption("탈퇴는 마이페이지에서만 가능합니다. 처리 후 즉시 로그아웃됩니다.")
                delete_pw = st.text_input("탈퇴 확인용 비밀번호", type="password")
                delete_submit = st.form_submit_button("탈퇴하기", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        if delete_submit:
            ok, msg = delete_user(user["service_number"], delete_pw)
            (st.success if ok else st.error)(msg)
            if ok:
                st.switch_page("app.py")

    labels = ["내 접속 기록", "내 감사 로그"]
    if user.get("role") in {"admin", "officer"}:
        labels += ["전체 접속 로그", "전체 감사 로그"]

    st.markdown('<div class="section-title" style="margin-top:1rem;">기록 조회</div>', unsafe_allow_html=True)
    tabs = st.tabs(labels)
    with tabs[0]:
        render_access_logs_table(pd.DataFrame(get_my_access_logs()))
    with tabs[1]:
        render_audit_logs_table(pd.DataFrame(get_my_audit_logs()))
    if len(labels) > 2:
        with tabs[2]:
            render_access_logs_table(pd.DataFrame(get_all_access_logs()))
        with tabs[3]:
            render_audit_logs_table(pd.DataFrame(get_all_audit_logs()))
