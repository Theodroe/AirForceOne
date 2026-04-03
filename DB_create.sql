-- W-BOSS Database Schema (Plain Password / DB Connected)
CREATE DATABASE IF NOT EXISTS weather_db
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE weather_db;

CREATE TABLE IF NOT EXISTS region (
    region_id    INT NOT NULL AUTO_INCREMENT,
    region_name  VARCHAR(50) NOT NULL,
    province     VARCHAR(50) NOT NULL,
    PRIMARY KEY (region_id),
    INDEX idx_province (province)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS spatial_boundary (
    id          INT NOT NULL AUTO_INCREMENT,
    region_id   INT NOT NULL,
    geojson     MEDIUMTEXT NOT NULL,
    crs         VARCHAR(20) NOT NULL DEFAULT 'EPSG:4326',
    updated_at  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uq_region_boundary (region_id),
    CONSTRAINT fk_sb_region FOREIGN KEY (region_id) REFERENCES region(region_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS asos_station (
    station_id         INT NOT NULL,
    region_id          INT NOT NULL,
    station_name       VARCHAR(50) NOT NULL,
    lat                DECIMAL(9,6) NOT NULL,
    lng                DECIMAL(9,6) NOT NULL,
    operational_since  DATE,
    PRIMARY KEY (station_id),
    CONSTRAINT fk_as_region FOREIGN KEY (region_id) REFERENCES region(region_id),
    INDEX idx_region (region_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS forecast_data (
    id                   BIGINT AUTO_INCREMENT PRIMARY KEY,
    region               VARCHAR(50) NOT NULL,
    forecast_base_time   DATETIME NOT NULL,
    forecast_target_time DATETIME NOT NULL,
    tmp                  DECIMAL(5,1),
    wsd                  DECIMAL(5,1),
    reh                  DECIMAL(5,1),
    pcp                  DECIMAL(6,1),
    apparent_temp        DECIMAL(5,1),
    heat_index           DECIMAL(5,1),
    UNIQUE KEY uq_region_base_target (region, forecast_base_time, forecast_target_time)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS asos_history (
    id              BIGINT NOT NULL AUTO_INCREMENT,
    station_id      INT NOT NULL,
    observed_at     DATETIME NOT NULL,
    temperature     DECIMAL(5,2),
    humidity        DECIMAL(5,2),
    precipitation   DECIMAL(6,2),
    wind_speed      DECIMAL(5,2),
    wind_direction  DECIMAL(5,1),
    apparent_temp   DECIMAL(5,2),
    heat_index      DECIMAL(5,2),
    quality_flag    VARCHAR(10),
    collected_at    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uq_station_obs (station_id, observed_at),
    CONSTRAINT fk_ah_station FOREIGN KEY (station_id) REFERENCES asos_station(station_id),
    INDEX idx_observed (observed_at),
    INDEX idx_station_obs (station_id, observed_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS weather_alert (
    id                    INT NOT NULL AUTO_INCREMENT,
    brnch                 VARCHAR(30),
    wrn                   VARCHAR(5),
    lvl                   VARCHAR(5),
    cmd                   VARCHAR(5),
    ttl                   VARCHAR(200) NOT NULL,
    prsntn_tm             VARCHAR(30) NOT NULL,
    frmnt_tm              VARCHAR(30),
    tm_in                 VARCHAR(20),
    spne_frmnt_prcon_cn   TEXT,
    rlvt_zone             TEXT,
    reg_id                VARCHAR(20),
    alert_type            VARCHAR(30),
    alert_level           VARCHAR(20),
    status                VARCHAR(10) NOT NULL DEFAULT 'ACTIVE',
    collected_at          DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uq_alert (reg_id, wrn, prsntn_tm, cmd),
    INDEX idx_status (status),
    INDEX idx_reg_id (reg_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS unit (
    unit_id    VARCHAR(20) NOT NULL,
    region_id  INT NOT NULL,
    unit_name  VARCHAR(100) NOT NULL,
    PRIMARY KEY (unit_id),
    CONSTRAINT fk_unit_region FOREIGN KEY (region_id) REFERENCES region(region_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS users (
    user_id         INT NOT NULL AUTO_INCREMENT,
    unit_id         VARCHAR(20) NOT NULL,
    username        VARCHAR(20) NOT NULL,
    service_number  VARCHAR(20) NOT NULL,
    password        VARCHAR(255) NOT NULL,
    role            ENUM('admin','officer','nco','soldier') NOT NULL DEFAULT 'soldier',
    military_rank   VARCHAR(50) DEFAULT NULL,
    deleted_at      DATETIME DEFAULT NULL,
    created_at      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id),
    UNIQUE KEY uq_service_number (service_number),
    CONSTRAINT fk_users_unit FOREIGN KEY (unit_id) REFERENCES unit(unit_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS access_log (
    log_id           BIGINT NOT NULL AUTO_INCREMENT,
    user_id          INT NOT NULL,
    service_number   VARCHAR(20) NOT NULL,
    unit_id          VARCHAR(20) NOT NULL,
    ip_address       VARCHAR(64) DEFAULT NULL,
    user_agent       VARCHAR(255) DEFAULT NULL,
    session_id       VARCHAR(128) DEFAULT NULL,
    login_at         DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    logout_at        DATETIME DEFAULT NULL,
    PRIMARY KEY (log_id),
    INDEX idx_access_user (user_id, login_at),
    INDEX idx_access_sn (service_number, login_at),
    CONSTRAINT fk_access_user FOREIGN KEY (user_id) REFERENCES users(user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS audit_log (
    audit_id         BIGINT NOT NULL AUTO_INCREMENT,
    user_id          INT DEFAULT NULL,
    service_number   VARCHAR(20) DEFAULT NULL,
    action_type      VARCHAR(40) NOT NULL,
    page             VARCHAR(100) DEFAULT NULL,
    before_data      JSON DEFAULT NULL,
    after_data       JSON DEFAULT NULL,
    description      VARCHAR(255) DEFAULT NULL,
    ip_address       VARCHAR(64) DEFAULT NULL,
    device_info      VARCHAR(255) DEFAULT NULL,
    created_at       DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (audit_id),
    INDEX idx_audit_user (user_id, created_at),
    INDEX idx_audit_sn (service_number, created_at),
    INDEX idx_audit_action (action_type, created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT IGNORE INTO region (region_id, region_name, province) VALUES
    (1, '연천군', '경기도'),
    (2, '철원군', '강원도'),
    (3, '화천군', '강원도'),
    (4, '양구군', '강원도'),
    (5, '고성군', '강원도');

INSERT IGNORE INTO unit (unit_id, region_id, unit_name) VALUES
    ('HQ01', 1, '공군본부 기상단'),
    ('1BON', 1, '제1전투비행단'),
    ('2BON', 2, '제2전투비행단');

INSERT IGNORE INTO users (unit_id, username, service_number, password, role, military_rank)
VALUES ('HQ01', '관리자', '99-99999', 'acorn1234', 'admin', '대위');
