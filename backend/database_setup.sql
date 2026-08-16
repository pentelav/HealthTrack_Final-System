-- Designed HealthTrack database design with tables for user, health record, alert, risk history and report.
-- Inserted sample data for healthcare and controlled relationships in the tables with database creation commands.

-- Removing existing database
DROP DATABASE IF EXISTS HealthTrackDB;


-- Creating HealthTrack database
CREATE DATABASE HealthTrackDB;


-- Selecting HealthTrack database
USE HealthTrackDB;



-- Creating users table
CREATE TABLE users (

    id INT AUTO_INCREMENT PRIMARY KEY,

    username VARCHAR(100)
        UNIQUE NOT NULL,

    password VARCHAR(255)
        NOT NULL,

    role VARCHAR(50)
        DEFAULT 'Patient',

    created_at DATETIME
        DEFAULT CURRENT_TIMESTAMP

);



-- Creating health records table
CREATE TABLE health_records (

    id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT NOT NULL,

    heart_rate INT,

    oxygen FLOAT,

    temperature FLOAT,

    blood_pressure VARCHAR(20),

    created_at DATETIME
        DEFAULT CURRENT_TIMESTAMP,


    -- Connecting user records
    CONSTRAINT fk_health_user

    FOREIGN KEY(user_id)

    REFERENCES users(id)

    ON DELETE CASCADE

);



-- Creating alerts table
CREATE TABLE alerts (

    id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT NOT NULL,

    alert_type VARCHAR(100),

    severity VARCHAR(50),

    message TEXT,

    status VARCHAR(50)
        DEFAULT 'Unread',

    created_at DATETIME
        DEFAULT CURRENT_TIMESTAMP,


    -- Connecting alert records
    CONSTRAINT fk_alert_user

    FOREIGN KEY(user_id)

    REFERENCES users(id)

    ON DELETE CASCADE

);



-- Creating risk history table
CREATE TABLE risk_history (

    id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT,

    risk_score FLOAT,

    risk_level VARCHAR(50),

    prediction VARCHAR(100),

    created_at DATETIME
        DEFAULT CURRENT_TIMESTAMP,


    -- Connecting risk records
    CONSTRAINT fk_risk_user

    FOREIGN KEY(user_id)

    REFERENCES users(id)

    ON DELETE CASCADE

);



-- Creating reports table
CREATE TABLE reports (

    id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT,

    report_title VARCHAR(200),

    report_content TEXT,

    created_at DATETIME
        DEFAULT CURRENT_TIMESTAMP,


    -- Connecting report records
    CONSTRAINT fk_report_user

    FOREIGN KEY(user_id)

    REFERENCES users(id)

    ON DELETE CASCADE

);



-- Adding sample user data
INSERT INTO users

(
username,
password,
role
)

VALUES

(
"admin",
"$2b$12$hashedpassword",
"Administrator"
),

(
"patient1",
"$2b$12$hashedpassword",
"Patient"
);



-- Adding sample health record
INSERT INTO health_records

(
user_id,
heart_rate,
oxygen,
temperature,
blood_pressure
)

VALUES

(
2,
78,
98,
36.7,
"120/80"
);



-- Adding sample alert record
INSERT INTO alerts

(
user_id,
alert_type,
severity,
message
)

VALUES

(
2,
"Heart Rate",
"Low",
"Patient monitoring started"
);



-- Adding sample risk record
INSERT INTO risk_history

(
user_id,
risk_score,
risk_level,
prediction
)

VALUES

(
2,
25,
"Low Risk",
"Healthy"
);



-- Adding sample report record
INSERT INTO reports

(
user_id,
report_title,
report_content
)

VALUES

(
2,
"Initial Health Report",
"Patient health report generated successfully"
);