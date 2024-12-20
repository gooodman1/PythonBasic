# 데이터베이스 선택
USE chosun;

# 테이블 삭제
# - CASCADE(연쇄반응) + DROP = 연쇄 삭제
#      ㄴ 관련있는것을 모두 삭제
DROP TABLE IF EXISTS tbl_news CASCADE;

# 테이블 생성
# 문자열 -> CHAR, VARCHAR
# - CHAR(10)	-> |a|b|c| | |
# - VARCHAR(10) -> |a|b|c|
# 고정길이 문자열 -> CHAR
# 가변길이 문자열 -> VARCHAR

# -> VARCHAR(200) , 200 : 해당 컬럼 입력값의 최대 길이(byte).
#  영문(일반적으로 2byte), 한글(일반적으로 3byte)

# DATETIME -> 날짜(년월일시분)
# AUTO_INCREMENT -> 자동으로 count(+1) 값 입력
# PRIMARY KEY(PK) -> 테이블의 모든 값을 유일하게 식별 가능
CREATE TABLE IF NOT EXISTS tbl_news(
	id       INT AUTO_INCREMENT PRIMARY KEY,
	title	 VARCHAR(200),
	writer   VARCHAR(50),
	content  VARCHAR(10000),
	regdate  VARCHAR(50)
); 

# 테이블 조회
SELECT * FROM tbl_news;