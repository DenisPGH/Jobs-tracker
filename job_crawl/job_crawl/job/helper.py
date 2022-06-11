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





def binary_search(collection,target):
    """
    prove list with string, if contain a target string

    :param collection: list of all strings
    :param target: searched text
    :return: if text is found in a list, return true
    else return false, not in the list collection
    """
    first_index=0
    last_index=len(collection)-1
    while first_index<=last_index:
        mid_point=(first_index+last_index)//2
        if collection[mid_point]==target:
            return True
        elif collection[mid_point]<target:
            first_index=mid_point+1
        else:
            last_index=mid_point-1
    return  False


def check_if_record_already_exist(job):
    """
    this function check if a new job is already in db
    if it is return true
    if its not return false


    """
    tomorrow=str(dt.today()+datetime.timedelta(days=1)).split(" ")[0]
    yesterday=str(dt.today()-datetime.timedelta(days=1)).split(" ")[0]
    today=str(dt.today()).split(" ")[0]
    all_record_from_yesterday=JobScout.objects.filter(publication_date=yesterday).order_by('title')
    all_record_from_today=JobScout.objects.filter(publication_date=today).order_by('title')
    list_strings_yesterday_jobs=[x.title+x.place+x.employeer for x in all_record_from_yesterday]
    list_strings_today_jobs=[y.title+y.place+y.employeer for y in all_record_from_today]
    if binary_search(list_strings_yesterday_jobs,job) or binary_search(list_strings_today_jobs,job):
        return True
    else:
        return False








