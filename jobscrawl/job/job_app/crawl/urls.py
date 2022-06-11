from django.urls import path

from job.job_app.crawl.views import IndexPage, StoreNewJobs, StoreNewJobScout

urlpatterns = [
    path('',IndexPage.as_view(),name='index'),
    path('job/',StoreNewJobs,name='crawl'),
    path('jobscout/',StoreNewJobScout,name='crawlscout'),
]