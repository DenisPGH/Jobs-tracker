# Generated by Django 4.0.5 on 2022-06-20 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_alter_jobyoutoor_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='employeer',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
