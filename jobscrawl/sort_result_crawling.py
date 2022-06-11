import csv
import json


def prove_for_german_letter(text):
    deutsche={'ö':"oe",'Ö':'OE','Ü':'UE','ü':'ue','ä':'ae','Ä':'AE'}
    for each in deutsche:
        if each in text:
            text=text.replace(each,deutsche[each])
    for each_letter in text:
        if not 0 <= ord(each_letter) <= 127:
            text=text.replace(each_letter,'-')

    return str(text)


result=''
with open('jobs.json','r') as file:
    result=json.loads(file.readline())


with open('info.csv', mode='w',newline='') as job_file:
    jobs_writer = csv.writer(job_file, delimiter='|')
    for each_job_ind in range(len(result['documents'])):
        title = prove_for_german_letter(result["documents"][each_job_ind]['title'])
        print(title)
        publication_date = result["documents"][0]['publication_date'].split('T')[0]
        #print(publication_date)
        place = prove_for_german_letter(result["documents"][each_job_ind]['place'])
        is_active = result["documents"][each_job_ind]['is_active']
        link_ = result["documents"][each_job_ind]['_links']['detail_de']['href']
        #jobs_writer.writerow([title.encode("utf-8")])
        jobs_writer.writerow([title,publication_date,place,is_active,link_])


#print(len(result["documents"][0]))
link=result["documents"][0]['_links']['detail_de']['href']#.encode("utf-8")
title=result["documents"][0]['title']
id=result["documents"][0]['company_id']
publication_date=result["documents"][0]['publication_date']
preview=result["documents"][0]['preview']
place=result["documents"][0]['place']
is_active=result["documents"][0]['is_active']
#print(result["documents"][0])
#print(link)
#print(title)
