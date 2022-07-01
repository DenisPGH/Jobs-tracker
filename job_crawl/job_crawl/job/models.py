from django.db import models

# Create your models here.

class Job(models.Model):
    TITLE_MAX_LENGHT=200
    PLACE_MAX_LENGTH=50
    EMPLOYEER_MAX_LENGTH=200


    title=models.CharField( max_length=TITLE_MAX_LENGHT)
    publication_date=models.DateField()
    place=models.CharField(max_length=PLACE_MAX_LENGTH)
    is_active=models.BooleanField(default=True)
    link=models.URLField()
    employeer = models.CharField(max_length=EMPLOYEER_MAX_LENGTH, null=True)


class JobScout(models.Model):
    TITLE_MAX_LENGHT=200
    PLACE_MAX_LENGTH=50
    EMPLOYEER_MAX_LENGTH=100


    title=models.CharField( max_length=TITLE_MAX_LENGHT)
    publication_date = models.DateField()
    place=models.CharField(max_length=PLACE_MAX_LENGTH)
    employeer=models.CharField(max_length=EMPLOYEER_MAX_LENGTH)
    link=models.URLField()



class JobYouToor(models.Model):
    TITLE_MAX_LENGHT=200
    PLACE_MAX_LENGTH=50
    EMPLOYEER_MAX_LENGTH=100

    title=models.CharField( max_length=TITLE_MAX_LENGHT)
    publication_date = models.DateField()
    place=models.CharField(max_length=PLACE_MAX_LENGTH)
    employeer=models.CharField(max_length=EMPLOYEER_MAX_LENGTH)
    link=models.URLField(null=True)





class Bewerbungen(models.Model):
    TITLE_MAX_LENGHT=200
    PLACE_MAX_LENGTH=50
    EMPLOYEER_MAX_LENGTH=100

    title=models.CharField( max_length=TITLE_MAX_LENGHT)
    publication_date = models.DateField()
    place=models.CharField(max_length=PLACE_MAX_LENGTH)
    employer=models.CharField(max_length=EMPLOYEER_MAX_LENGTH)
    link=models.URLField(null=True)
    date_apply=models.DateTimeField(null=True)
    apply=models.BooleanField(default=False)


