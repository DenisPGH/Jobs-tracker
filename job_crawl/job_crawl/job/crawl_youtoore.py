import json

import requests

cookies = {
    'ARRAffinity': '136db78527ad94c9c44b111bf671d4b0183d9fa7e3f379d4d3855475997ea8ef',
    'ARRAffinitySameSite': '136db78527ad94c9c44b111bf671d4b0183d9fa7e3f379d4d3855475997ea8ef',
    'JSESSIONID': 'A655367481705BFD7D2302472A3F1AE8',
}

headers = {
    'authority': 'www.yootureapp.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'de',
    'authorization': 'Bearer eyJjdHkiOiJKV1QiLCJlbmMiOiJBMTI4R0NNIiwiYWxnIjoiZGlyIn0.._cpQ6uYC8BVuwEBH.WArSuOWM8YGRuK4stxwk-VKaU4wacx-_urgJacG8iev02VqBJzLoAEYzRL8KbrU1QEXJPn4XGrOAhzVobotqAD0jEIvPbZd_ibS41pSjUTOux2L20XK_4WFdf-KXvHTogbOBlElDxSDQqJNWaJOpMWZQOW-ejHunJJJ14fMCs7XODCbZyXhb-W7w_GdSj0jEYNN5k_5gZ78rNKbzRcXHFguQRjw6LB1H6OZl1l9GcmSrCz3UKgSUPswJjhYC5tIlGBaYwaBriuxfsR3lOhL18IaudimzeftHXQg8q7dfQLE8zzPkTAAh-jqioDMsUEYrS1WzIOCOxgc844ToGhOA2gkKvbxy0MqwK2NpOClzfza6OqShH_yezGt5Hi_2jitCRLZr06PHpY-8NKvc2mjGJ5jOP0N3oBeJkTP0aY0hZ_M61WtVwFGpa7RaCzYHdEqt8OV42KNU0hepdrQqjiGrBXfFq4EKqZ9CWnvuHn6qwAU_I6cW96YejQml1MutDQo3f6T24c-scl0nvSoi4_ipFiRWPMYFtOWoAOpDVoV9v3gJEj9cV3j8oax-8IBtyN0vx8SZGQwO7URKOi2acNZMxRoY_L2w.tlXUNzz4ZDUBZ4aKP7d8uQ',
    'content-type': 'application/json;charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'ARRAffinity=136db78527ad94c9c44b111bf671d4b0183d9fa7e3f379d4d3855475997ea8ef; ARRAffinitySameSite=136db78527ad94c9c44b111bf671d4b0183d9fa7e3f379d4d3855475997ea8ef; JSESSIONID=A655367481705BFD7D2302472A3F1AE8',
    'origin': 'https://www.yootureapp.com',
    'referer': 'https://www.yootureapp.com/ui/candidates/searchvacancies',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
    'x-supportsjobdescriptionformatted': 'true',
}

json_data = {
    'searchTerm': 'bern',
    'filters': {
        'location': {
            'regionCodes': [],
            'locationSearchType': 'REGION',
            'location': None,
            'radius': 60,
        },
        'workQuota': {
            'min': 0,
            'max': 100,
        },
    },
    'page': 0,
    'pageSize': 10,
    'sortType': 'RELEVANCE',
}

response = requests.post('https://www.yootureapp.com/api/v2.0/users/vacancies/search', cookies=cookies, headers=headers, json=json_data)
result=json.loads(response.text)
company=result['vacancies'][0]['company']['ident']
title=result['vacancies'][0]['jobTitle']
date=result['vacancies'][0]['createTime'].split('T')[0]
link=result['vacancies'][0]['yootureUrl']

#print(result['vacancies'][0])
print(company,title,date,link)