import demjson
import requests
import json

from sqlalchemy import null


def post_fre(url, data, header, fre_time):
    for i in range(int(fre_time)):
        res = requests.post(url=url, data=json.dumps(data), headers=header).json()
        #print(res)
        if res["data"] != []:
            print("data not null")
    return res


if __name__ == '__main__':
    url = "http://172.18.166.154:9005/see-dataset/api/bot/getCheckSession"

    data = {
        "checkType": 1,
        "pageSize": 100,
        "startTime": "2021-11-11 00:40:22",
        "endTime": "2021-11-27 23:39:35",
        "checkId": "4-22-1"
}

    header = {
        "X-businessId": "4",
        "Content-Type": "application/json"
    }

    print(data)
    print(header)

    res = post_fre(url=url, data=data, header=header, fre_time='20')
    # print(res)
