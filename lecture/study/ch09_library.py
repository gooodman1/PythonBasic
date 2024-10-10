# 라이브러리(Library), 패키지(Package), 모듈(Module)
#  - 라이브러리 >= 패키지 >= 모듈
#  - 라이브러리(내부, 외부, 사용자 정의)

#  - 모듈(.py 1개)  ex) ch09_library.py
#  - 패키지         ex) study
#  - 라이브러리     ex) lecture


#  ** 라이브러리 사용 방법
#  1. 다운로드(아나콘다 pip install ~)
#  2. 불러오기(import 라이브러리)
#  3. 사용하기(라이브러리.모듈())

#  **import 
#  1. import 라이브러리
#   ex) import requests
#     → requests 라이브러리 모든 기능을 불러오기
#     → 사용법: requests.get()

#  2. from 라이브러리 import 모듈
#   ex) from requests import get, post
#     → get, post 모듈만 불러오기
#     → 사용법: get(), post()

#  * as(Alias: 별명)
#   ex) import Beautifulsoup as bs4
#     → Beautifulsoup을 bs4로 부르자!
#     → 사용법: bs4.select()
