import urllib3
import requests
import json

url = "http://wsxf.ahxfj.gov.cn/pl-ws-web/wantInquire/caseSearchList.do?navIndex=5-3&code="
repsonse1 = requests.get(url)
data = repsonse1.text
print(data)
with open("data.txt", "w", encoding="utf-8") as file:
    file.write(data)
