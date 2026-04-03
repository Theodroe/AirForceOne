from __future__ import annotations

import streamlit as st


def render_streamlit_base_style() -> None:
    css = """
    <style>
    :root {
        --wb-radius: 18px;
        --wb-radius-sm: 12px;
        --wb-border: rgba(120, 130, 150, 0.22);
        --wb-shadow: 0 12px 28px rgba(15, 23, 42, 0.08);
        --wb-text-muted: rgba(31, 41, 55, 0.72);
        --wb-accent-soft: color-mix(in srgb, var(--primary-color) 10%, transparent);
        --wb-accent-border: color-mix(in srgb, var(--primary-color) 26%, transparent);
    }

    @media (prefers-color-scheme: dark) {
        :root {
            --wb-border: rgba(255, 255, 255, 0.12);
            --wb-shadow: 0 12px 28px rgba(0, 0, 0, 0.28);
            --wb-text-muted: rgba(255, 255, 255, 0.72);
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

    .wb-brand {
        font-size: 1.65rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        margin-bottom: .2rem;
    }

    .hero-card,
    .wb-panel,
    .wb-module-card,
    .wb-brief-card,
    .wb-stat-card,
    .wb-operator-box {
        background: var(--secondary-background-color);
        border: 1px solid var(--wb-border);
        border-radius: 20px;
        box-shadow: var(--wb-shadow);
    }

    .hero-card {
        padding: 1.3rem 1.45rem;
        margin-bottom: 1rem;
    }

    .wb-panel,
    .wb-module-card,
    .wb-brief-card,
    .wb-stat-card,
    .wb-operator-box {
        padding: 1rem 1.05rem;
    }

    .page-eyebrow {
        color: var(--primary-color);
        font-size: .92rem;
        font-weight: 700;
        margin-bottom: .35rem;
    }

    .page-title {
        font-size: 2.15rem;
        line-height: 1.08;
        font-weight: 800;
        margin: 0 0 .35rem 0;
        color: var(--text-color);
    }

    .page-subtitle {
        color: var(--wb-text-muted);
        font-size: 1.03rem;
        margin: 0;
    }

    .section-title {
        font-size: 1.03rem;
        font-weight: 800;
        margin-bottom: .7rem;
        color: var(--text-color);
    }

    .wb-hero-chip-wrap {
        display: flex;
        gap: .55rem;
        flex-wrap: wrap;
        align-items: center;
    }

    .wb-hero-chip {
        background: var(--wb-accent-soft);
        border: 1px solid var(--wb-accent-border);
        color: var(--text-color);
        border-radius: 999px;
        padding: .5rem .8rem;
        font-size: .9rem;
        font-weight: 700;
    }

    .wb-stat-card {
        min-height: 92px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        gap: .2rem;
    }

    .wb-stat-label {
        font-size: .92rem;
        font-weight: 700;
        color: var(--wb-text-muted) !important;
        -webkit-text-fill-color: var(--wb-text-muted) !important;
        margin-bottom: .15rem;
    }

    .wb-stat-value {
        font-size: 1.45rem;
        line-height: 1.15;
        font-weight: 800;
        color: var(--text-color) !important;
        -webkit-text-fill-color: var(--text-color) !important;
    }

    .wb-stat-card,
    .wb-stat-card * {
        color: var(--text-color);
    }

    .wb-stat-label * {
        color: var(--wb-text-muted) !important;
        -webkit-text-fill-color: var(--wb-text-muted) !important;
    }

    .wb-stat-value * {
        color: var(--text-color) !important;
        -webkit-text-fill-color: var(--text-color) !important;
    }

    .wb-module-card {
        min-height: 220px;
    }

    .wb-module-card-strong {
        position: relative;
    }

    .wb-module-variant-primary .wb-module-icon,
    .wb-module-variant-success .wb-module-icon {
        background: var(--wb-accent-soft);
        border: 1px solid var(--wb-accent-border);
        color: var(--text-color);
    }

    .wb-module-head {
        display: flex;
        gap: .8rem;
        align-items: flex-start;
        margin-bottom: .9rem;
    }

    .wb-module-icon {
        width: 48px;
        height: 48px;
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.35rem;
        flex-shrink: 0;
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
        min-height: 124px;
    }

    .wb-brief-label {
        font-size: .9rem;
        font-weight: 700;
        color: var(--wb-text-muted);
        margin-bottom: .35rem;
    }

    .wb-brief-value {
        font-size: 1.9rem;
        font-weight: 800;
        line-height: 1;
        color: var(--text-color);
        margin-bottom: .45rem;
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
        background: var(--wb-accent-soft);
        border-radius: 999px;
        padding: .45rem .8rem;
        font-size: .85rem;
        font-weight: 800;
    }

    .wb-operator-state {
        font-size: .95rem;
        font-weight: 700;
    }

    .wb-operator-name {
        font-size: 2rem;
        font-weight: 900;
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
        font-size: 1.05rem;
        color: var(--text-color);
    }

    .stButton > button,
    .stFormSubmitButton > button {
        width: 100%;
        min-height: 44px;
        font-size: 1rem;
        font-weight: 700;
        white-space: nowrap;
        border-radius: 14px !important;
        border: 1px solid var(--wb-border) !important;
        background: var(--secondary-background-color) !important;
        color: var(--text-color) !important;
        box-shadow: none !important;
    }

    .stButton > button:hover,
    .stFormSubmitButton > button:hover {
        border-color: var(--primary-color) !important;
        color: var(--primary-color) !important;
        background: var(--wb-accent-soft) !important;
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
