# 문제: 피보나치 수열을 계산하는 코드를 작성하세요.

#   - 조건

#     1. 파이썬 프로그래밍 언어를 사용하세요.

#     2. 라이브러리를 사용하지말고 순수 파이썬 문법만 사용하세요.

#     3. 제출은 작성한 코드를 복사 붙여넣기 해서 제출하세요.(파일로 제출하지 마세요.)

 

#   - 내용

#     1. 피보나치 수열은 "0 1 1 2 3 5 8 13 ..."과 같이 앞의 두 수를 더해서 다음수가 계산되는 수열입니다.

#     2. 사용자가 max_num을 입력하면 해당 값까지 출력되야 합니다.

#        ex) max_num=5 → 출력 "0 1 1 2 3 5"

#     3. 다음 주어진 변수와 값을 반드시 사용하세요.

    

#     # 다음 변수와 값을 반드시 코드에 사용하세요. 

#     front = 0   

#     end = 1     

 

#   ※ print()를 활용한 출력을 가로로 나오게 하고 싶으면

#       print(값, end=" ")을 사용하면 가로로 출력이 됩니다.

#      ex) print(0, end= " ")

#            print(1, end= " ")



max_num = int(input("max_num="))
front = 0
end = 1

check = [front, end, front+end]
i = 2
while check[i] <= max_num:
    check.append(check[i] + check[i-1])
    i += 1
if not max_num in check:
    print(f"{max_num} is not in the Fibonacci Sequence.")
    print(f"max_num smaller than {max_num} is {check[i-1]}")

while front <= max_num:
    print(front,end=" ")
    front, end = end, front + end