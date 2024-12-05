#######################################################################################
##    Project:      별다방조선
##    Writer:       이상민
##    Company:      조선대학교
##    Reg_date:     2024.10.14
##    Update_date:  2024.10.14
##    License:
##    Contents: 콘솔 프로그래밍을 활용한 커피 전문점에서 사용하는 키오스크

# 키오스크

# 1. 메인 메뉴 출력(커피, 스무디, 베이커리)
# 2. 메인 메뉴 선택(사용자)
# 3. 서브 메뉴 출력(커피 or 스무디 or 베이커리)
# 4. 서브 메뉴 선택(사용자)
# 5. 고객 주문 메뉴 목록에 저장(선택한 서브 메뉴)
# 6. 추가 주문 여부?(Yes, No)
# 7-1. Yes : 1번으로
# 7-2. No  : 최종부문 내역으로 보내기
# 8. 최종주문 내역 출력

from service_kiosk import *

###################
## 1. 메뉴 만들기 ##
###################

main_menu = {
    1: "커피",
    2: "스무디",
    3: "베이커리"
}
coffee_menu = {
    1: "에스프레소",
    2: "아메리카노"
}
coffee_price = {
    1: 3500,
    2: 4000
}
smoothie_menu = {
    1: "딸기 스무디",
    2: "망고 스무디",
    3: "블루베리 스무디",
    4: "키위 스무디"
}
smoothie_price = {
    1: 5500,
    2: 6000,
    3: 5500,
    4: 5000
}
bakery_menu = {
    1: "조각 케이크",
    2: "롤 케이크",
    3: "샌드위치"
}
bakery_price = {
    1: 6500,
    2: 5500,
    3: 5000
}

order_list = []  # 고객 주문 목록 [[메뉴,가격], [메뉴,가격], ... ]
while True:
    # 1. 메인 메뉴 출력
    print("★" * 50)
    print(" "*17+"★★ 별다방조선 ★★")
    print_menu(main_menu, 3)

    # 2. 메인 메뉴 선택
    order = select_menu(3)
    
    # 3. 서브 메뉴 출력
    if order == 1:      # 커피
        print_menu(coffee_menu,2)
        sub_order = select_menu(2)
        order_list.append([coffee_menu[sub_order], 
                           coffee_price[sub_order]])
    elif order == 2:    # 스무디
        print_menu(smoothie_menu,4) 
        sub_order = select_menu(4)
        order_list.append([smoothie_menu[sub_order], 
                           smoothie_price[sub_order]])
    elif order == 3:    # 베이커리
        print_menu(bakery_menu,3)
        sub_order = select_menu(3)
        order_list.append([bakery_menu[sub_order], 
                           bakery_price[sub_order]])
    
    
# 6번 추가 주문하시겠습니까? -> input()
# 결과 y/n
# y: 1번으로 이동
# n : 출력(주문 페이지로 이동합니다.)

    if not extra_order():
        # 7-2. 최종 부문 내역으로
        break
    else:
        # 7-1. 추가 주문
        continue
   
#    8. 주문 내역 출력하기 
print("★"*50)
print(" "*13 + "==== 주문 내역 ====")
total = 0
for i, item in enumerate(order_list):
    total += item[1]
    # item -> [메뉴, 가격] / item[0] : 메뉴 /  item[1] : 가격
    print(f"{i+1}.{item[0]}({item[1]}원)")  # ex) 1.아메리카노(4000원)
print(f"\n고객님이 주문하신 메뉴는 총 {len(order_list)}건으로")
print(f"결제 금액은 {total}원 입니다.")
print("이용해주셔서 감사합니다.")
