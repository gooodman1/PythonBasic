# 반복문
#  - for   : 반복 회수를 아는 경우,     예) 게시판
#  - while : 반복 횟수를 모르는 경우, 예) 키오스크
 
#  반복문(Loop)
#   - 반복적인 작업을 가능하게 해주는 도구
#   - list, str, tuple 등 컬렉션 타입의 아이템을 하나씩 순회하면서 사용(for)
#   - 특정 조건을 만족하는 경우(while)

# JAVA, C의 for
# for(int i = 0; i<10; i++){
#     실행문
# } 

# Python의 for
# for i in range() 혹은 컬렉션
# range() 혹은 컬렉션의 길이만큼 반복함.

for i in range(10):
    print(i)
    
for i in [1, 2, 3]:
    print(i)
    
# range(시작, 끝, 인터벌) : 범위 값을 만들어 줌
#  - 시작을 생략하면 0부터
#  - 인터벌을 생략하면 1
# range(1,5)   : 1, 2, 3, 4
# range(1,5,2) : 1, 3
# range(7)     : 0, 1, 2, 3, 4, 5, 6

a = ["A", "B", "C"]

# 반복횟수(인덱스)를 알고 싶은 경우 : enumerate
for i, val in enumerate(a):
    print(i, val)
    
    
# 구구단 2단 출력

for i in range(1,10):
    print(f"2x{i}={2*i}")
    
#  중첩 for문
# for i in 범위:
#     for j in 범위:
#         for k in 범위:

# 숙제: 구구단을 2단~9단까지 출력하는 코드 작성(중첩 for문 사용)
# - 반복1: 구구단 2단~9단
# - 반복2: 1~9곱셈

for j in range(2,10):
    for i in range(1,10):
        print(f"{j}x{i}={j*i}")
    print('==========')