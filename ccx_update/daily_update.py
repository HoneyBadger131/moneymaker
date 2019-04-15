
"""
Upbit 시세 종목 조회 참조
https://docs.upbit.com/v1.0.2/reference#%EC%8B%9C%EC%84%B8-%EC%A2%85%EB%AA%A9-%EC%A1%B0%ED%9A%8C
업비트에서 거래 가능한 마켓 목록 업데이트 하는 프로세스
Quotation API 사용
"""

import requests
from sqlalchemy import create_engine
import json


engine = create_engine('mysql://moneymaker:moneymaker$$@moneymaker.cgzbexb5lqid.us-east-2.rds.amazonaws.com:3306/moneymaker')
cur = engine.connect()

url = "https://api.upbit.com/v1/market/all"
response = requests.request("GET", url)
res = response.json()


for i in res:
    sqltext = """
    replace ccx_ticker_master(market, korean_name, english_name) values('{:market}','{:korean_name}','{:english_name}');
    """
    sqltext = sqltext.replace('{:market}',i['market'])
    sqltext = sqltext.replace('{:korean_name}',i['korean_name'])
    sqltext = sqltext.replace('{:english_name}',i['english_name'])

    cur.execute(sqltext)