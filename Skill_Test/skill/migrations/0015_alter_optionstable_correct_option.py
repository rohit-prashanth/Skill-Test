# Generated by Django 3.2.5 on 2021-09-02 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0014_auto_20210902_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optionstable',
            name='correct_option',
            field=models.CharField(max_length=50),
        ),
    ]