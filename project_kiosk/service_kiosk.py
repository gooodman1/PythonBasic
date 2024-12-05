# 메뉴 출력
def print_menu(menu : dict, menu_cnt: int):
    print("★"*50)
    for i in range(1,menu_cnt+1):
        print(f"★★  {i}. {menu[i]}")

# 메뉴 선택 
def select_menu(menu_cnt: int) -> int:
    while True:
        order = int(input(">> 메뉴: "))
        if order > menu_cnt or order < 1:
            print(">> WARNING: 올바른 번호를 입력해주세요.")
        else:
            break
    return order

def extra_order() -> bool:
    while True:    
        extra_order = input(">> MSG: 추가로 주문하시겠습니까? (Y/N) : ").strip().lower()
        if extra_order == "y":
            return True
        elif extra_order == 'n':
            return False
        else:
            print(">> WARNING: 올바른 값을 입력해주세요.")