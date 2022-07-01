from django.urls import path

from job_crawl.job.views import IndexPage, StoreNewJobs, StoreNewJobScout, store_to_bewerbungen_jobs_ch,\
    store_to_bewerbungen_jobs_scout,store_to_bewerbungen_youtore

urlpatterns = [
    path('',IndexPage.as_view(),name='index'),
    path('job/',StoreNewJobs,name='crawl'),
    path('jobscout/',StoreNewJobScout,name='crawlscout'),
    path('storej/<int:pk>/',store_to_bewerbungen_jobs_ch,name='jobs_ch'),
    path('storek/<int:pk>/',store_to_bewerbungen_jobs_scout,name='jobs_scout'),
    path('storel/<int:pk>/',store_to_bewerbungen_youtore,name='jobs_youtore'),
]