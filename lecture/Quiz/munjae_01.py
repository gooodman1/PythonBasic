#문제1. "cherry1004@gmail.com", 
#       "cherry01@gmail.com",
#       "cherry0@gmail.com" 에서
#       아이디만 추출하는 코드 작성

# 문제2. 도메인 추출하는 코드 작성
# www.naver.com
# www.daun.net
# www.google.com
# -> naver, aun, google만 추출

intro_1 = "cherry1004@gmail.com"
intro_2 = "cherry01@gmail.com"
intro_3 = "cherry0@gmail.com"
print(intro_1.split("@")[0])
print(intro_2.split("@")[0])
print(intro_3.split("@")[0])


# print(intro_1[0:10])
# print(intro_2[0:8])
# print(intro_3[0:7])

in_1 = "www.naver.com"
in_2 = "www.daun.net"
in_3 = "www.google.com"

print(in_1.split(".")[1])
print(in_2.split(".")[1])
print(in_3.split(".")[1])

# print(in_1[4:19])
# print(in_2[4:8])
# print(in_3[4:10])