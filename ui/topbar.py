import html
import streamlit as st

from services import get_current_user, is_authenticated


TOPBAR_ITEMS = [
    ("메인", "/", "main"),
    ("실시간", "/best_train_time", "realtime"),
    ("연간 훈련", "/heatmap", "annual"),
    ("마이페이지", "/my_page", "mypage"),
]


def _current_user_summary() -> str:
    user = get_current_user() or {}
    authenticated = is_authenticated()

    if authenticated and user:
        name = str(user.get("username", "operator"))
        service_number = str(user.get("service_number", "-"))
        rank = str(user.get("military_rank") or "미설정")
        return f"{name} · {service_number} · {rank}"

    return "Guest · 로그인 필요 · -"


def render_topbar(current_key: str) -> None:
    summary = html.escape(_current_user_summary())

    nav_items = []
    for label, href, key in TOPBAR_ITEMS:
        cls = "wb-nav-link active" if key == current_key else "wb-nav-link"
        nav_items.append(
            f'<a class="{cls}" href="{href}" target="_self">{html.escape(label)}</a>'
        )

    st.markdown(
        f'''
        <style>
        .wb-html-topbar {{
            width: 100%;
            display: grid;
            grid-template-columns: 180px 1fr auto;
            align-items: center;
            gap: 28px;
            padding: 14px 22px;
            margin: 0 0 18px 0;
            background: #ffffff;
            border-bottom: 1px solid #e5edf6;
        }}

        .wb-brand {{
            display: inline-flex;
            align-items: center;
            gap: 10px;
            font-weight: 900;
            font-size: 1.05rem;
            color: #0f172a;
            letter-spacing: -0.02em;
            white-space: nowrap;
        }}

        .wb-brand-mark {{
            width: 38px;
            height: 38px;
            border-radius: 12px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #dbeafe 0%, #eff6ff 100%);
            color: #2563eb;
            box-shadow: inset 0 0 0 1px rgba(37, 99, 235, 0.10);
            font-size: 1.04rem;
            flex: 0 0 auto;
        }}

        .wb-nav {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 18px;
        }}

        .wb-nav-link {{
            position: relative;
            display: inline-flex;
            align-items: center;
            text-decoration: none !important;
            color: #334155 !important;
            font-size: 0.98rem;
            font-weight: 700;
            line-height: 1;
            padding: 10px 2px 12px 2px;
            transition: color .15s ease;
        }}

        .wb-nav-link::after {{
            content: "";
            position: absolute;
            left: 0;
            right: 0;
            bottom: -2px;
            height: 2px;
            background: transparent;
            border-radius: 999px;
            transition: background .15s ease;
        }}

        .wb-nav-link:hover {{
            color: #1d4ed8 !important;
        }}

        .wb-nav-link:hover::after {{
            background: #bfdbfe;
        }}

        .wb-nav-link.active {{
            color: #1d4ed8 !important;
            font-weight: 800;
        }}

        .wb-nav-link.active::after {{
            background: #2563eb;
        }}

        .wb-user {{
            display: inline-flex;
            align-items: center;
            gap: 10px;
            padding: 9px 14px;
            border-radius: 999px;
            border: 1px solid #dbe4ef;
            background: #ffffff;
            color: #334155;
            font-size: 0.92rem;
            font-weight: 700;
            white-space: nowrap;
            box-shadow: 0 4px 12px rgba(15, 23, 42, 0.03);
        }}

        .wb-user-dot {{
            width: 8px;
            height: 8px;
            border-radius: 999px;
            background: #2563eb;
            box-shadow: 0 0 0 4px rgba(37,99,235,0.12);
            flex: 0 0 auto;
        }}

        @media (max-width: 1200px) {{
            .wb-html-topbar {{
                grid-template-columns: 160px 1fr auto;
                gap: 18px;
                padding: 12px 16px;
            }}
            .wb-brand {{
                font-size: 0.98rem;
            }}
            .wb-nav {{
                gap: 14px;
            }}
            .wb-nav-link {{
                font-size: 0.92rem;
            }}
            .wb-user {{
                font-size: 0.84rem;
                padding: 8px 12px;
            }}
        }}
        </style>

        <div class="wb-html-topbar">
            <div class="wb-brand">
                <span class="wb-brand-mark">🌐</span>
                <span>W-BOSS</span>
            </div>
            <div class="wb-nav">
                {"".join(nav_items)}
            </div>
            <div class="wb-user">
                <span class="wb-user-dot"></span>
                <span>{summary}</span>
            </div>
        </div>
        ''',
        unsafe_allow_html=True,
    )
