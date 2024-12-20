# 문자열의 이해
#  - 데이터 분석
#  - 자연어 처리
#  - 유효성 체크(사용자로부터 입력받은 값 체크)

# 1. 문자열 인덱스(index)
#  - 인덱스는 0번부터 시작
#  - 역인덱스는 -1번부터 시작
#  - 공백도 포함
intro = "Hello Python" # 인덱스(0~11) 역인덱스(-12~-1), 길이(12)

# 2. 문자 추출
print(intro[0])  # H
print(intro[-2]) # o

# 3. 문자열 슬라이싱(문자열 추출)
#  - [시작:끝]
#  - [2:5] -> 2~4
print(intro[2:7]) # 2~6
print(intro[:])   # 처음부터 끝까지
print(intro[:7])  # 처음부터 6까지
print(intro[3:])  # 3부터 끝까지

# 20240919 17:20:30

# 4. 문자열 함수
#  - len() : 문자열 길이
print(len(intro))

#  - upper(), lower() : 대소문자 변경
print(intro.upper())
print(intro.lower())

#  - replace() : 특정 문자 치환
print(intro.replace("H","J")) # "H"를 "J"로 치환

#  - split(): 구분자를 기준으로 문자열 분할(기본값: 공백)
print(intro.split())
print(intro.split("o"))

# - strip() : 문자열의 좌우공백 제거
print(intro.strip())
print("Hi" in intro)  # False

# - find() and rfind() : 문자열 내부의 특정 문자 인덱스 출력
print(intro.find("H")) # 0
print(intro.find("Python")) # 7
print(intro.find("o")) # 4, 좌 -> 우
print(intro.rfind("o")) # 10, 우 -> 좌

# 문제1. "cherry1004@gmail.com", "cherry01@gmail.com", "cherry0@gmail.com"에서
#        아이디만 추출하는 코드 작성

A = "cherry1004@gmail.com"
B = "cherry01@gmail.com"
C = "cherry0@gmail.com"

print(A[:A.find('@')])
print(B[:B.find('@')])
print(C[:C.find('@')])

# 문제2. 도메인 추출하는 코드 작성
# www.naver.com
# www.daum.net
# www.google.com
# -> naver, daum, google만 추출 

naver = "www.naver.com"
daum = "www.daum.net"
google = "www.google.com"

print(naver[4:naver.rfind('.')])
print(daum[4:daum.rfind('.')])
print(google[4:google.rfind('.')])

print(naver.split('.')[1])
print(daum.split('.')[1])
print(google.split('.')[1])