from datetime import datetime as dt
import datetime

from job_crawl.job.models import JobScout


def prove_for_german_letter(text):
    """ function for clear the text from no ASCII char,
     and replace german letters,
     return pure text"""
    deutsche={'ö':"oe",'Ö':'OE','Ü':'UE','ü':'ue','ä':'ae','Ä':'AE'}
    for each in deutsche:
        if each in text:
            text=text.replace(each,deutsche[each])
    for each_letter in text:
        if not 0 <= ord(each_letter) <= 127:
            text=text.replace(each_letter,'-')

    return str(text)


def bad_works(name):
    """
    if has a bad work return true and dont save in db
    else return false, it will be save
    """
    bad_works = ['pflege', 'pflege', 'dipl.', 'sachberater',
                 'sozial', 'sozial', 'geruestbauer', 'geruestbauer',
                'apotheker', 'automatiker', 'fage', 'gipser', 'sachbearbeit',
                 'wissenschaft','zimmerm','maler','metallbauer',
                 'fabe','buchhalter','koch','maurer','schreiner']
    if any(word in name.lower() for word in bad_works):
        return True
    else:
        return False





def binary_search(list,searched):
    pass


def check_if_record_already_exist(job):
    yesterday=str(dt.today()-datetime.timedelta(days=1)).split(" ")[0]
    today=str(dt.today()).split(" ")[0]
    all_record_from_yesterday=JobScout.objects.filter(publication_date=yesterday).order_by('title')
    all_record_from_today=JobScout.objects.filter(publication_date=today).order_by('title')
    list_strings_yesterday_jobs=[x.title+x.place+x.employeer for x in all_record_from_yesterday]
    list_strings_today_jobs=[x.title+x.place+x.employeer for x in all_record_from_today]
    if job in list_strings_yesterday_jobs or job in list_strings_today_jobs:
        return True
    else:
        return False








