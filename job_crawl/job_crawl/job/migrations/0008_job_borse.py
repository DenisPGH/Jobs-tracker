# Generated by Django 4.0.5 on 2022-07-17 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_rename_employer_jobyoutoor_employeer'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='borse',
            field=models.CharField(max_length=50, null=True),
        ),
    ]