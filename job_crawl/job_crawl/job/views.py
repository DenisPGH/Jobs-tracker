from django.shortcuts import render, redirect
from django.views import generic as views
from datetime import datetime
from  datetime import datetime
from job_crawl.job.crawl_jobs_ch import crawl_data_from_jobs_ch
from job_crawl.job.crawl_jobs_scout import searcher_jobscout
from job_crawl.job.crawl_youtoore import crawl_from_youtoore
from job_crawl.job.models import Job, JobScout, JobYouToor, Bewerbungen


class IndexPage(views.TemplateView):
    """ start function, return context data for show in html"""
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        today = str(datetime.today()).split(' ')[0]
        context = super().get_context_data(**kwargs)
        # self.object is a Profile instance
        jobs = Job.objects.all().order_by('title')
        jobscout = JobScout.objects.all().filter(publication_date=today).order_by('title')
        youtoore= JobYouToor.objects.all().filter(publication_date=today).order_by('title')
        bewerbungen= Bewerbungen.objects.all()
        context['jobs']=jobs
        context['today']=today
        context['jobscout']=jobscout
        context['youtoore']=youtoore
        context['bewerbungen']=bewerbungen
        context['all']=len(jobs)+len(jobscout)+len(youtoore)
        context['jobs_ch_len']=len(jobs)
        context['scout_ch_len']=len(jobscout)
        context['youtoor_ch_len']=len(youtoore)
        context['my_line']="-"*140


        return context



def StoreNewJobs(request):
    """ this function start the crawling from Jobs.ch and Jobscout.ch and store the result to db"""
    crawl_data_from_jobs_ch()
    crawl_from_youtoore()
    searcher_jobscout()
    return redirect('index')


def StoreNewJobScout(request):
    """ this function start the crawling from Jobscout.ch and store the result to db"""
    searcher_jobscout()
    return redirect('index')



def store_to_bewerbungen(requests,pk):
    """
    function to store applied job in different table in db
    """
    print(pk)

    return redirect('index')



