from __future__ import annotations

from contextlib import contextmanager
from urllib.parse import quote_plus

import streamlit as st
from sqlalchemy import create_engine

try:
    import pymysql
    from pymysql.cursors import DictCursor
except Exception:
    pymysql = None
    DictCursor = None


def _secret_get(*path, default=None):
    try:
        cur = st.secrets
        for key in path:
            cur = cur[key]
        return cur
    except Exception:
        return default


def _build_local_url() -> str | None:
    host = _secret_get("mysql", "host")
    port = _secret_get("mysql", "port", default=3306)
    database = _secret_get("mysql", "database")
    user = _secret_get("mysql", "user")
    password = _secret_get("mysql", "password", default="")
    charset = _secret_get("mysql", "charset", default="utf8mb4")

    if not (host and database and user):
        return None

    return (
        f"mysql+pymysql://{quote_plus(str(user))}:{quote_plus(str(password))}"
        f"@{host}:{int(port)}/{database}?charset={charset}"
    )


@st.cache_resource
def get_engine():
    try:
        return st.connection("weather", type="sql").engine
    except Exception:
        pass

    local_url = _build_local_url()
    if local_url:
        return create_engine(
            local_url,
            pool_pre_ping=True,
            pool_recycle=3600,
        )

    raise RuntimeError(
        "DB 연결 설정을 찾지 못했습니다. "
        "`.streamlit/secrets.toml`에 `[connections.weather]` 또는 `[mysql]` 설정을 넣어 주세요."
    )


def get_connection():
    return get_engine().raw_connection()


def _dict_cursor(conn):
    if pymysql is not None and DictCursor is not None:
        try:
            return conn.cursor(DictCursor)
        except Exception:
            pass

    try:
        return conn.cursor(dictionary=True)
    except Exception:
        return conn.cursor()


@contextmanager
def get_cursor():
    conn = get_connection()
    cur = _dict_cursor(conn)
    try:
        yield cur, conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()
