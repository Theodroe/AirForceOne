# Refactored W-BOSS

- `services/`: business logic + session/auth/log handling
- `ui/`: Streamlit rendering layer
- `functions/`: compatibility shims for old imports


## DB 인증 연결
- 인증/회원가입/탈퇴/비밀번호 변경/계급 수정은 MySQL `users` 테이블을 직접 사용합니다.
- 비밀번호는 현재 평문 비교 방식입니다. (`users.password`)
- `.streamlit/secrets.toml`의 `[database]` 값을 먼저 읽고, 없으면 `WBOSS_DB_*` 환경변수를 사용합니다.
- 처음 세팅할 때는 `DB_create.sql`을 실행해 `users`, `access_log`, `audit_log`를 생성하세요.
