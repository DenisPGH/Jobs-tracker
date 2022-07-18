import requests
from bs4 import BeautifulSoup as soup
import re
import time
pattern=r'<a aria-label="(?P<title>([^@]+))" class="jcs-JobTitle css-jspxzf eu4oa1w0"[^@]+ class="companyLocation">(?P<location>([^@]+)), [^@]+'

cookies = {
    'CTK': '1frd7g1fur89n800',
    'OptanonAlertBoxClosed': '2022-02-08T17:53:59.920Z',
    '_ga': 'GA1.2.760069551.1644342841',
    '__ssid': '562fcfa815b5eb818951694549bbfcc',
    'SOCK': '"ffGX4XivAKwKhVodu1r1AAtPXWs="',
    'SHOE': '"R9BdUROJhQ_l7cEcixm1nk5MA4e16R3Y7AesTbhme7KNa4PCJsoYmLTUOWgp-xd0X3R2M4KEePKfjq606NSCY819S-c-qf6RFsvN41eNDc71a9OYWDFaq-SDeHvJ2d41PJC5agdOAXbYQw=="',
    '_gcl_au': '1.1.1657837122.1652794718',
    # 'CO': 'CH',
    # 'LOCALE': 'en',
    'pjps': '1',
    'RF': '"q2avyVql9o-cBmrvvmPxu085701jUWdhZgOj7zZyhguFdVdIA_spbAsIbLtCg6i2cYiNmUxrVt1yoc8V37_QpW_12ML1zXimwd2LbJTedKjJQLsMN8tcBpqYNZrfOvvGpLQyEAGXp9wZo8IddBOTdRWxVc_Cg82uvHQeQqgJwlTxF9DuY_B-oKJ9m8uE49SgNIWtQv-WGeJj-4GkGBqiUrIQsgQAd24BsZaoRi3a-Q-cAt3FbnGbKrj5FBNZhVrMQU0uqqvrBYR8ipRQvLjr_tVPvsE5AUb94qdWMB12Ck-LtkW4-P3muAmwXlIPmwbEkwfonuEMtUGzEXELDuzUY7aqJtJlsIiUssoz8pQ8cn0="',
    'LC': 'co=CH&hl=en',
    'CO': 'CH',
    'LOCALE': 'en',
    'CSRF': 'WVLg0uAVdUuFIcCoSIUK4N9bL6djem7u',
    'INDEED_CSRF_TOKEN': 'A33d8kUG7gEo8NTQH7dQY5bDm5djwrwT',
    'LV': '"LA=1655183169:LV=1654502723:CV=1655183169:TS=1652794716"',
    'UD': '"LA=1655183169:LV=1654502723:CV=1655183169:TS=1652794716"',
    'indeed_rcc': '"LOCALE:PREF:LV:CTK:CO:RQ:UD"',
    'CMP_VISITED': '1',
    'SHARED_INDEED_CSRF_TOKEN': 'A33d8kUG7gEo8NTQH7dQY5bDm5djwrwT',
    'PREF': '"TM=1658143951797:L=Bern%2C+BE"',
    'MICRO_CONTENT_CSRF_TOKEN': 'VJY8ACuOnzDKGXzLw72gsaz7FyjYK3U7',
    'jobAlertPopoverShown': '1',
    'RQ': '"q=&l=Bern%2C+BE&ts=1658143984976:q=software+engineer&l=Z%C3%BCrich%2C+ZH&ts=1655183169834:q=&l=Schweiz&ts=1654505612887:q=Python&l=&ts=1654367379298&pts=1652795493370:q=Solar+Montage&l=&ts=1653931717867:q=Python&l=Schweiz&ts=1652797611513"',
    'ac': 'avC6MAaNEe2vuOWy6sZdcA#avIZwAaNEe2vuOWy6sZdcA',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Mon+Jul+18+2022+14%3A33%3A17+GMT%2B0300+(Eastern+European+Summer+Time)&version=6.37.0&geolocation=%3B&isIABGlobal=false&hosts=&consentId=f48cd989-ec6b-4a18-8faa-c568eb5289ec&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0%2CC0007%3A0&AwaitingReconsent=false',
    'PPID': 'eyJraWQiOiI2YmQ2MjM1MS0wZGM5LTQxNmUtOGQzOS02NTY2MjNiNjQ0YjEiLCJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJzdWIiOiJlMmZlYzNlYjZlMTMxODIzIiwiYXVkIjoiYzFhYjhmMDRmIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImNyZWF0ZWQiOjE1MTMyNzYyOTQwMDAsInJlbV9tZSI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL3NlY3VyZS5pbmRlZWQuY29tIiwiZXhwIjoxNjU4MTQ1NzkxLCJpYXQiOjE2NTgxNDM5OTEsImxvZ190cyI6MTY0NDM0MzExNDg5NSwiZW1haWwiOiJkZW5pXzkwMDBfMTk5MEBhYnYuYmcifQ.HWMgdnZI0a5zq3_c3ZG4gWu8u5qor_A-9hktW-BCCZYVhrYKOHWx-ZVD8yMLBgYE2EtMoy-JEF3ffgMOCIZ4cg',
    'JSESSIONID': 'A55CC15CBD08EE155516C684EDC1C937',
    'PTK': '"tk=1g88haj8ajv6v800&type=jobsearch&subtype=pagination&fp=1"',
}

