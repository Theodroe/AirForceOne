def get_topbar_css() -> str:
    return '''
    <style>
    .wb-topbar-shell {
        width: 100%;
        margin: 0 0 16px 0;
        padding: 12px 18px;
        background: #ffffff;
        border: 1px solid #e6edf5;
        border-radius: 18px;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.05);
    }

    .wb-topbar-brand {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        min-height: 40px;
        font-size: 1.02rem;
        font-weight: 900;
        color: #0f172a;
        letter-spacing: -0.02em;
        white-space: nowrap;
    }

    .wb-topbar-brand-mark {
        width: 36px;
        height: 36px;
        border-radius: 12px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, #dbeafe 0%, #eff6ff 100%);
        color: #2563eb;
        box-shadow: inset 0 0 0 1px rgba(37, 99, 235, 0.10);
        font-size: 1.02rem;
        flex: 0 0 auto;
    }

    .wb-topbar-nav-slot {
        position: relative;
        min-height: 40px;
    }

    .wb-topbar-nav-slot::after {
        content: "";
        position: absolute;
        left: 0;
        right: 0;
        bottom: -1px;
        height: 1px;
        background: linear-gradient(90deg, transparent 0%, #e8eef6 8%, #e8eef6 92%, transparent 100%);
    }

    .wb-topbar-shell .stButton > button {
        min-height: 40px !important;
        border: none !important;
        border-bottom: 2px solid transparent !important;
        border-radius: 0 !important;
        background: transparent !important;
        box-shadow: none !important;
        color: #334155 !important;
        font-size: 0.96rem !important;
        font-weight: 700 !important;
        line-height: 1 !important;
        padding: 0 4px 10px 4px !important;
        white-space: nowrap !important;
    }

    .wb-topbar-shell .stButton > button:hover {
        background: transparent !important;
        color: #1d4ed8 !important;
        border-bottom-color: #bfdbfe !important;
        transform: none !important;
    }

    .wb-topbar-shell .stButton > button:disabled {
        opacity: 1 !important;
        background: transparent !important;
        color: #1d4ed8 !important;
        border-bottom-color: #2563eb !important;
        -webkit-text-fill-color: #1d4ed8 !important;
    }

    .wb-topbar-sep {
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 40px;
        color: #d0d9e6;
        font-size: 0.95rem;
        user-select: none;
        padding-bottom: 8px;
    }

    .wb-topbar-user {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        min-height: 40px;
    }

    .wb-topbar-user-chip {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        padding: 8px 14px;
        border-radius: 999px;
        border: 1px solid #dbe4ef;
        background: #ffffff;
        color: #334155;
        font-size: 0.9rem;
        font-weight: 700;
        white-space: nowrap;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.03);
    }

    .wb-topbar-user-dot {
        width: 8px;
        height: 8px;
        border-radius: 999px;
        background: #2563eb;
        box-shadow: 0 0 0 4px rgba(37,99,235,0.12);
        flex: 0 0 auto;
    }

    @media (max-width: 1200px) {
        .wb-topbar-shell {
            padding: 10px 14px;
        }
        .wb-topbar-brand {
            font-size: 0.96rem;
        }
        .wb-topbar-shell .stButton > button {
            font-size: 0.9rem !important;
        }
        .wb-topbar-user-chip {
            font-size: 0.83rem;
            padding: 7px 12px;
        }
    }
    </style>
    '''
