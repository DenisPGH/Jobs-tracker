
from datetime import datetime as dt
import datetime
import requests
from asgiref.sync import sync_to_async
from bs4 import BeautifulSoup as soup
import re
import time

from job_crawl.job.helper import wished_works, speak_function, CounterJobs
from job_crawl.job.models import  Job

pattern=r'<a aria-label="(?P<title>([^@]+))" class="jcs-JobTitle css-jspxzf eu4oa1w0"[^@]+ href="(?P<href>([^@]+role="button"))[^@]+ class="companyLocation">(?P<location>([^@]+)),'








def indeed_ch():
    start = time.time()
    cookies = {
        'CTK': '1frd7g1fur89n800',
        'OptanonAlertBoxClosed': '2022-02-08T17:53:59.920Z',
        '_ga': 'GA1.2.760069551.1644342841',
        '__ssid': '562fcfa815b5eb818951694549bbfcc',
        'SOCK': '"ffGX4XivAKwKhVodu1r1AAtPXWs="',
        'SHOE': '"R9BdUROJhQ_l7cEcixm1nk5MA4e16R3Y7AesTbhme7KNa4PCJsoYmLTUOWgp-xd0X3R2M4KEePKfjq606NSCY819S-c-qf6RFsvN41eNDc71a9OYWDFaq-SDeHvJ2d41PJC5agdOAXbYQw=="',
        '_gcl_au': '1.1.1657837122.1652794718',
        'pjps': '1',
        'RF': '"q2avyVql9o-cBmrvvmPxu085701jUWdhZgOj7zZyhguFdVdIA_spbAsIbLtCg6i2cYiNmUxrVt1yoc8V37_QpW_12ML1zXimwd2LbJTedKjJQLsMN8tcBpqYNZrfOvvGpLQyEAGXp9wZo8IddBOTdRWxVc_Cg82uvHQeQqgJwlTxF9DuY_B-oKJ9m8uE49SgNIWtQv-WGeJj-4GkGBqiUrIQsgQAd24BsZaoRi3a-Q-cAt3FbnGbKrj5FBNZhVrMQU0uqqvrBYR8ipRQvLjr_tVPvsE5AUb94qdWMB12Ck-LtkW4-P3muAmwXlIPmwbEkwfonuEMtUGzEXELDuzUY7aqJtJlsIiUssoz8pQ8cn0="',
        'CO': 'CH',
        'LOCALE': 'en',
        'CMP_VISITED': '1',
        'RSJC': '50a565615e400018',
        'cmppmeta': '"eNoBSAC3/4yH20+g5Ls42gAe2e9fZSPEYpuCyTe6KDHp/UnXTc7luLgnNPUJ7bmbNzuvHjCekX2QMsJiwiQML+xL6wXhEYXK6u+Y49lbGnIMJe4="',
        'indeed_rcc': '"LOCALE:PREF:cmppmeta:LV:CTK:CO:RQ:UD"',
        'JATG': 'control',
        'CSRF': 'lYUujyZceNuXxKvMxx6IOgbaqNiTa2pK',
        'INDEED_CSRF_TOKEN': 'Utdorb8vbL3RIyce4d09rS32sGRDoa2U',
        'LV': '"LA=1658154367:LV=1655183169:CV=1658143951:TS=1652794716"',
        'UD': '"LA=1658154367:LV=1655183169:CV=1658143951:TS=1652794716"',
        '__cf_bm': 'Lsr0VsHpaM6SZCHYundIY3xevv9tif2jDfXNnAuL98o-1660150449-0-Afj4n2hpvYeEGG1issQZIu0Zd4o0eE83MJShARGIs0LtWBLRrKHAlejn4L5QZLi8O2WoG/ewaEgGOwV+vmSARzA=',
        '_cfuvid': 'krt5igfMgYu78MY7fhI_WCfUkgLW6vEqjfPvt.5XP48-1660150449326-0-604800000',
        'SHARED_INDEED_CSRF_TOKEN': 'Utdorb8vbL3RIyce4d09rS32sGRDoa2U',
        'MICRO_CONTENT_CSRF_TOKEN': 'ywsX8WsaShLwF8TOzRSpOfqiGcQ87M9M',
        'PREF': '"TM=1660150541333:L=Schweiz"',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Aug+10+2022+18%3A55%3A43+GMT%2B0200+(Central+European+Summer+Time)&version=6.37.0&geolocation=%3B&isIABGlobal=false&hosts=&consentId=f48cd989-ec6b-4a18-8faa-c568eb5289ec&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0%2CC0007%3A0&AwaitingReconsent=false',
        'LC': '"co=CH"',
        'PPID': 'eyJraWQiOiI3YmYwYzJmMy05OTdmLTQyNGItOWQ4Yi1hZmMzZWEwZmUwMGMiLCJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJzdWIiOiJlMmZlYzNlYjZlMTMxODIzIiwiYXVkIjoiYzFhYjhmMDRmIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImNyZWF0ZWQiOjE1MTMyNzYyOTQwMDAsInJlbV9tZSI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL3NlY3VyZS5pbmRlZWQuY29tIiwiZXhwIjoxNjYwMTUyMzQ0LCJpYXQiOjE2NjAxNTA1NDQsImxvZ190cyI6MTY0NDM0MzExNDg5NSwiZW1haWwiOiJkZW5pXzkwMDBfMTk5MEBhYnYuYmcifQ.MWM_4JibgXlXWhyaDJTtLlpKS5OADphi65aqz9JYeYiOV0vU8oqodZbY5sVInR0PZB0la3uDZHWQxwCFD_0xsQ',
        '_dd_s': 'rum=0&expire=1660151443516',
        'RQ': '"q=&l=Schweiz&ts=1660150562846&pts=1654505612887:q=Masseur&l=Bern%2C+BE&ts=1660150509011:q=Masseur&l=&ts=1660150495271:q=&l=Bern%2C+BE&ts=1658149689640:q=Betreuung+Kinder&l=Bern%2C+BE&ts=1658149096115:q=babysitter&l=Bern%2C+BE&ts=1658149004864:q=babysitter&l=stadt+bern&ts=1658148992467:q=babysitter&l=3000&ts=1658148930149:q=software+engineer&l=Z%C3%BCrich%2C+ZH&ts=1655183169834:q=Python&l=&ts=1654367379298&pts=1652795493370"',
        'JSESSIONID': 'BB464DBA22C4FFA5F5AA062A431735DC',
    }
    counter_pages=1
    today = str(dt.today()).split(' ')[0]
    yesterday = str(dt.today() - datetime.timedelta(days=1)).split(" ")[0]
    prefix='https://ch.indeed.com'

    while True:
        headers = {
            'authority': 'ch.indeed.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            # 'content-length': '0',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'CTK=1frd7g1fur89n800; OptanonAlertBoxClosed=2022-02-08T17:53:59.920Z; _ga=GA1.2.760069551.1644342841; __ssid=562fcfa815b5eb818951694549bbfcc; SOCK="ffGX4XivAKwKhVodu1r1AAtPXWs="; SHOE="R9BdUROJhQ_l7cEcixm1nk5MA4e16R3Y7AesTbhme7KNa4PCJsoYmLTUOWgp-xd0X3R2M4KEePKfjq606NSCY819S-c-qf6RFsvN41eNDc71a9OYWDFaq-SDeHvJ2d41PJC5agdOAXbYQw=="; _gcl_au=1.1.1657837122.1652794718; CO=CH; LOCALE=en; pjps=1; RF="q2avyVql9o-cBmrvvmPxu085701jUWdhZgOj7zZyhguFdVdIA_spbAsIbLtCg6i2cYiNmUxrVt1yoc8V37_QpW_12ML1zXimwd2LbJTedKjJQLsMN8tcBpqYNZrfOvvGpLQyEAGXp9wZo8IddBOTdRWxVc_Cg82uvHQeQqgJwlTxF9DuY_B-oKJ9m8uE49SgNIWtQv-WGeJj-4GkGBqiUrIQsgQAd24BsZaoRi3a-Q-cAt3FbnGbKrj5FBNZhVrMQU0uqqvrBYR8ipRQvLjr_tVPvsE5AUb94qdWMB12Ck-LtkW4-P3muAmwXlIPmwbEkwfonuEMtUGzEXELDuzUY7aqJtJlsIiUssoz8pQ8cn0="; CO=CH; LOCALE=en; CMP_VISITED=1; RSJC=50a565615e400018; cmppmeta="eNoBSAC3/4yH20+g5Ls42gAe2e9fZSPEYpuCyTe6KDHp/UnXTc7luLgnNPUJ7bmbNzuvHjCekX2QMsJiwiQML+xL6wXhEYXK6u+Y49lbGnIMJe4="; indeed_rcc="LOCALE:PREF:cmppmeta:LV:CTK:CO:RQ:UD"; JATG=control; CSRF=lYUujyZceNuXxKvMxx6IOgbaqNiTa2pK; INDEED_CSRF_TOKEN=Utdorb8vbL3RIyce4d09rS32sGRDoa2U; LV="LA=1658154367:LV=1655183169:CV=1658143951:TS=1652794716"; UD="LA=1658154367:LV=1655183169:CV=1658143951:TS=1652794716"; __cf_bm=Lsr0VsHpaM6SZCHYundIY3xevv9tif2jDfXNnAuL98o-1660150449-0-Afj4n2hpvYeEGG1issQZIu0Zd4o0eE83MJShARGIs0LtWBLRrKHAlejn4L5QZLi8O2WoG/ewaEgGOwV+vmSARzA=; _cfuvid=krt5igfMgYu78MY7fhI_WCfUkgLW6vEqjfPvt.5XP48-1660150449326-0-604800000; SHARED_INDEED_CSRF_TOKEN=Utdorb8vbL3RIyce4d09rS32sGRDoa2U; MICRO_CONTENT_CSRF_TOKEN=ywsX8WsaShLwF8TOzRSpOfqiGcQ87M9M; PREF="TM=1660150541333:L=Schweiz"; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Aug+10+2022+18%3A55%3A43+GMT%2B0200+(Central+European+Summer+Time)&version=6.37.0&geolocation=%3B&isIABGlobal=false&hosts=&consentId=f48cd989-ec6b-4a18-8faa-c568eb5289ec&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0%2CC0007%3A0&AwaitingReconsent=false; LC="co=CH"; PPID=eyJraWQiOiI3YmYwYzJmMy05OTdmLTQyNGItOWQ4Yi1hZmMzZWEwZmUwMGMiLCJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJzdWIiOiJlMmZlYzNlYjZlMTMxODIzIiwiYXVkIjoiYzFhYjhmMDRmIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImNyZWF0ZWQiOjE1MTMyNzYyOTQwMDAsInJlbV9tZSI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL3NlY3VyZS5pbmRlZWQuY29tIiwiZXhwIjoxNjYwMTUyMzQ0LCJpYXQiOjE2NjAxNTA1NDQsImxvZ190cyI6MTY0NDM0MzExNDg5NSwiZW1haWwiOiJkZW5pXzkwMDBfMTk5MEBhYnYuYmcifQ.MWM_4JibgXlXWhyaDJTtLlpKS5OADphi65aqz9JYeYiOV0vU8oqodZbY5sVInR0PZB0la3uDZHWQxwCFD_0xsQ; _dd_s=rum=0&expire=1660151443516; RQ="q=&l=Schweiz&ts=1660150562846&pts=1654505612887:q=Masseur&l=Bern%2C+BE&ts=1660150509011:q=Masseur&l=&ts=1660150495271:q=&l=Bern%2C+BE&ts=1658149689640:q=Betreuung+Kinder&l=Bern%2C+BE&ts=1658149096115:q=babysitter&l=Bern%2C+BE&ts=1658149004864:q=babysitter&l=stadt+bern&ts=1658148992467:q=babysitter&l=3000&ts=1658148930149:q=software+engineer&l=Z%C3%BCrich%2C+ZH&ts=1655183169834:q=Python&l=&ts=1654367379298&pts=1652795493370"; JSESSIONID=BB464DBA22C4FFA5F5AA062A431735DC',
            'origin': 'https://ch.indeed.com',
            'referer': 'https://ch.indeed.com/jobs?q=&l=Schweiz',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        }
        params = {
            'a': 'check',
            'q': '',
            'l': 'Schweiz',
            'tk': '1ga4aufvrt1e0802',
        }

        # params = {
        #     'q': '',
        #     'l': 'Schweiz',
        #     #'start': f'{counter_pages}0',  # ot koq pochwa 0-1,10-2,20-3,30-4str
        #     #'pp': 'gQAPAAAAAAAAAAAAAAAB3YkJSAAuAQAZ7zv6Ed1n2nD4EsybaOjp04wd_5vdPtAirO0Aal-kXLZ5nG5stUtr7pW6kgAA',
        #
        # }
        #response = requests.get('https://ch.indeed.com/jobs', params=params, cookies=cookies, headers=headers)
        #response = requests.get('https://ch.indeed.com/jobs', params=params, cookies=cookies, headers=headers)
        response = requests.post('https://ch.indeed.com/rpc/jobalert', params=params, cookies=cookies, headers=headers)
        print(response.status_code)
        if response.status_code !=200 or counter_pages>100:
            break
        counter_pages+=1
        html=soup(response.text,'html.parser')
        all_jobs=html.select('.resultContent') # return a list
        print(f" Indeed Page {counter_pages} ==> {len(all_jobs)}")
        for each_job in all_jobs:
            title = ''
            place = ''
            link = ''
            found = re.finditer(pattern, str(each_job))
            for info in found: #allways one result
                title = info.group('title').split(' of ')[1]
                place = info.group('location')
                link = f"{info.group('href').split(';')[0]}"
            #print(f'{title}=={place}=={link}')
            CounterJobs.COUNTER+=1
            if wished_works(title):
                    new_job = Job(
                        title=title,
                        publication_date=today,
                        link=prefix + link,
                        place=place,
                        is_active=True,
                        employeer="no info",
                        borse='Indeed.ch'
                    )
                    new_job.save()



    print(f'Done indeed.Time: {time.time() - start}')
    speak_function(f'The Program is finished in {int(time.time() - start)} seconds!!!')

