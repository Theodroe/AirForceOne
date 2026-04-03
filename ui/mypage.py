from __future__ import annotations

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


def _info_card(label: str, value: object, variant: str) -> None:
    safe_value = value if value not in (None, "") else "-"
    st.markdown(f'<div class="wb-info-box {variant}">', unsafe_allow_html=True)
    st.markdown(f'<div class="wb-info-kicker">{label}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="wb-info-main">{safe_value}</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


def _section_header(title: str, subtitle: str | None = None) -> None:
    if subtitle:
        st.markdown(
            f'''
            <div class="wb-section-head">
                <div class="section-title" style="margin-bottom:.2rem;">{title}</div>
                <div class="wb-section-subtitle">{subtitle}</div>
            </div>
            ''',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)


def render_mypage_dashboard() -> None:
    user = get_current_user() or {}
    if user.get("service_number"):
        fresh = get_user_fresh(user["service_number"])
        if fresh:
            fresh.pop("password", None)
            st.session_state["user"] = {k: v for k, v in fresh.items() if k != "password"}
            user = st.session_state["user"]

    st.markdown(
        '''
        <div class="hero-card wb-mypage-hero">
            <div class="page-eyebrow">OPERATOR PROFILE</div>
            <div class="page-title" style="font-size:1.95rem;">마이페이지</div>
            <div class="page-subtitle">기본 정보, 계급, 비밀번호, 접속 로그를 한 곳에서 관리합니다.</div>
        </div>
        ''',
        unsafe_allow_html=True,
    )

    if not user:
        st.info("로그인이 필요합니다.")
        return

    left, right = st.columns([1.28, 0.72], gap="large")

    with left:
        _section_header("기본 정보", "운용자 프로필과 권한 정보를 한눈에 확인합니다.")
        st.markdown('<div class="wb-panel wb-info-panel">', unsafe_allow_html=True)

        r1c1, r1c2 = st.columns(2, gap="medium")
        with r1c1:
            _info_card("이름", user.get("username"), "blue")
        with r1c2:
            _info_card("군번", user.get("service_number"), "purple")

        r2c1, r2c2 = st.columns(2, gap="medium")
        with r2c1:
            _info_card("부대", user.get("unit_id"), "cyan")
        with r2c2:
            _info_card("권한", user.get("role"), "amber")

        r3c1, r3c2 = st.columns(2, gap="medium")
        with r3c1:
            _info_card("계급", user.get("military_rank") or "미설정", "green")
        with r3c2:
            st.markdown(
                '''
                <div class="wb-info-box wb-info-summary">
                    <div class="wb-info-kicker">상태</div>
                    <div class="wb-info-main">정상</div>
                    <div class="wb-info-note">계정 정보가 최신 상태로 동기화되었습니다.</div>
                </div>
                ''',
                unsafe_allow_html=True,
            )

        st.markdown("</div>", unsafe_allow_html=True)

    with right:
        _section_header("빠른 설정", "마이페이지에서 자주 쓰는 작업")
        st.markdown('<div class="wb-panel wb-action-panel wb-stack-panel">', unsafe_allow_html=True)

        current_rank = user.get("military_rank") or "미설정"
        idx = RANK_OPTIONS.index(current_rank) if current_rank in RANK_OPTIONS else 0

        st.markdown('<div class="wb-mini-head">계급 변경</div>', unsafe_allow_html=True)
        with st.form("rank_update_form", clear_on_submit=False):
            new_rank = st.selectbox("계급", RANK_OPTIONS, index=idx)
            rank_submit = st.form_submit_button("계급 저장", use_container_width=True)

        st.markdown('<div class="wb-divider"></div>', unsafe_allow_html=True)

        st.markdown('<div class="wb-mini-head">비밀번호 변경</div>', unsafe_allow_html=True)
        with st.form("change_password_form", clear_on_submit=True):
            cur = st.text_input("현재 비밀번호", type="password")
            new = st.text_input("새 비밀번호", type="password")
            pw_submit = st.form_submit_button("비밀번호 변경", use_container_width=True)

        st.markdown('<div class="wb-divider"></div>', unsafe_allow_html=True)

        with st.expander("계정 관리", expanded=False):
            st.markdown('<div class="wb-danger-note">탈퇴는 마이페이지에서만 가능합니다. 처리 후 즉시 로그아웃됩니다.</div>', unsafe_allow_html=True)
            with st.form("delete_account_form", clear_on_submit=True):
                delete_pw = st.text_input("탈퇴 확인용 비밀번호", type="password")
                delete_submit = st.form_submit_button("탈퇴하기", use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

        if rank_submit:
            ok, msg = update_rank(user["service_number"], None if new_rank == "미설정" else new_rank)
            (st.success if ok else st.error)(msg)
            if ok:
                st.switch_page("pages/my_page.py")

        if pw_submit:
            ok, msg = change_password(user["service_number"], cur, new)
            (st.success if ok else st.error)(msg)

        if 'delete_submit' in locals() and delete_submit:
            ok, msg = delete_user(user["service_number"], delete_pw)
            (st.success if ok else st.error)(msg)
            if ok:
                st.switch_page("app.py")

    labels = ["내 접속 기록", "내 감사 로그"]
    if user.get("role") in {"admin", "officer"}:
        labels += ["전체 접속 로그", "전체 감사 로그"]

    _section_header("기록 조회", "접속 및 감사 로그를 탭별로 확인합니다.")
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
