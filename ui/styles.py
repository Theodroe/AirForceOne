from __future__ import annotations

import streamlit as st


def render_streamlit_base_style() -> None:
    css = """
    <style>
    :root {
        --wb-radius: 20px;
        --wb-radius-sm: 14px;
        --wb-border: rgba(120, 130, 150, 0.18);
        --wb-shadow: 0 14px 30px rgba(15, 23, 42, 0.10);
        --wb-text-muted: rgba(31, 41, 55, 0.72);

        /* 눈에 보이는 색 */
        --wb-blue: #dbeafe;
        --wb-indigo: #e0e7ff;
        --wb-purple: #f3e8ff;
        --wb-cyan: #cffafe;
        --wb-rose: #ffe4e6;
        --wb-amber: #fef3c7;
        --wb-green: #dcfce7;

        --wb-blue-border: #93c5fd;
        --wb-purple-border: #c4b5fd;
        --wb-cyan-border: #67e8f9;
        --wb-amber-border: #fcd34d;
        --wb-green-border: #86efac;
        --wb-rose-border: #fda4af;
    }

    @media (prefers-color-scheme: dark) {
        :root {
            --wb-border: rgba(255, 255, 255, 0.10);
            --wb-shadow: 0 16px 34px rgba(0, 0, 0, 0.34);
            --wb-text-muted: rgba(255, 255, 255, 0.76);

            /* 다크모드용 보이는 색 */
            --wb-blue: rgba(59, 130, 246, 0.22);
            --wb-indigo: rgba(99, 102, 241, 0.22);
            --wb-purple: rgba(168, 85, 247, 0.20);
            --wb-cyan: rgba(34, 211, 238, 0.18);
            --wb-rose: rgba(244, 63, 94, 0.18);
            --wb-amber: rgba(245, 158, 11, 0.20);
            --wb-green: rgba(34, 197, 94, 0.18);

            --wb-blue-border: rgba(96, 165, 250, 0.40);
            --wb-purple-border: rgba(196, 181, 253, 0.38);
            --wb-cyan-border: rgba(103, 232, 249, 0.34);
            --wb-amber-border: rgba(252, 211, 77, 0.36);
            --wb-green-border: rgba(134, 239, 172, 0.34);
            --wb-rose-border: rgba(253, 164, 175, 0.34);
        }
    }

    [data-testid="stSidebarNav"] {
        display: none;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    .stApp {
        background: var(--background-color);
        color: var(--text-color);
    }

    section[data-testid="stSidebar"] {
        background: var(--secondary-background-color);
        border-right: 1px solid var(--wb-border);
    }

    section[data-testid="stSidebar"] * {
        color: var(--text-color);
    }

    .block-container {
        max-width: none;
        padding-top: .85rem;
        padding-bottom: 1rem;
        padding-left: .75rem;
        padding-right: .75rem;
    }

    .hero-card,
    .wb-panel,
    .wb-module-card,
    .wb-brief-card,
    .wb-stat-card,
    .wb-operator-box {
        border-radius: 22px;
        box-shadow: var(--wb-shadow);
        border: 1px solid var(--wb-border);
        overflow: hidden;
    }

    .hero-card {
        padding: 1.45rem 1.6rem;
        margin-bottom: 1.05rem;
        background:
            radial-gradient(circle at top right, var(--wb-cyan) 0, transparent 28%),
            radial-gradient(circle at left bottom, var(--wb-purple) 0, transparent 28%),
            var(--secondary-background-color);
    }

    .wb-panel,
    .wb-module-card,
    .wb-brief-card,
    .wb-stat-card,
    .wb-operator-box {
        padding: 1rem 1.05rem;
        background: var(--secondary-background-color);
    }

    .page-eyebrow {
        color: var(--primary-color);
        font-size: .84rem;
        font-weight: 700;
        letter-spacing: .08em;
        text-transform: uppercase;
        margin-bottom: .45rem;
    }

    .page-title {
        font-size: 2.05rem;
        line-height: 1.08;
        font-weight: 700;
        margin: 0 0 .35rem 0;
        color: var(--text-color);
    }

    .page-subtitle {
        color: var(--wb-text-muted);
        font-size: 1rem;
        margin: 0;
    }

    .section-title {
        font-size: 1rem;
        font-weight: 700;
        margin-bottom: .8rem;
        color: var(--text-color);
    }

    .wb-hero-chip-wrap {
        display: flex;
        gap: .55rem;
        flex-wrap: wrap;
        align-items: center;
    }

    .wb-hero-chip {
        background: var(--wb-indigo);
        border: 1px solid var(--wb-blue-border);
        color: var(--text-color);
        border-radius: 999px;
        padding: .52rem .86rem;
        font-size: .88rem;
        font-weight: 600;
    }

    .wb-stat-card {
        min-height: 98px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        gap: .22rem;
    }

    /* 카드 4개 각각 눈에 보이게 색 */
    .wb-stat-card:nth-of-type(1) {
        background: linear-gradient(135deg, var(--wb-blue), var(--secondary-background-color) 72%);
        border-color: var(--wb-blue-border);
    }
    .wb-stat-card:nth-of-type(2) {
        background: linear-gradient(135deg, var(--wb-cyan), var(--secondary-background-color) 72%);
        border-color: var(--wb-cyan-border);
    }
    .wb-stat-card:nth-of-type(3) {
        background: linear-gradient(135deg, var(--wb-amber), var(--secondary-background-color) 72%);
        border-color: var(--wb-amber-border);
    }
    .wb-stat-card:nth-of-type(4) {
        background: linear-gradient(135deg, var(--wb-purple), var(--secondary-background-color) 72%);
        border-color: var(--wb-purple-border);
    }

    .wb-stat-label {
        font-size: .92rem;
        font-weight: 600;
        color: var(--wb-text-muted);
        margin-bottom: .18rem;
    }

    .wb-stat-value {
        font-size: 1.55rem;
        line-height: 1.1;
        font-weight: 700;
        color: var(--text-color);
    }

    .wb-module-card {
        min-height: 220px;
    }

    .wb-module-card-strong:nth-of-type(1) {
        background:
            radial-gradient(circle at right bottom, var(--wb-cyan) 0, transparent 24%),
            linear-gradient(135deg, var(--wb-blue), var(--secondary-background-color) 68%);
        border-color: var(--wb-blue-border);
    }

    .wb-module-card-strong:nth-of-type(2) {
        background:
            radial-gradient(circle at right bottom, var(--wb-purple) 0, transparent 24%),
            linear-gradient(135deg, var(--wb-rose), var(--secondary-background-color) 68%);
        border-color: var(--wb-purple-border);
    }

    .wb-module-head {
        display: flex;
        gap: .9rem;
        align-items: flex-start;
        margin-bottom: 1rem;
    }

    .wb-module-icon {
        width: 50px;
        height: 50px;
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.35rem;
        flex-shrink: 0;
        background: rgba(255,255,255,0.45);
        backdrop-filter: blur(8px);
    }

    @media (prefers-color-scheme: dark) {
        .wb-module-icon {
            background: rgba(255,255,255,0.06);
        }
    }

    .wb-module-list {
        margin: 0;
        padding-left: 1.2rem;
        color: var(--text-color);
    }

    .wb-module-list li {
        margin-bottom: .35rem;
    }

    .wb-brief-card {
        min-height: 132px;
    }

    .wb-brief-card:nth-of-type(1) {
        background: linear-gradient(135deg, var(--wb-green), var(--secondary-background-color) 72%);
        border-color: var(--wb-green-border);
    }
    .wb-brief-card:nth-of-type(2) {
        background: linear-gradient(135deg, var(--wb-purple), var(--secondary-background-color) 72%);
        border-color: var(--wb-purple-border);
    }
    .wb-brief-card:nth-of-type(3) {
        background: linear-gradient(135deg, var(--wb-cyan), var(--secondary-background-color) 72%);
        border-color: var(--wb-cyan-border);
    }

    .wb-brief-label {
        font-size: .9rem;
        font-weight: 600;
        color: var(--wb-text-muted);
        margin-bottom: .4rem;
    }

    .wb-brief-value {
        font-size: 1.9rem;
        font-weight: 700;
        line-height: 1;
        color: var(--text-color);
        margin-bottom: .48rem;
    }

    .wb-brief-desc {
        font-size: .95rem;
        color: var(--wb-text-muted);
    }

    .wb-operator-top {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: .75rem;
        margin-bottom: .9rem;
    }

    .wb-operator-badge {
        background: var(--wb-indigo);
        border: 1px solid var(--wb-blue-border);
        border-radius: 999px;
        padding: .45rem .8rem;
        font-size: .85rem;
        font-weight: 600;
    }

    .wb-operator-state {
        font-size: .95rem;
        font-weight: 600;
    }

    .wb-operator-name {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: .35rem;
    }

    .wb-operator-meta {
        font-size: 1rem;
        margin-bottom: .9rem;
        color: var(--wb-text-muted);
    }

    .wb-operator-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: .8rem;
    }

    .wb-operator-chip {
        background: var(--background-color);
        border: 1px solid var(--wb-border);
        border-radius: 14px;
        padding: .9rem 1rem;
    }

    .wb-operator-chip span {
        display: block;
        font-size: .84rem;
        margin-bottom: .3rem;
        color: var(--wb-text-muted);
    }

    .wb-operator-chip strong {
        font-size: 1.02rem;
        color: var(--text-color);
        font-weight: 700;
    }

    .stButton > button,
    .stFormSubmitButton > button {
        width: 100%;
        min-height: 46px;
        font-size: 1rem;
        font-weight: 600;
        white-space: nowrap;
        border-radius: 14px !important;
        border: 1px solid var(--wb-border) !important;
        background: linear-gradient(135deg, var(--wb-indigo), var(--secondary-background-color)) !important;
        color: var(--text-color) !important;
        box-shadow: none !important;
    }

    .stButton > button:hover,
    .stFormSubmitButton > button:hover {
        border-color: var(--wb-blue-border) !important;
        background: linear-gradient(135deg, var(--wb-blue), var(--wb-cyan)) !important;
        color: var(--text-color) !important;
    }

    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a {
        border-radius: 14px;
    }

    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a:hover {
        background: linear-gradient(90deg, var(--wb-indigo), transparent);
    }

    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a[aria-current="page"] {
        background: linear-gradient(90deg, var(--wb-blue), var(--wb-purple));
        border: 1px solid var(--wb-blue-border);
    }

    .stTextInput input,
    .stNumberInput input,
    .stTextArea textarea,
    .stSelectbox [data-baseweb="select"] > div,
    .stMultiSelect [data-baseweb="select"] > div {
        background: var(--secondary-background-color) !important;
        color: var(--text-color) !important;
        border: 1px solid var(--wb-border) !important;
        border-radius: 14px !important;
        box-shadow: none !important;
    }

    [data-testid="stDataFrame"],
    [data-testid="stTable"],
    [data-testid="stPlotlyChart"] {
        border: 1px solid var(--wb-border);
        border-radius: 18px;
        overflow: hidden;
        background: var(--secondary-background-color);
    }

    [data-testid="collapsedControl"] {
        border-radius: 12px !important;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
