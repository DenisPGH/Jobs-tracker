from django.db import models

# Create your models here.

class Job(models.Model):
    TITLE_MAX_LENGHT=200
    PLACE_MAX_LENGTH=50


    title=models.CharField( max_length=TITLE_MAX_LENGHT)
    publication_date=models.DateField()
    place=models.CharField(max_length=PLACE_MAX_LENGTH)
    is_active=models.BooleanField(default=True)
    link=models.URLField()


class JobScout(models.Model):
    TITLE_MAX_LENGHT=200
    PLACE_MAX_LENGTH=50
    EMPLOYEER_MAX_LENGTH=100


    title=models.CharField( max_length=TITLE_MAX_LENGHT)
    place=models.CharField(max_length=PLACE_MAX_LENGTH)
    employeer=models.CharField(max_length=EMPLOYEER_MAX_LENGTH)
    link=models.URLField()


