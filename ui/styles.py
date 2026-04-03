from __future__ import annotations

import streamlit as st


def render_streamlit_base_style() -> None:
    css = """
    <style>
    :root {
        --wb-radius: 20px;
        --wb-radius-sm: 14px;
        --wb-border: color-mix(in srgb, var(--text-color) 14%, transparent);
        --wb-border-strong: color-mix(in srgb, var(--text-color) 22%, transparent);
        --wb-shadow: 0 14px 34px rgba(15, 23, 42, 0.10);
        --wb-shadow-hover: 0 18px 40px rgba(15, 23, 42, 0.14);
        --wb-text-muted: color-mix(in srgb, var(--text-color) 72%, transparent);
        --wb-accent-soft: color-mix(in srgb, var(--primary-color) 16%, var(--secondary-background-color));
        --wb-accent-soft-2: color-mix(in srgb, var(--primary-color) 10%, var(--background-color));
        --wb-accent-alt: color-mix(in srgb, #7c3aed 14%, var(--secondary-background-color));
        --wb-accent-alt-2: color-mix(in srgb, #06b6d4 12%, var(--secondary-background-color));
        --wb-accent-border: color-mix(in srgb, var(--primary-color) 24%, transparent);
        --wb-card-highlight: linear-gradient(
            135deg,
            color-mix(in srgb, var(--primary-color) 5%, var(--secondary-background-color)) 0%,
            color-mix(in srgb, #7c3aed 4%, var(--secondary-background-color)) 48%,
            color-mix(in srgb, #06b6d4 3%, var(--secondary-background-color)) 100%
        );
    }

    @media (prefers-color-scheme: dark) {
        :root {
            --wb-border: color-mix(in srgb, white 12%, transparent);
            --wb-border-strong: color-mix(in srgb, white 18%, transparent);
            --wb-shadow: 0 14px 34px rgba(0, 0, 0, 0.34);
            --wb-shadow-hover: 0 18px 40px rgba(0, 0, 0, 0.42);
            --wb-text-muted: color-mix(in srgb, var(--text-color) 74%, transparent);
            --wb-accent-soft: color-mix(in srgb, var(--primary-color) 18%, var(--secondary-background-color));
            --wb-accent-soft-2: color-mix(in srgb, var(--primary-color) 12%, var(--background-color));
            --wb-accent-alt: color-mix(in srgb, #a78bfa 16%, var(--secondary-background-color));
            --wb-accent-alt-2: color-mix(in srgb, #22d3ee 14%, var(--secondary-background-color));
            --wb-accent-border: color-mix(in srgb, var(--primary-color) 28%, transparent);
            --wb-card-highlight: linear-gradient(
                135deg,
                color-mix(in srgb, var(--primary-color) 7%, var(--secondary-background-color)) 0%,
                color-mix(in srgb, #a78bfa 5%, var(--secondary-background-color)) 48%,
                color-mix(in srgb, #22d3ee 4%, var(--secondary-background-color)) 100%
            );
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

    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a {
        border-radius: 14px;
    }

    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a:hover {
        background: color-mix(in srgb, var(--primary-color) 10%, transparent);
    }

    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a[aria-current="page"] {
        background: linear-gradient(
            90deg,
            color-mix(in srgb, var(--primary-color) 14%, var(--secondary-background-color)) 0%,
            color-mix(in srgb, #7c3aed 8%, var(--secondary-background-color)) 55%,
            color-mix(in srgb, #06b6d4 6%, var(--secondary-background-color)) 100%
        );
        border: 1px solid color-mix(in srgb, var(--primary-color) 18%, transparent);
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
        font-weight: 650;
        letter-spacing: -0.03em;
        margin-bottom: .2rem;
    }

    .hero-card,
    .wb-panel,
    .wb-module-card,
    .wb-brief-card,
    .wb-stat-card,
    .wb-operator-box {
        background: var(--wb-card-highlight);
        border: 1.1px solid var(--wb-border);
        border-radius: 22px;
        box-shadow: var(--wb-shadow);
        transition: box-shadow .18s ease, border-color .18s ease, transform .18s ease;
    }

    .hero-card:hover,
    .wb-panel:hover,
    .wb-module-card:hover,
    .wb-brief-card:hover,
    .wb-stat-card:hover,
    .wb-operator-box:hover {
        border-color: var(--wb-border-strong);
        box-shadow: var(--wb-shadow-hover);
        transform: translateY(-1px);
    }

    .hero-card {
        padding: 1.45rem 1.6rem;
        margin-bottom: 1.05rem;
        position: relative;
        overflow: hidden;
        background: linear-gradient(
            135deg,
            color-mix(in srgb, var(--primary-color) 7%, var(--secondary-background-color)) 0%,
            color-mix(in srgb, #7c3aed 4%, var(--secondary-background-color)) 52%,
            color-mix(in srgb, #06b6d4 3%, var(--secondary-background-color)) 100%
        );
    }
    .hero-card::after {
        content: "";
        position: absolute;
        right: -40px;
        top: -40px;
        width: 180px;
        height: 180px;
        border-radius: 999px;
        background: radial-gradient(
            circle,
            color-mix(in srgb, var(--primary-color) 10%, transparent) 0%,
            transparent 72%
        );
        pointer-events: none;
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
        font-size: .84rem;
        font-weight: 650;
        letter-spacing: .08em;
        text-transform: uppercase;
        margin-bottom: .45rem;
    }

    .page-title {
        font-size: 2.15rem;
        line-height: 1.08;
        font-weight: 740;
        margin: 0 0 .35rem 0;
        color: var(--text-color);
    }

    .page-subtitle {
        color: var(--wb-text-muted);
        font-size: 1.03rem;
        margin: 0;
    }

    .section-title {
        font-size: 1.02rem;
        font-weight: 650;
        margin-bottom: .8rem;
        color: var(--text-color);
        letter-spacing: -0.01em;
    }

    .wb-hero-chip-wrap {
        display: flex;
        gap: .55rem;
        flex-wrap: wrap;
        align-items: center;
    }

    .wb-hero-chip {
        background: linear-gradient(
            180deg,
            color-mix(in srgb, var(--primary-color) 22%, var(--secondary-background-color)),
            color-mix(in srgb, var(--primary-color) 12%, var(--secondary-background-color))
        );
        border: 1px solid var(--wb-accent-border);
        color: var(--text-color);
        border-radius: 999px;
        padding: .52rem .86rem;
        font-size: .88rem;
        font-weight: 650;
        backdrop-filter: blur(6px);
    }

    .wb-stat-card {
        min-height: 98px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        gap: .22rem;
        position: relative;
        overflow: hidden;
        background: linear-gradient(
            135deg,
            color-mix(in srgb, var(--primary-color) 6%, var(--secondary-background-color)) 0%,
            color-mix(in srgb, #06b6d4 3%, var(--secondary-background-color)) 100%
        );
    }
    .wb-stat-card::before {
        content: "";
        position: absolute;
        inset: auto auto -28px -18px;
        width: 92px;
        height: 92px;
        border-radius: 999px;
        background: radial-gradient(
            circle,
            color-mix(in srgb, var(--primary-color) 10%, transparent) 0%,
            transparent 72%
        );
        opacity: .95;
        pointer-events: none;
    }

    .wb-stat-label {
        font-size: .9rem;
        font-weight: 650;
        color: var(--wb-text-muted);
        margin-bottom: .18rem;
        letter-spacing: -0.01em;
    }

    .wb-stat-value {
        font-size: 1.65rem;
        line-height: 1.1;
        font-weight: 650;
        color: var(--text-color);
        letter-spacing: -0.03em;
    }

    .wb-module-card {
        min-height: 220px;
        position: relative;
        overflow: hidden;
        background: linear-gradient(
            135deg,
            color-mix(in srgb, var(--primary-color) 5%, var(--secondary-background-color)) 0%,
            color-mix(in srgb, #7c3aed 4%, var(--secondary-background-color)) 100%
        );
    }

    .wb-module-card-strong {
        position: relative;
    }
    .wb-module-card-strong::after {
        content: "";
        position: absolute;
        inset: auto -20px -28px auto;
        width: 96px;
        height: 96px;
        border-radius: 999px;
        background: radial-gradient(
            circle,
            color-mix(in srgb, #06b6d4 10%, transparent) 0%,
            transparent 72%
        );
        pointer-events: none;
    }

    .wb-module-variant-primary .wb-module-icon {
        background: linear-gradient(
            180deg,
            color-mix(in srgb, var(--primary-color) 20%, var(--secondary-background-color)),
            color-mix(in srgb, #06b6d4 10%, var(--background-color))
        );
        border: 1px solid color-mix(in srgb, var(--primary-color) 22%, transparent);
        color: var(--text-color);
        box-shadow:
            inset 0 1px 0 color-mix(in srgb, white 22%, transparent),
            0 6px 16px color-mix(in srgb, var(--primary-color) 8%, transparent);
    }

    .wb-module-variant-success .wb-module-icon {
        background: linear-gradient(
            180deg,
            color-mix(in srgb, #7c3aed 18%, var(--secondary-background-color)),
            color-mix(in srgb, #06b6d4 9%, var(--background-color))
        );
        border: 1px solid color-mix(in srgb, #7c3aed 22%, transparent);
        color: var(--text-color);
        box-shadow:
            inset 0 1px 0 color-mix(in srgb, white 22%, transparent),
            0 6px 16px color-mix(in srgb, #7c3aed 8%, transparent);
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
        position: relative;
        overflow: hidden;
        background: linear-gradient(
            135deg,
            color-mix(in srgb, #7c3aed 5%, var(--secondary-background-color)) 0%,
            color-mix(in srgb, #06b6d4 3%, var(--secondary-background-color)) 100%
        );
    }
    .wb-brief-card::before {
        content: "";
        position: absolute;
        inset: auto -18px -26px auto;
        width: 88px;
        height: 88px;
        border-radius: 999px;
        background: radial-gradient(
            circle,
            color-mix(in srgb, #7c3aed 10%, transparent) 0%,
            transparent 74%
        );
        pointer-events: none;
    }

    .wb-brief-label {
        font-size: .9rem;
        font-weight: 650;
        color: var(--wb-text-muted);
        margin-bottom: .4rem;
    }

    .wb-brief-value {
        font-size: 1.95rem;
        font-weight: 650;
        line-height: 1;
        color: var(--text-color);
        margin-bottom: .48rem;
        letter-spacing: -0.03em;
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
        border: 1px solid var(--wb-accent-border);
        border-radius: 999px;
        padding: .45rem .8rem;
        font-size: .85rem;
        font-weight: 650;
    }

    .wb-operator-state {
        font-size: .95rem;
        font-weight: 650;
    }

    .wb-operator-name {
        font-size: 2rem;
        font-weight: 650;
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
        min-height: 46px;
        font-size: 1rem;
        font-weight: 650;
        white-space: nowrap;
        border-radius: 14px !important;
        border: 1px solid var(--wb-border) !important;
        background: linear-gradient(
            180deg,
            color-mix(in srgb, var(--secondary-background-color) 86%, white),
            var(--secondary-background-color)
        ) !important;
        color: var(--text-color) !important;
        box-shadow: 0 6px 16px color-mix(in srgb, black 6%, transparent) !important;
        transition: all .16s ease !important;
    }

    .stButton > button:hover,
    .stFormSubmitButton > button:hover {
        border-color: color-mix(in srgb, var(--primary-color) 20%, transparent) !important;
        color: var(--text-color) !important;
        background: linear-gradient(
            135deg,
            color-mix(in srgb, var(--primary-color) 10%, var(--secondary-background-color)) 0%,
            color-mix(in srgb, #7c3aed 7%, var(--secondary-background-color)) 58%,
            color-mix(in srgb, #06b6d4 5%, var(--secondary-background-color)) 100%
        ) !important;
        transform: translateY(-1px);
        box-shadow: 0 10px 22px color-mix(in srgb, var(--primary-color) 10%, transparent) !important;
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