headers = {
    'authority': 'ch.indeed.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'CTK=1frd7g1fur89n800; OptanonAlertBoxClosed=2022-02-08T17:53:59.920Z; _ga=GA1.2.760069551.1644342841; __ssid=562fcfa815b5eb818951694549bbfcc; SOCK="ffGX4XivAKwKhVodu1r1AAtPXWs="; SHOE="R9BdUROJhQ_l7cEcixm1nk5MA4e16R3Y7AesTbhme7KNa4PCJsoYmLTUOWgp-xd0X3R2M4KEePKfjq606NSCY819S-c-qf6RFsvN41eNDc71a9OYWDFaq-SDeHvJ2d41PJC5agdOAXbYQw=="; _gcl_au=1.1.1657837122.1652794718; CO=CH; LOCALE=en; pjps=1; RF="q2avyVql9o-cBmrvvmPxu085701jUWdhZgOj7zZyhguFdVdIA_spbAsIbLtCg6i2cYiNmUxrVt1yoc8V37_QpW_12ML1zXimwd2LbJTedKjJQLsMN8tcBpqYNZrfOvvGpLQyEAGXp9wZo8IddBOTdRWxVc_Cg82uvHQeQqgJwlTxF9DuY_B-oKJ9m8uE49SgNIWtQv-WGeJj-4GkGBqiUrIQsgQAd24BsZaoRi3a-Q-cAt3FbnGbKrj5FBNZhVrMQU0uqqvrBYR8ipRQvLjr_tVPvsE5AUb94qdWMB12Ck-LtkW4-P3muAmwXlIPmwbEkwfonuEMtUGzEXELDuzUY7aqJtJlsIiUssoz8pQ8cn0="; LC=co=CH&hl=en; CO=CH; LOCALE=en; CSRF=WVLg0uAVdUuFIcCoSIUK4N9bL6djem7u; INDEED_CSRF_TOKEN=A33d8kUG7gEo8NTQH7dQY5bDm5djwrwT; LV="LA=1655183169:LV=1654502723:CV=1655183169:TS=1652794716"; UD="LA=1655183169:LV=1654502723:CV=1655183169:TS=1652794716"; indeed_rcc="LOCALE:PREF:LV:CTK:CO:RQ:UD"; CMP_VISITED=1; SHARED_INDEED_CSRF_TOKEN=A33d8kUG7gEo8NTQH7dQY5bDm5djwrwT; PREF="TM=1658143951797:L=Bern%2C+BE"; MICRO_CONTENT_CSRF_TOKEN=VJY8ACuOnzDKGXzLw72gsaz7FyjYK3U7; jobAlertPopoverShown=1; RQ="q=&l=Bern%2C+BE&ts=1658143984976:q=software+engineer&l=Z%C3%BCrich%2C+ZH&ts=1655183169834:q=&l=Schweiz&ts=1654505612887:q=Python&l=&ts=1654367379298&pts=1652795493370:q=Solar+Montage&l=&ts=1653931717867:q=Python&l=Schweiz&ts=1652797611513"; ac=avC6MAaNEe2vuOWy6sZdcA#avIZwAaNEe2vuOWy6sZdcA; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Jul+18+2022+14%3A33%3A17+GMT%2B0300+(Eastern+European+Summer+Time)&version=6.37.0&geolocation=%3B&isIABGlobal=false&hosts=&consentId=f48cd989-ec6b-4a18-8faa-c568eb5289ec&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0%2CC0007%3A0&AwaitingReconsent=false; PPID=eyJraWQiOiI2YmQ2MjM1MS0wZGM5LTQxNmUtOGQzOS02NTY2MjNiNjQ0YjEiLCJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJzdWIiOiJlMmZlYzNlYjZlMTMxODIzIiwiYXVkIjoiYzFhYjhmMDRmIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImNyZWF0ZWQiOjE1MTMyNzYyOTQwMDAsInJlbV9tZSI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL3NlY3VyZS5pbmRlZWQuY29tIiwiZXhwIjoxNjU4MTQ1NzkxLCJpYXQiOjE2NTgxNDM5OTEsImxvZ190cyI6MTY0NDM0MzExNDg5NSwiZW1haWwiOiJkZW5pXzkwMDBfMTk5MEBhYnYuYmcifQ.HWMgdnZI0a5zq3_c3ZG4gWu8u5qor_A-9hktW-BCCZYVhrYKOHWx-ZVD8yMLBgYE2EtMoy-JEF3ffgMOCIZ4cg; JSESSIONID=A55CC15CBD08EE155516C684EDC1C937; PTK="tk=1g88haj8ajv6v800&type=jobsearch&subtype=pagination&fp=1"',
    'referer': 'https://ch.indeed.com/jobs?q&l=Bern%2C%20BE&vjk=b68961277a54e754',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

params = {
    'q': '',
    'l': 'Bern, BE',
    'start': '0', # ot koq pochwa 0-1,10-2,20-3,30-4str
    'pp': 'gQAPAAAAAAAAAAAAAAAB3YkJSAAuAQAZ7zv6Ed1n2nD4EsybaOjp04wd_5vdPtAirO0Aal-kXLZ5nG5stUtr7pW6kgAA',

}

response = requests.get('https://ch.indeed.com/jobs', params=params, cookies=cookies, headers=headers)

#print(response.text)
html=soup(response.text,'html.parser')
all_jobs=html.select('.job_seen_beacon') # return a list
alll_jobs=html.select('.resultContent') # return a list
#allll_jobs=html.select('.jobTitle jobTitle-newJob css-bdjp2m eu4oa1w0') # return a list
#print(all_jobs)
#print(alll_jobs[0])
for each_job in alll_jobs:
    title=''
    place=''
    found=re.finditer(pattern,str(each_job))
    for info in found:
        title=info.group('title')
        place=info.group('location')
    print(f'{title}=={place}')


# https://ch.indeed.com/+ linka ot faila
