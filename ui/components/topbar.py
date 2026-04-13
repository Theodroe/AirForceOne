import html
import textwrap

import streamlit as st

from .topbar_config import TOPBAR_ITEMS, BRAND_ICON, BRAND_NAME
from .topbar_styles import get_topbar_css
from .topbar_user import get_topbar_user_summary


def _target_for_href(href: str) -> str:
    mapping = {
        "/": "app.py",
        "/best_train_time": "pages/best_train_time.py",
        "/heatmap": "pages/heatmap.py",
        "/my_page": "pages/my_page.py",
    }
    return mapping.get(href, "app.py")


def render_topbar(current_key: str) -> None:
    st.markdown(get_topbar_css(), unsafe_allow_html=True)
    st.markdown('<div class="wb-topbar-shell">', unsafe_allow_html=True)

    left_col, center_col, right_col = st.columns([1.8, 5.6, 2.6], gap="medium")

    with left_col:
        st.markdown(
            textwrap.dedent(f'''
            <div class="wb-topbar-brand">
                <span class="wb-topbar-brand-mark">{html.escape(BRAND_ICON)}</span>
                <span>{html.escape(BRAND_NAME)}</span>
            </div>
            '''),
            unsafe_allow_html=True,
        )

    with center_col:
        st.markdown('<div class="wb-topbar-nav-slot">', unsafe_allow_html=True)
        nav_cols = st.columns(len(TOPBAR_ITEMS) * 2 - 1, gap="small")
        idx = 0
        for i, (label, href, key) in enumerate(TOPBAR_ITEMS):
            with nav_cols[idx]:
                if key == current_key:
                    st.button(
                        label,
                        key=f"topbar_current_{key}",
                        disabled=True,
                        use_container_width=True,
                    )
                else:
                    if st.button(
                        label,
                        key=f"topbar_go_{key}",
                        use_container_width=True,
                    ):
                        st.switch_page(_target_for_href(href))
            idx += 1
            if i < len(TOPBAR_ITEMS) - 1:
                with nav_cols[idx]:
                    st.markdown('<div class="wb-topbar-sep">|</div>', unsafe_allow_html=True)
                idx += 1
        st.markdown('</div>', unsafe_allow_html=True)

    with right_col:
        summary = html.escape(get_topbar_user_summary())
        st.markdown(
            textwrap.dedent(f'''
            <div class="wb-topbar-user">
                <div class="wb-topbar-user-chip">
                    <span class="wb-topbar-user-dot"></span>
                    <span>{summary}</span>
                </div>
            </div>
            '''),
            unsafe_allow_html=True,
        )

    st.markdown('</div>', unsafe_allow_html=True)
