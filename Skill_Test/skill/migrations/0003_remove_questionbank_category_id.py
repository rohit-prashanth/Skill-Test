# Generated by Django 3.2.6 on 2021-09-02 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0002_candidatestable_employeetable_examresults_optionstable_testlinktable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionbank',
            name='category_id',
        ),
    ]