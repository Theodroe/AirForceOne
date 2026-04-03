from __future__ import annotations

from datetime import datetime
from zoneinfo import ZoneInfo

KST = ZoneInfo("Asia/Seoul")

def now_kst() -> datetime:
    return datetime.now(KST)

def fmt_hms(dt: datetime | None = None) -> str:
    if dt is None:
        dt = now_kst()
    return dt.strftime("%H:%M:%S")
