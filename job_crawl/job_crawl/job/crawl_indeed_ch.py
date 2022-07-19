
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
        'ASID': '02dc0aeb-6173-4a16-b9fd-90c6af5f4285|20220520|20',
        'CONSENTMGR': 'c1:1%7Cc4:1%7Cc2:0%7Cc3:0%7Cc5:0%7Cc6:0%7Cc7:0%7Cc8:0%7Cc9:0%7Cc10:0%7Cc11:0%7Cc12:0%7Cc13:0%7Cc14:0%7Cc15:0%7Cts:1653026236856%7Cconsent:true',
        'JS24_CONSENT': 'sn|ff|mr|1',
        '_gcl_au': '1.1.1468808755.1653026238',
        '_hjSessionUser_373146': 'eyJpZCI6ImI1ZmQwMGVmLTZjNGUtNWVhMy05NzA3LWZmOGQ3ZmIzMDNlOCIsImNyZWF0ZWQiOjE2NTMwMjYyMzgwOTMsImV4aXN0aW5nIjp0cnVlfQ==',
        '_gid': 'GA1.2.1579453522.1654505721',
        '_JS24A': '0',
        'ASP.NET_SessionId': 'xm2lp2rz4wpaxngmizdyilid',
        '__RequestVerificationToken': 'fm0XFBUtpU2skpslyx1_STV8ESR2P7DdX6TZRh9tLoEpzKthvw2S9lX4TC3GWzBYJfZlmMpHA68LW9auz9mOwbezvBI1',
        'xm_jobweb': '3389002762.20480.0000',
        '_hjAbsoluteSessionInProgress': '1',
        '_hjSession_373146': 'eyJpZCI6ImE2MTc1ZmY4LWQzMDEtNGE5Zi1hNzYyLTY5YjQzZTg2MWUwYyIsImNyZWF0ZWQiOjE2NTQ1ODA4MjIxOTgsImluU2FtcGxlIjpmYWxzZX0=',
        '_hjIncludedInPageviewSample': '1',
        '_hjIncludedInSessionSample': '0',
        'TS01ce6450': '017721f21f79e863847a7f7dc3e7bb2c1f494ed1e9bec96e77d6dd676c4f09689a788ddf59d85c48d3225b743c155760055f3e3ed9',
        'ViewSource': '',
        '_ga_3EKC6G4KSB': 'GS1.1.1654580821.5.1.1654582330.0',
        #'utag_main': f"v_id:0180e00aa34f001afe859fddd98d0506f0029067007e8{_sn:8$_se:26$_ss:0$_st:1654584130867$browser_client_id:xfsq0qy$user_anon_id:anon_1520784316553$dc_visit:8$ses_id:1654580820603%3Bexp-session$_pn:5%3Bexp-session$dc_event:26%3Bexp-session$dc_region:eu-central-1%3Bexp-session}",
        '_ga': 'GA1.1.xfsq0qy',
    }
    counter_pages=1
    today = str(dt.today()).split(' ')[0]
    yesterday = str(dt.today() - datetime.timedelta(days=1)).split(" ")[0]
    prefix='https://ch.indeed.com'

    while True:
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
            'start': f'{counter_pages}0',  # ot koq pochwa 0-1,10-2,20-3,30-4str
            'pp': 'gQAPAAAAAAAAAAAAAAAB3YkJSAAuAQAZ7zv6Ed1n2nD4EsybaOjp04wd_5vdPtAirO0Aal-kXLZ5nG5stUtr7pW6kgAA',

        }
        response = requests.get('https://ch.indeed.com/jobs', params=params, cookies=cookies, headers=headers)
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

