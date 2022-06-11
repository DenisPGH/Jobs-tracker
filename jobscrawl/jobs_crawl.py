import json
import os
import csv
import requests
import time
from datetime import datetime

def prove_for_german_letter(text):
    deutsche={'ö':"oe",'Ö':'OE','Ü':'UE','ü':'ue','ä':'ae','Ä':'AE'}
    for each in deutsche:
        if each in text:
            text=text.replace(each,deutsche[each])
    for each_letter in text:
        if not 0 <= ord(each_letter) <= 127:
            text=text.replace(each_letter,'-')

    return str(text)

#_sn=13 #$_se:7$_ss:0$_st:1654522198770$browser_client_id:el97kjl4$user_anon_id:anon_467984385155$dc_visit:13$ses_id:1654520385639%3Bexp-session$_pn:1%3Bexp-session$dc_event:7%3Bexp-session$dc_region:eu-central-1%3Bexp-session = os.getenv('_sn:13$_se:7$_ss:0$_st:1654522198770$browser_client_id:el97kjl4$user_anon_id:anon_467984385155$dc_visit:13$ses_id:1654520385639%3Bexp-session$_pn:1%3Bexp-session$dc_event:7%3Bexp-session$dc_region:eu-central-1%3Bexp-session')
#_sn:13$_se:7$_ss:0$_st:1654522198770$browser_client_id:el97kjl4$user_anon_id:anon_467984385155$dc_visit:13$ses_id:1654520385639%3Bexp-session$_pn:1%3Bexp-session$dc_event:7%3Bexp-session$dc_region:eu-central-1%3Bexp-session; = os.getenv('_sn:13$_se:7$_ss:0$_st:1654522198770$browser_client_id:el97kjl4$user_anon_id:anon_467984385155$dc_visit:13$ses_id:1654520385639%3Bexp-session$_pn:1%3Bexp-session$dc_event:7%3Bexp-session$dc_region:eu-central-1%3Bexp-session;')

cookies = {
    'session_id': '289a0728-dde1-4c6a-bca4-da645a35e6b7',
    'xp_consent_mgr': 'analytics%2Csearch',
    'CONSENTMGR': 'c1:1%7Cc4:1%7Cc2:0%7Cc3:0%7Cc5:0%7Cc6:0%7Cc7:0%7Cc8:0%7Cc9:0%7Cc10:0%7Cc11:0%7Cc12:0%7Cc13:0%7Cc14:0%7Cc15:0%7Cts:1651731583241%7Cconsent:true',
    'cookie_consent_accept': 'true',
    '_gcl_au': '1.1.1669649857.1651731584',
    '_fbp': 'fb.1.1651731583992.1607363100',
    'ab_experiments': '%5B%7B%22key%22%3A%22CHI-2258-survey%22%2C%22variant%22%3A1%7D%2C%7B%22key%22%3A%22CHI-2258-survey-srp%22%2C%22variant%22%3A1%7D%2C%7B%22key%22%3A%22NUC-3139-publication-date%22%2C%22variant%22%3A1%7D%2C%7B%22key%22%3A%22CHI-2449-personal-message-selector-v2%22%2C%22variant%22%3A1%7D%5D',
    '_hjSessionUser_242502': 'eyJpZCI6IjU5MzI0M2FlLWFjMzAtNWRhYy04NjQ1LTdjMDAyODMzMTMyZiIsImNyZWF0ZWQiOjE2NTM1NDU1MjEyNTcsImV4aXN0aW5nIjp0cnVlfQ==',
    '_gid': 'GA1.2.1283867874.1654493524',
    '_clck': '11nlppr|1|f23|0',
    '_uetsid': 'ff5fbda0e55911eca99dc3eb6c33ac4e',
    '_uetvid': '7f237490ce2811ec9cfb539d0cc427fe',
    '_ga': 'GA1.1.el97kjl4',
    'cto_bundle': 'ja2Nsl9GSkRDWXlvTTFxYVpIMkhDaFpVUnJRZ1JNR2wweGlPYlVFZXRnN0pZdjlnMkdhZjFEZyUyQnhQbWZsJTJGTlVUTnk3WTlVTFh1NCUyRnFPZlpSTk1ZcmVVcWNubVgzbEhWdmFpS0hUJTJGdFZ5SVgxYXM4ZFVtcmcwckx2Y0E0JTJCemJVdkdqY1cwNVI5JTJGS25PaUNpVGhtUmU5JTJCYmRQdyUzRCUzRA',
    '_clsk': '1puei0c|1654520397576|2|1|e.clarity.ms/collect',
    'last_searches': '[{%22query%22:%22location=Bern%22%2C%22date%22:%222022-06-06%2015:59:58%22}%2C{%22query%22:%22query=python%2520developer%22%2C%22date%22:%222022-06-06%2015:59:45%22}%2C{%22query%22:%22category-ids%255B0%255D=103&category-ids%255B1%255D=105&category-ids%255B2%255D=106&category-ids%255B3%255D=108&category-ids%255B4%255D=117&employment-position-ids%255B0%255D=3&location=Bern%22%2C%22date%22:%222022-06-06%2011:04:56%22}]',
    '_ga_WVB8D40K7K': 'GS1.1.1654520387.4.1.1654520398.0',
    #'utag_main': f"v_id:01809f7fa7ee001d088bd1adc17b05073003f06b007e8{_sn:13$_se:7$_ss:0$_st:1654522198770$browser_client_id:el97kjl4$user_anon_id:anon_467984385155$dc_visit:13$ses_id:1654520385639%3Bexp-session$_pn:1%3Bexp-session$dc_event:7%3Bexp-session$dc_region:eu-central-1%3Bexp-session}",
    '_gat_globalGaTracker': '1',
}

