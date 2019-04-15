"""
Upbit 시세 종목 조회 참조
https://docs.upbit.com/v1.0.2/reference#%EC%8B%9C%EC%84%B8-%EC%A2%85%EB%AA%A9-%EC%A1%B0%ED%9A%8C
업비트에서 거래 가능한 마켓 목록 업데이트 하는 프로세스
Quotation API 사용
"""

import requests

url = "https://api.upbit.com/v1/market/all"

response = requests.request("GET", url)

print(response.text)