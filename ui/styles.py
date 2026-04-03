from __future__ import annotations

import streamlit as st

_LIGHT = {
    "bg": "#f4f7fb",
    "surface": "#ffffff",
    "surface_2": "#f7faff",
    "border": "#d9e4f0",
    "text": "#132238",
    "muted": "#66758b",
    "primary": "#2f6fed",
    "primary_soft": "#e8f0ff",
    "success": "#0f766e",
    "success_soft": "#e8f7ee",
    "danger_soft": "#fee9e7",
    "card_grad": "linear-gradient(180deg, #ffffff 0%, #f8fbff 100%)",
    "hero_grad": "linear-gradient(135deg, #ffffff 0%, #edf4ff 100%)",
    "shadow": "0 12px 28px rgba(15, 23, 42, 0.06)",
}

_DARK = {
    "bg": "#0b1220",
    "surface": "#111a2b",
    "surface_2": "#162235",
    "border": "#24344f",
    "text": "#e8eef8",
    "muted": "#9aabc4",
    "primary": "#70a7ff",
    "primary_soft": "rgba(112, 167, 255, 0.15)",
    "success": "#34d399",
    "success_soft": "rgba(52, 211, 153, 0.14)",
    "danger_soft": "rgba(248, 113, 113, 0.14)",
    "card_grad": "linear-gradient(180deg, #121d30 0%, #0f1828 100%)",
    "hero_grad": "linear-gradient(135deg, #101a2b 0%, #142238 100%)",
    "shadow": "0 14px 30px rgba(0, 0, 0, 0.25)",
}


def _theme_vars(colors: dict[str, str]) -> str:
    return "
".join([
        f"--wb-bg: {colors['bg']};",
        f"--wb-surface: {colors['surface']};",
        f"--wb-surface-2: {colors['surface_2']};",
        f"--wb-border: {colors['border']};",
        f"--wb-text: {colors['text']};",
        f"--wb-muted: {colors['muted']};",
        f"--wb-primary: {colors['primary']};",
        f"--wb-primary-soft: {colors['primary_soft']};",
        f"--wb-success: {colors['success']};",
        f"--wb-success-soft: {colors['success_soft']};",
        f"--wb-danger-soft: {colors['danger_soft']};",
        f"--wb-card-grad: {colors['card_grad']};",
        f"--wb-hero-grad: {colors['hero_grad']};",
        f"--wb-shadow: {colors['shadow']};",
    ])