headers = {
    'authority': 'www.jobs.ch',
    'accept': 'application/json',
    'accept-language': 'de',
    # Requests sorts cookies= alphabetically
    # 'cookie': f"session_id=289a0728-dde1-4c6a-bca4-da645a35e6b7; xp_consent_mgr=analytics%2Csearch; CONSENTMGR=c1:1%7Cc4:1%7Cc2:0%7Cc3:0%7Cc5:0%7Cc6:0%7Cc7:0%7Cc8:0%7Cc9:0%7Cc10:0%7Cc11:0%7Cc12:0%7Cc13:0%7Cc14:0%7Cc15:0%7Cts:1651731583241%7Cconsent:true; cookie_consent_accept=true; _gcl_au=1.1.1669649857.1651731584; _fbp=fb.1.1651731583992.1607363100; ab_experiments=%5B%7B%22key%22%3A%22CHI-2258-survey%22%2C%22variant%22%3A1%7D%2C%7B%22key%22%3A%22CHI-2258-survey-srp%22%2C%22variant%22%3A1%7D%2C%7B%22key%22%3A%22NUC-3139-publication-date%22%2C%22variant%22%3A1%7D%2C%7B%22key%22%3A%22CHI-2449-personal-message-selector-v2%22%2C%22variant%22%3A1%7D%5D; _hjSessionUser_242502=eyJpZCI6IjU5MzI0M2FlLWFjMzAtNWRhYy04NjQ1LTdjMDAyODMzMTMyZiIsImNyZWF0ZWQiOjE2NTM1NDU1MjEyNTcsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.1283867874.1654493524; _clck=11nlppr|1|f23|0; _uetsid=ff5fbda0e55911eca99dc3eb6c33ac4e; _uetvid=7f237490ce2811ec9cfb539d0cc427fe; _ga=GA1.1.el97kjl4; cto_bundle=ja2Nsl9GSkRDWXlvTTFxYVpIMkhDaFpVUnJRZ1JNR2wweGlPYlVFZXRnN0pZdjlnMkdhZjFEZyUyQnhQbWZsJTJGTlVUTnk3WTlVTFh1NCUyRnFPZlpSTk1ZcmVVcWNubVgzbEhWdmFpS0hUJTJGdFZ5SVgxYXM4ZFVtcmcwckx2Y0E0JTJCemJVdkdqY1cwNVI5JTJGS25PaUNpVGhtUmU5JTJCYmRQdyUzRCUzRA; _clsk=1puei0c|1654520397576|2|1|e.clarity.ms/collect; last_searches=[{%22query%22:%22location=Bern%22%2C%22date%22:%222022-06-06%2015:59:58%22}%2C{%22query%22:%22query=python%2520developer%22%2C%22date%22:%222022-06-06%2015:59:45%22}%2C{%22query%22:%22category-ids%255B0%255D=103&category-ids%255B1%255D=105&category-ids%255B2%255D=106&category-ids%255B3%255D=108&category-ids%255B4%255D=117&employment-position-ids%255B0%255D=3&location=Bern%22%2C%22date%22:%222022-06-06%2011:04:56%22}]; _ga_WVB8D40K7K=GS1.1.1654520387.4.1.1654520398.0; utag_main=v_id:01809f7fa7ee001d088bd1adc17b05073003f06b007e8{_sn:13$_se:7$_ss:0$_st:1654522198770$browser_client_id:el97kjl4$user_anon_id:anon_467984385155$dc_visit:13$ses_id:1654520385639%3Bexp-session$_pn:1%3Bexp-session$dc_event:7%3Bexp-session$dc_region:eu-central-1%3Bexp-session;} _gat_globalGaTracker=1",
    'referer': 'https://www.jobs.ch/de/stellenangebote/?location=Bern&page=2&term=',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
    'x-node-request': 'false',
    'x-source': 'jobs_ch_desktop',
}


counter=1
code=0
start=time.time()
today=str(datetime.today()).split(' ')[0]
#print(today)
with open('info.csv','w') as file:
    file.write('')

while True:
    params = {
        'location': 'Bern',
        'page': f'{counter}',
        'rows': '20',
        'sort': 'date',
    }
    response = requests.get('https://www.jobs.ch/api/v1/public/search', params=params, cookies=cookies, headers=headers)
    result=json.loads(response.text)
    code=response.status_code #200 ok,422 ne e

    if code!=200:
        break

    print(f"Page: {counter} ==> {len(result['documents'])}")
    counter+=1
    with open('info.csv', mode='a', newline='') as job_file:
        jobs_writer = csv.writer(job_file, delimiter='|')
        for each_job_ind in range(len(result['documents'])):

            title = prove_for_german_letter(result["documents"][each_job_ind]['title'])
            # (title)
            publication_date = result["documents"][0]['publication_date'].split('T')[0]
            if publication_date !=today:
                """ store only jobs from the current day"""
                continue
            # print(publication_date)
            place = prove_for_german_letter(result["documents"][each_job_ind]['place'])
            is_active = result["documents"][each_job_ind]['is_active']
            link_ = result["documents"][each_job_ind]['_links']['detail_de']['href']
            # jobs_writer.writerow([title.encode("utf-8")])
            jobs_writer.writerow([title, publication_date, place, is_active, link_])



print(f'Time for it: {time.time()-start}')



#print(result)
# with open('jobs.json','w') as file:
#     file.write(result)
#
# with open('info.csv',mode='w',newline='') as csv:
#     csv.write("aaa")
#     for each_job_ind in range(len(result['documents'])):
#         csv.write(str(each_job_ind))







