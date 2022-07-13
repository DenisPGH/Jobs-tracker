import csv
from datetime import datetime as dt
import datetime
import requests
from bs4 import BeautifulSoup as soup
import re
import time





from job_crawl.job.helper import prove_for_german_letter, bad_works, check_if_record_already_exist, wished_works
from job_crawl.job.models import JobScout, Job

pattern=r'href="(?P<link>([^@]+/))"[^@]+ title="(?P<name>([^@]+))"'
patter_town=r'<span>(?P<employer>([^@]+))</[^@]+>, <span>(?P<place>([^@]+))</span>'



def searcher_jobscout():
    start = time.time()
    del_table=JobScout.objects.all()
    del_table.delete()
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
    counter_found_jobs=0
    today = str(dt.today()).split(' ')[0]
    yesterday = str(dt.today() - datetime.timedelta(days=1)).split(" ")[0]
    prefix='https://www.jobscout24.ch'

    with open('result_scout.csv', 'w') as file:
        file.write('')

    while True:
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # Requests sorts cookies= alphabetically
            # 'Cookie': f"ASID=02dc0aeb-6173-4a16-b9fd-90c6af5f4285|20220520|20; CONSENTMGR=c1:1%7Cc4:1%7Cc2:0%7Cc3:0%7Cc5:0%7Cc6:0%7Cc7:0%7Cc8:0%7Cc9:0%7Cc10:0%7Cc11:0%7Cc12:0%7Cc13:0%7Cc14:0%7Cc15:0%7Cts:1653026236856%7Cconsent:true; JS24_CONSENT=sn|ff|mr|1; _gcl_au=1.1.1468808755.1653026238; _hjSessionUser_373146=eyJpZCI6ImI1ZmQwMGVmLTZjNGUtNWVhMy05NzA3LWZmOGQ3ZmIzMDNlOCIsImNyZWF0ZWQiOjE2NTMwMjYyMzgwOTMsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.1579453522.1654505721; _JS24A=0; ASP.NET_SessionId=xm2lp2rz4wpaxngmizdyilid; __RequestVerificationToken=fm0XFBUtpU2skpslyx1_STV8ESR2P7DdX6TZRh9tLoEpzKthvw2S9lX4TC3GWzBYJfZlmMpHA68LW9auz9mOwbezvBI1; xm_jobweb=3389002762.20480.0000; _hjAbsoluteSessionInProgress=1; _hjSession_373146=eyJpZCI6ImE2MTc1ZmY4LWQzMDEtNGE5Zi1hNzYyLTY5YjQzZTg2MWUwYyIsImNyZWF0ZWQiOjE2NTQ1ODA4MjIxOTgsImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _hjIncludedInSessionSample=0; TS01ce6450=017721f21f79e863847a7f7dc3e7bb2c1f494ed1e9bec96e77d6dd676c4f09689a788ddf59d85c48d3225b743c155760055f3e3ed9; ViewSource=; _ga_3EKC6G4KSB=GS1.1.1654580821.5.1.1654582330.0; utag_main=v_id:0180e00aa34f001afe859fddd98d0506f0029067007e8{_sn:8$_se:26$_ss:0$_st:1654584130867$browser_client_id:xfsq0qy$user_anon_id:anon_1520784316553$dc_visit:8$ses_id:1654580820603%3Bexp-session$_pn:5%3Bexp-session$dc_event:26%3Bexp-session$dc_region:eu-central-1%3Bexp-session;} _ga=GA1.1.xfsq0qy",
            'Origin': 'https://www.jobscout24.ch',
            'Referer': f'https://www.jobscout24.ch/de/jobs/?psz=3000&actuality=0&p={counter_pages}',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        params = {
            'psz': '3000',
            'p': f'{counter_pages}',
            'actuality': '0', # last 24 hr is set
        }


        response = requests.get('https://www.jobscout24.ch/de/jobs/', params=params, cookies=cookies, headers=headers)
        if response.status_code !=200:
            break
        counter_pages+=1
        html=soup(response.text,'html.parser')
        all_jobs=html.select('.upper-line') # return a list
        job_attributes=html.select('.job-attributes')
        dict_=dict(zip(all_jobs,job_attributes))
        print(f" Jobscout Page {counter_pages} ==> {len(all_jobs)}")
        for key,value in dict_.items():
            info=re.finditer(pattern,str(key))
            places=re.finditer(patter_town,str(value))
            title=''
            title_origin=''
            link=''
            place=''
            employer=''

            # with open('result_scout.csv', mode='a', newline='') as job:
            #     obs_writer = csv.writer(job, delimiter='|')
            for each_data in info:
                counter_found_jobs+=1
                link=str(each_data.group('link'))
                title=str(prove_for_german_letter(each_data.group('name')))
                title_origin=each_data.group('name')
            for each_place in places:
                place = str(prove_for_german_letter(each_place.group('place')))
                employer = str(prove_for_german_letter(each_place.group('employer')))
                employeer_origin=each_place.group('employer')


                #obs_writer.writerow([title,link,place,employer])
                #job_for_prove=title_origin+place+employeer_origin # for prove if already in db, Jobs and Jobscout
                # if bad_works(title) or check_if_record_already_exist(job_for_prove):
                #     continue

                if wished_works(title):
                    # new_jobs=JobScout(
                    #     title=title_origin,
                    #     publication_date=today,
                    #     link=prefix+link,
                    #     place=place,
                    #     employeer=employeer_origin
                    #
                    #     )
                    # new_jobs.save()

                    new_job = Job(
                        title=title_origin,
                        publication_date=today,
                        #publication_date='2000-01-01',
                        link=prefix + link,
                        place=place,
                        is_active=True,
                        employeer=employeer_origin
                    )
                    new_job.save()



    print(f'Done jobscout.Time for it: {time.time() - start}')

