# 변수: 하나의 값을 저장할 수 있는 메모리 공간
# 배열: 여러 값을 저장할 수 있음
#  - 동일한 자료형만 저장 가능
#  - 항상 고정된 크기를 가짐( 메모리 비효율적 ) ( 100칸 배열 생성, 2칸 사용 -> 98칸 사용X )

# 컬렉션 프레임워크
# 1. 리스트(List)
# 2. 튜플(Tuple)
# 3. 딕셔너리(Dictionary)
# 4. 세트(Set)

# * 순서가 있는 자료형: 리스트, 튜플
# * 순서가 없는 자료형: 딕셔너리, 세트

# 1. 리스트(List)
# + [] 사용
# + 정렬 가능
# + 시퀀스 자료형(인덱스 존재)
# + packing과 unpacking 가능
# + 멤버함수: append(), extend(), insert() 등등
# + mutable ( 생성 후 변경 가능)
# + 2차원 리스트는 표 형태

a = [] # 빈 리스트
b = [1, 5, 2]
c = [1, 0.2, "chosun", True, ["A", 1, False]]

["a", "b", "c"] # 리스트 Packing
a, b, c = ["a","b","c"] # 리스트 Unpacking

test = [1, 2, 3]

# 가. append(): 맨 마지막에 값 추가
test.append(4)
print(test)

# 나. insert(): 원하는 인덱스에 값 추가
test.insert(1, 99)
print(test)

# 다. extend(): 리스트 병합
a = [1, 2]
b = [2, 3]
a.extend(b)  # a를 기준으로 b를 추가
print(a)     # a 출력
 
# 라. remove(): 값으로 삭제
test.remove(2)
print(test)

# 마. pop(): 인덱스로 삭제
temp = test.pop(1) # 리스트에서 제거되지만, 값을 따로 보관하고 싶은 경우
print(test)
print(temp)

# 바. index(): 특정 값 인덱스 찾기
test.index(1)

# 사. sorted(): 정렬
# sort()   : 원본값을 정렬 ( 원본값 상실 )
# sorted() : 복제본을 정렬 ( 원본값 유지 )
# 오름차순(기본)
a = [9, 1, 3, 2, 5]
print(sorted(a))               # 오름차순(ASC)
print(sorted(a, reverse=True)) # 내림차순(DESC)

# 2. 튜플
#  + 시퀀스 자료형(인덱스 존재)
#  + packing과 unpacking 가능
#  - () 사용, 생략 가능
#  - immutable(생성 후 변경 불가) -> 멤버변수, 정렬 불가
#  - 함수의 return값 튜플

a = [1, 2, 3]  # 리스트
b = (1, 2, 3)  # 튜플
c = 1, 2, 3    # 튜플
d = (5)        # 튜플
e = 5          # 정수
f = 5,         # 튜플

# 3. 딕셔너리(Dict)
#  + JSON (데이터를 주고 받을 때 표준 포맷)
#  + Dict == JSON
#  + {key : Value} 구조(key value 1 pair)
#  + 인덱스 없음, KEY값 이용
#  + Value 중복 가능
#  + Key 중복 불가능(유니크 속성 가져야 함)
#  + value는 key로만 접근 가능

member = {
    "id" : "test1234",
    "pw" : "4321tset"
}

#   가. 조회
print(member["id"])
print(member.get("id"))

# print(member["name"])  # ERROR
print(member.get("name"))  # None

#   나. 추가 및 변경
member["name"] = "이상민"  # 추가
member["id"] = "test"  # 변경
print(member)

#   다. 삭제
member.pop("name")

#   라. 병합
# a를 기준으로 b를 추가
# 중복 key가 있는 경우 매개변수로 전달한 값을 overwrite
a = {"a":1, "b":2}
b = {"b":99, "c":3, "d":4}
a.update(b)
print(a)

#   마. in
print("id" in member)  # True
print("phone" in member)  # False

#   바. Value Access
print(member.keys())
print(member.values())
print(member.items())

# 4. 세트(Set)
#  + 수학에서 집합과 동일한 개념
#  + 합집합, 교집합, 부분집합, 차집합 가능
#  + 인덱스 없음
#  + {} 사용
#  + 중복값을 혀용 X -> 값으로 호출

a = {1, 2, 3, 3, 4, 4, 5}
print(a)

c = {}  # Dict

a = [1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]
# 중복값을 제거할 때
print(a)
print(set(a))
print(list(set(a)))

# 숙제
a = 10
b = 50

# 코드 작성
a, b = b, a

# tmp = a
# a = b
# b = tmp


print(a)  # 50 출력
print(b)  # 10 출력