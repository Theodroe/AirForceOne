from __future__ import annotations

import streamlit as st


def render_streamlit_base_style() -> None:
    css = """
    <style>
    :root {
        --wb-border: rgba(120, 130, 150, 0.18);
        --wb-shadow: 0 9px 20px rgba(15, 23, 42, 0.07);

        --wb-blue: #dbeafe;
        --wb-cyan: #cffafe;
        --wb-purple: #f3e8ff;
        --wb-amber: #fef3c7;
        --wb-green: #dcfce7;
        --wb-rose: #ffe4e6;

        --wb-blue-border: #93c5fd;
        --wb-cyan-border: #67e8f9;
        --wb-purple-border: #c4b5fd;
        --wb-amber-border: #fcd34d;
        --wb-green-border: #86efac;
        --wb-rose-border: #fda4af;
    }

    @media (prefers-color-scheme: dark) {
        :root {
            --wb-border: rgba(255, 255, 255, 0.12);
            --wb-shadow: 0 11px 22px rgba(0, 0, 0, 0.24);

            --wb-blue: rgba(59, 130, 246, 0.20);
            --wb-cyan: rgba(34, 211, 238, 0.18);
            --wb-purple: rgba(168, 85, 247, 0.18);
            --wb-amber: rgba(245, 158, 11, 0.18);
            --wb-green: rgba(34, 197, 94, 0.18);
            --wb-rose: rgba(244, 63, 94, 0.18);

            --wb-blue-border: rgba(96, 165, 250, 0.38);
            --wb-cyan-border: rgba(103, 232, 249, 0.34);
            --wb-purple-border: rgba(196, 181, 253, 0.34);
            --wb-amber-border: rgba(252, 211, 77, 0.32);
            --wb-green-border: rgba(134, 239, 172, 0.32);
            --wb-rose-border: rgba(253, 164, 175, 0.32);
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
    }

    section[data-testid="stSidebar"] {
        background:
            radial-gradient(circle at top left, var(--wb-purple) 0, transparent 25%),
            radial-gradient(circle at bottom right, var(--wb-cyan) 0, transparent 22%),
            var(--secondary-background-color);
        border-right: 1px solid var(--wb-border);
    }

    .block-container {
        max-width: none;
        padding-top: .85rem;
        padding-bottom: 1rem;
        padding-left: .75rem;
        padding-right: .75rem;
    }

    .wb-brand {
        font-size: 1.58rem;
        font-weight: 700;
        letter-spacing: -0.03em;
        margin-bottom: .2rem;
    }

    .hero-card,
    .wb-panel,
    .wb-module-card,
    .wb-brief-card,
    .wb-stat-card,
    .wb-operator-box,
    .card-soft {
        border: 1px solid color-mix(in srgb, var(--wb-border) 78%, transparent);
        border-radius: 22px;
        box-shadow: var(--wb-shadow);
        overflow: hidden;
        background: var(--secondary-background-color);
    }

    .hero-card {
        padding: 1.35rem 1.5rem;
        margin-bottom: 1rem;
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
    }

    .card-soft {
        max-width: 560px;
        margin: 0 auto 1rem auto;
        padding: 1.1rem;
        background:
            radial-gradient(circle at top right, var(--wb-blue) 0, transparent 28%),
            radial-gradient(circle at left bottom, var(--wb-purple) 0, transparent 26%),
            var(--secondary-background-color);
    }

    .page-eyebrow {
        font-size: .84rem;
        font-weight: 700;
        letter-spacing: .08em;
        text-transform: uppercase;
        margin-bottom: .45rem;
        opacity: .9;
    }

    .page-title {
        font-size: 2.05rem;
        line-height: 1.08;
        font-weight: 700;
        margin: 0 0 .35rem 0;
    }

    .page-subtitle {
        font-size: 1rem;
        margin: 0;
        opacity: .82;
    }

    .section-title {
        font-size: 1rem;
        font-weight: 700;
        margin-bottom: .8rem;
    }

    .wb-hero-chip-wrap {
        display: flex;
        gap: .55rem;
        flex-wrap: wrap;
        align-items: center;
    }

    .wb-hero-chip {
        background: linear-gradient(135deg, var(--wb-blue), var(--wb-purple));
        border: 1px solid var(--wb-blue-border);
        border-radius: 999px;
        padding: .5rem .8rem;
        font-size: .9rem;
        font-weight: 600;
    }

    .wb-stat-card {
        min-height: 98px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        gap: .22rem;
    }

    .wb-stat-label {
        font-size: .92rem;
        font-weight: 600;
        margin-bottom: .18rem;
        opacity: .82;
    }

    .wb-stat-value {
        font-size: 1.55rem;
        line-height: 1.1;
        font-weight: 700;
    }

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
        background: rgba(255, 255, 255, 0.28);
        border: 1px solid var(--wb-border);
        backdrop-filter: blur(8px);
    }

    @media (prefers-color-scheme: dark) {
        .wb-module-icon {
            background: rgba(255, 255, 255, 0.06);
        }
    }

    .wb-module-list {
        margin: 0;
        padding-left: 1.2rem;
    }

    .wb-module-list li {
        margin-bottom: .35rem;
    }

    .wb-page-link-wrap {
        margin-top: .55rem;
    }

    .wb-page-link-wrap [data-testid="stPageLink"] a {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 44px;
        width: 100%;
        border-radius: 14px;
        border: 1px solid var(--wb-border);
        background: linear-gradient(135deg, var(--wb-blue), var(--wb-purple));
        text-decoration: none;
        box-shadow: none;
    }

    .wb-page-link-wrap [data-testid="stPageLink"] a:hover {
        border-color: var(--wb-blue-border);
        background: linear-gradient(135deg, var(--wb-cyan), var(--wb-blue));
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
        margin-bottom: .4rem;
        opacity: .82;
    }

    .wb-brief-value {
        font-size: 1.9rem;
        font-weight: 700;
        line-height: 1;
        margin-bottom: .48rem;
    }

    .wb-brief-desc {
        font-size: .95rem;
        opacity: .82;
    }

    .wb-operator-top {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: .75rem;
        margin-bottom: .9rem;
    }

    .wb-operator-badge {
        background: linear-gradient(135deg, var(--wb-blue), var(--wb-purple));
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
        opacity: .82;
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
        opacity: .8;
    }

    .wb-operator-chip strong {
        font-size: 1.02rem;
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
        background: linear-gradient(135deg, var(--wb-blue), var(--wb-purple)) !important;
        box-shadow: none !important;
    }

    .stButton > button:hover,
    .stFormSubmitButton > button:hover {
        border-color: var(--wb-blue-border) !important;
        background: linear-gradient(135deg, var(--wb-cyan), var(--wb-blue)) !important;
    }

    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a {
        border-radius: 14px;
    }

    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a:hover {
        background: linear-gradient(90deg, var(--wb-purple), transparent);
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
    
/* mypage */
.wb-info-panel,
.wb-action-panel {
    padding: 1.05rem 1.1rem;
}

.wb-info-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: .85rem;
}

.wb-info-item {
    background: linear-gradient(135deg, var(--wb-blue), var(--secondary-background-color) 72%);
    border: 1px solid var(--wb-blue-border);
    border-radius: 16px;
    padding: .95rem 1rem;
    min-height: 96px;
}

.wb-info-item:nth-child(2n) {
    background: linear-gradient(135deg, var(--wb-purple), var(--secondary-background-color) 72%);
    border-color: var(--wb-purple-border);
}

.wb-info-label {
    font-size: .9rem;
    font-weight: 600;
    margin-bottom: .45rem;
    opacity: .78;
}

.wb-info-value {
    font-size: 1.18rem;
    font-weight: 700;
    line-height: 1.25;
    word-break: break-word;
}

.wb-action-panel .stForm {
    margin-bottom: 0;
}

.wb-action-panel [data-testid="stForm"] {
    background: transparent;
    border: 0;
    padding: 0;
}

@media (max-width: 900px) {
    .wb-info-grid {
        grid-template-columns: 1fr;
    }
}

    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
