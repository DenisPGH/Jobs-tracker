from django.urls import path

from job_crawl.job.views import IndexPage, StoreNewJobs, StoreNewJobScout

urlpatterns = [
    path('',IndexPage.as_view(),name='index'),
    path('job/',StoreNewJobs,name='crawl'),
    path('jobscout/',StoreNewJobScout,name='crawlscout'),
]