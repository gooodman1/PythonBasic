import requests
from bs4 import BeautifulSoup

#  1. URL 설정
#  - 수집하고 싶은 웹사이트 설정
url = "https://v.daum.net/v/20241028164052926"

# 2. 전체 소스코드 가져오기
#  - 상태코드
#    200(성공)
#    400~(클라이언트 오류)
#    500~(서버 오류)

result = requests.get(url)
print(result)
# print(result.text)

# 3. BS가 읽을 수 있도록 전체 소스코드 파싱
doc = BeautifulSoup(result.text, "html.parser")

# 4. 웹 크롤링
# - select() -> list
title = doc.select("h3.tit_view")[0].get_text()

contents = doc.select("section > p")  #  [<p>본문1</p>, <p>본문2</p>]
content = ""
for text in contents:
    content += text.get_text()



print("="*50)
print(f"뉴스 제목 : {title}")
print("="*50)
print(f"뉴스 본문 : {content}")