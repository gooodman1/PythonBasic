# 절차지향 프로그래밍(C언어)
#  + 함수를 만들고 순차적으로 프로그램이 동작하는 방식
#  + file 1개에 모든 코드를 넣고 위에서부터 아래로 실행
#  + 함수 호출     함수 정의
#    함수 정의     함수 호출
#      (X)           (O)
#  + 객체나 클래스 없이 바로 개발 가능(개발 속도 ↑)
#  + 코드 재사용과 유지보수가 어려움(비용 ↓)

# 객체지향 프로그래밍(Java,Python)
#  + 함수가 어디있든지 간에 객체를 사용해서 호출 가능
#  + 객체나 클래스를 사용하기 때문에 많은 양의 메모리가 필요하며
#    설계하는데 시간이 오래 걸림.
#  + 코드 재사용과 유지보수가 용이

# Class
# + 객체 설계 도면

# Object(객체)
# + Class로 생성된 구체화된 객체 -> 인스턴스
# + *** (매우 중요) 파이썬의 모든 것은 객체(인스턴스)

# ○ 기본자료형(프리미티브 타입)  : 변수에 실제 값이 저장
# ○ 객체자료형(레퍼런스 타입)    : 변수에 실제 값이 위치한 주소 저장
# C : 기본
# JAVA : 기본 + 객체
# Python : 객체
# ※ NULL : 참조할 대상이 없는 경우.

a = 4
b = a
print(id(a))  # id() : 값의 주소 출력

# 프로그래밍 언어 메모리 영역
# - Stack, Heap, Data, Code ... 

#  ** 객체 사용 3단계 **
# 1. Class(도면) -> 2. 객체 생성 -> 3. 인스턴스(결과물), 인스턴스 사용

# 1. Class 작성
#  파스칼 표기법 사용
#  멤버함수는 첫 번째 인자로 반드시 self를 사용
# self: 인스턴스(결과물) 자기 자신
class ChosunTest:
    def print_name(self):
        print("초롱")

# 2. 객체 생성
# + () 붙어있으면 함수 -> 스네이크 표기법
# + 생성자 함수() -> 예외적으로 클래스 이름과 동일
# + class에 생성자 함수를 생략하면 디폴트 생성자 함수 자동 생성
# + class가 동일하더라도 생성된 인스턴스는 각각 다름

test1 = ChosunTest()
test2 = ChosunTest()
test3 = ChosunTest()

# 3. 객체 사용
test1.print_name()

# 객체를 사용하면 좋은 점
# 1. 상속
class Parent:
    def print_star(self):
        print("★")
        
class Child(Parent):
    pass

ch = Child()
ch.print_star()

# 이론: class 어떻게 만들어야 할까?
#  -> 객체 모델링
#  모델링 : 현실세계를 컴퓨터 세계로 구현

# 현실세계
# 아이디, 이름, 나이를 입력하면 회원가입을 할 수 있다.

# 컴퓨터 세계
class Member:
    # 필드(변수)
    id = "abc"
    name = "이상민"
    age = 22
    # 멤버함수
    def member_join(self, id, name, age):
        print("회원가입을 한다.")

mem = Member()
mem.member_join("def", "홍길동", 10)