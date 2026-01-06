create database my_diary_db;

USE my_diary_db;

CREATE USER 'md_user1'@'%' IDENTIFIED BY '비밀번호1191';

-- 2. my_diary_db 데이터베이스에 대한 모든 권한을 md_user1에게 줍니다.
GRANT ALL PRIVILEGES ON my_diary_db.* TO 'md_user1'@'%';

-- 3. 변경된 권한 설정을 즉시 적용합니다.
FLUSH PRIVILEGES;