def render_streamlit_base_style() -> None:
    root_css = f"""
:root {{
{_theme_vars(_LIGHT)}
    --wb-radius: 18px;
    --wb-radius-sm: 12px;
}}
@media (prefers-color-scheme: dark) {{
  :root {{
{_theme_vars(_DARK)}
    --wb-radius: 18px;
    --wb-radius-sm: 12px;
  }}
}}
"""

    css = f"""
<style>
{root_css}
[data-testid="stSidebarNav"] {{ display:none; }}
html, body, [class*="css"], .stApp {{ color:var(--wb-text); }}
[data-testid="stAppViewContainer"], [data-testid="stMain"], .stApp {{ background:var(--wb-bg); }}
[data-testid="stHeader"] {{ background:transparent; }}
section[data-testid="stSidebar"] {{ background:var(--wb-surface); border-right:1px solid var(--wb-border); }}
section[data-testid="stSidebar"] * {{ color:var(--wb-text) !important; }}
[data-testid="stSidebarCollapseButton"], [data-testid="stSidebarCollapseButton"] button, [data-testid="collapsedControl"] {{ opacity:1 !important; visibility:visible !important; }}
[data-testid="stSidebarCollapseButton"] button, [data-testid="collapsedControl"] {{ display:inline-flex !important; align-items:center !important; justify-content:center !important; min-width:40px !important; min-height:40px !important; background:var(--wb-primary) !important; border:1px solid var(--wb-primary) !important; border-radius:12px !important; box-shadow:var(--wb-shadow) !important; }}
[data-testid="stSidebarCollapseButton"] button:hover, [data-testid="collapsedControl"]:hover {{ background:var(--wb-primary-soft) !important; border-color:var(--wb-primary) !important; }}
[data-testid="stSidebarCollapseButton"] button svg, [data-testid="stSidebarCollapseButton"] button *, [data-testid="collapsedControl"] svg, [data-testid="collapsedControl"] * {{ color:var(--wb-surface) !important; fill:var(--wb-surface) !important; stroke:var(--wb-surface) !important; opacity:1 !important; }}
[data-testid="collapsedControl"] {{ position:fixed !important; top:4.2rem !important; left:.9rem !important; z-index:1000 !important; }}
.block-container {{ max-width:none; padding:.9rem .75rem 1rem; }}
.wb-brand {{ font-size:1.65rem; font-weight:800; letter-spacing:-0.03em; margin-bottom:.2rem; }}
.hero-card {{ background:var(--wb-hero-grad); border:1px solid var(--wb-border); border-radius:24px; box-shadow:var(--wb-shadow); padding:1.3rem 1.45rem; margin-bottom:1rem; }}
.wb-panel, .card-soft, .wb-module-card, .wb-brief-card {{ background:var(--wb-card-grad); border:1px solid var(--wb-border); box-shadow:var(--wb-shadow); }}
.wb-panel, .card-soft, .wb-module-card {{ border-radius:20px; padding:1rem 1.05rem; }}
.wb-brief-card {{ border-radius:18px; padding:1rem; min-height:126px; }}
.page-eyebrow {{ color:var(--wb-primary); font-size:.88rem; font-weight:800; letter-spacing:.04em; margin-bottom:.32rem; }}
.page-title {{ font-size:2.12rem; line-height:1.08; font-weight:800; margin:0 0 .35rem 0; color:var(--wb-text); }}
.page-subtitle {{ color:var(--wb-muted); font-size:1.03rem; margin:0; }}
.section-title {{ font-size:1.03rem; font-weight:800; margin-bottom:.7rem; color:var(--wb-text); }}
p, li, label, .stCaption, .stMarkdown {{ color:var(--wb-text); font-size:.98rem; }}
.wb-hero-chip-wrap {{ display:flex; flex-wrap:wrap; gap:.55rem; }}
.wb-hero-chip {{ padding:.52rem .9rem; border-radius:999px; border:1px solid var(--wb-border); background:var(--wb-surface-2); font-size:.84rem; font-weight:800; color:var(--wb-primary); }}
.wb-module-card {{ min-height:225px; }}
.wb-module-card-strong {{ min-height:250px; }}
.wb-module-head {{ display:flex; align-items:flex-start; gap:.9rem; margin-bottom:.9rem; }}
.wb-module-icon {{ width:54px; height:54px; border-radius:16px; display:flex; align-items:center; justify-content:center; margin-bottom:.9rem; background:var(--wb-primary-soft); color:var(--wb-primary); font-size:1.55rem; }}
.wb-module-variant-success .wb-module-icon {{ background:var(--wb-success-soft); color:var(--wb-success); }}
.wb-module-list {{ margin:0 0 1rem 1.1rem; padding:0; color:var(--wb-muted); }}
.wb-module-list li {{ margin-bottom:.28rem; }}
.wb-brief-label {{ font-size:.82rem; color:var(--wb-muted); font-weight:800; margin-bottom:.45rem; }}
.wb-brief-value {{ font-size:1.38rem; line-height:1.1; color:var(--wb-text); font-weight:800; margin-bottom:.32rem; }}
.wb-brief-desc {{ font-size:.88rem; color:var(--wb-muted); }}
section[data-testid="stSidebar"] [data-testid="stPageLinkContainer"] a, [data-testid="stSidebar"] .stPageLink a {{ display:flex !important; align-items:center !important; width:100% !important; border:1px solid var(--wb-border) !important; border-radius:16px !important; padding:.85rem .9rem !important; margin-bottom:.55rem !important; background:var(--wb-surface) !important; box-shadow:none !important; text-decoration:none !important; font-weight:700 !important; }}
section[data-testid="stSidebar"] [data-testid="stPageLinkContainer"] a:hover, [data-testid="stSidebar"] .stPageLink a:hover {{ border-color:var(--wb-primary) !important; background:var(--wb-primary-soft) !important; color:var(--wb-primary) !important; }}
[data-testid="stSidebar"] .stPageLink a[aria-current="page"] {{ background:var(--wb-primary-soft) !important; color:var(--wb-primary) !important; border-color:var(--wb-primary) !important; box-shadow:none !important; }}
[data-testid="stSidebar"] .stPageLink a[aria-current="page"] * {{ color:var(--wb-primary) !important; }}
.wb-info-grid {{ display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:.8rem; }}
.wb-info-item {{ background:var(--wb-surface); border:1px solid var(--wb-border); border-radius:14px; padding:.9rem 1rem; }}
.wb-info-label {{ color:var(--wb-muted); font-size:.84rem; margin-bottom:.2rem; }}
.wb-info-value {{ color:var(--wb-text); font-size:1.05rem; font-weight:700; }}
.wb-operator-box {{ background:var(--wb-card-grad); border:1px solid var(--wb-border); border-radius:22px; box-shadow:var(--wb-shadow); padding:1rem; }}
.wb-operator-top {{ display:flex; align-items:center; justify-content:space-between; gap:.5rem; margin-bottom:.55rem; }}
.wb-operator-badge {{ display:inline-flex; align-items:center; padding:.26rem .56rem; border-radius:999px; background:var(--wb-primary-soft); color:var(--wb-primary); font-size:.74rem; font-weight:800; }}
.wb-operator-state {{ font-size:.74rem; color:var(--wb-muted); font-weight:700; }}
.wb-operator-name {{ font-size:1.18rem; font-weight:800; color:var(--wb-text); margin-bottom:.18rem; }}
.wb-operator-meta {{ font-size:.86rem; color:var(--wb-muted); }}
.wb-operator-grid {{ display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:.55rem; margin-top:.8rem; }}
.wb-operator-chip {{ border:1px solid var(--wb-border); border-radius:14px; background:var(--wb-surface); padding:.7rem .75rem; }}
.wb-operator-chip span {{ display:block; font-size:.75rem; color:var(--wb-muted); margin-bottom:.2rem; }}
.wb-operator-chip strong {{ font-size:.88rem; color:var(--wb-text); }}
.stTextInput input, .stNumberInput input, .stTextArea textarea, .stDateInput input, .stSelectbox [data-baseweb="select"] > div, .stMultiSelect [data-baseweb="select"] > div {{ background:var(--wb-surface) !important; color:var(--wb-text) !important; border:1px solid var(--wb-border) !important; border-radius:14px !important; box-shadow:none !important; }}
.stButton > button, .stFormSubmitButton > button {{ width:100%; min-height:44px; font-size:1rem; font-weight:700; white-space:nowrap; border-radius:14px !important; border:1px solid var(--wb-border) !important; background:var(--wb-surface) !important; color:var(--wb-text) !important; box-shadow:none !important; }}
.stButton > button:hover, .stFormSubmitButton > button:hover {{ border-color:var(--wb-primary) !important; color:var(--wb-primary) !important; background:var(--wb-primary-soft) !important; }}
[data-testid="stMetricValue"], [data-testid="stMetricLabel"] {{ color:var(--wb-text) !important; }}
[data-testid="stDataFrame"], [data-testid="stTable"], [data-testid="stPlotlyChart"] {{ border:1px solid var(--wb-border); border-radius:18px; overflow:hidden; background:var(--wb-surface); }}
[data-testid="stAlert"] {{ border-radius:14px; border:1px solid var(--wb-border); }}
.stInfo {{ background:var(--wb-primary-soft) !important; }}
.stSuccess {{ background:var(--wb-success-soft) !important; }}
.stError {{ background:var(--wb-danger-soft) !important; }}
.stTabs [data-baseweb="tab-list"] {{ gap:.4rem; }}
.stTabs [data-baseweb="tab"] {{ border-radius:12px 12px 0 0; background:var(--wb-surface); border:1px solid var(--wb-border); padding:.7rem 1rem; }}
.wb-stat-grid {{ display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:.85rem; }}
.wb-stat-card {{ background:var(--wb-card-grad); border:1px solid var(--wb-border); border-radius:18px; padding:.95rem 1rem; min-height:104px; box-shadow:var(--wb-shadow); }}
.wb-stat-label {{ color:var(--wb-muted); font-size:.82rem; font-weight:700; margin-bottom:.35rem; }}
.wb-stat-value {{ color:var(--wb-text); font-size:1.9rem; font-weight:800; line-height:1; }}
@media (max-width: 1024px) {{ .wb-stat-grid, .wb-info-grid, .wb-operator-grid {{ grid-template-columns:repeat(2,minmax(0,1fr)); }} }}
</style>
"""
    st.markdown(css, unsafe_allow_html=True)
