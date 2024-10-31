# 주차 타워(엘리베이터)
#  - 5층으로 제한
#  - 1층마다 차량 1대만 입고
#  - 차량번호는 숫자 4자리

#  기능
# 1. 차량 입고
# 2. 차량 출고
# 3. 차량 조회
# 4. 종료

# 1. 공통 설정
max_car = 5  # 최대 주차 차량
cnt_car = 0  # 현재 주차되어있는 차량 수

# 2. 주차 타워 생성 -> [] -> "" (빈칸)

# tower = ["", "", "", "", "" ] # 방법1. 하드코딩(지양)

# 방법2. for문 사용
# tower = []
# for i in range(max_car):
#     tower.append("")
    
# 방법3. 리스트 컴프리헨슨
#  - 모든 for문을 리스트 컴프리헨슨으로 변경하는건 불가
tower = ["" for i in range(max_car)]

# 3. 메뉴 출력
print("=" * 50)
print("== 주차 타워 시스템 ver 1.0 ==")
print("="*50)
print("= 1. 차량입고")
print("= 2. 차량출고")
print("= 3. 차량조회")
print("= 4. 종료")
print("=" * 50)

# 4. 메뉴 선택
# 사용자로부터 1~4번까지 입력받는 코드 작성
# 사용자가 입력한 값은 select_num 변수에 저장
# 사용자가 1~4 이외의 값을 넣으면 경고메세지 출력 후 다시 입력받기
while True:
    select_num = input(">> 선택 : ")
    try:
        select_num = int(select_num)
    except:
        print(">> WARNING : 올바른 값을 입력하세요.")
        continue
        
    if select_num > 4 or select_num < 1:
        print(">> WARNING : 올바른 값을 입력하세요.")
    else:
        break 

# 5. 메뉴 서비스
# select_num이 1, 2, 3, 4인 경우
if select_num == 1:
    # 도메인 지식 -> 비즈니스 로직
    # 1. 주차공간 유무 확인
    if max_car > cnt_car:
    # y : 다음
    # 2. 차량번호 입력
    #  유효성체크(숫자, 4자리수) -> 정규식(re)
            
    # 3. 주차타워 입고(tower[])
    #   3-1. 주차타워의 비어있는 공간 검색
    #   3-2. 비어있는 공간에 값 저장
        num_car = input(">> 차량번호: ")
        for i in range(max_car):
            if tower[i] == "":
                tower[i] = num_car
    # 4. 현재 차량 수 최신화 -> cnt_car += 1
                cnt_car += 1
                break
    else:
    # n : 만차입니다. 출력
        print("만차입니다.")
    
     
elif select_num == 2:  # 숙제
    # 1. 출고 차량 번호 입력 ex) 5789
    num_car = input(">> 차량번호: ")
    # 2. 입력한 번호 존재 여부 확인
    if num_car in tower:
        pass
        # cnt_car == 0 -> "현재 주차 된 차량이 없습니다."
    #   t: 다음 스텝
    # 3. 차량 출고
    
    # 4. 현재 차량 수 최신화 -> cnt_car -= 1
    else:
    #   f: "주차되지 않은 차량번호입니다."
        print("해당 차량을 찾을 수 없습니다.")
elif select_num == 3:
    # range(시작,끝,스텝) range(0, 5, 1)   = 0,1,2,3,4
    #                    range(4, -1, -1) = 4,3,2,1,0
    for i in range(max_car-1,-1,-1):
        print(f"{i+1}층: {tower[i]}")
elif select_num == 4:
    print("프로그램을 종료합니다.")
    exit()