# Generated by Django 3.2.5 on 2021-09-02 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0007_auto_20210902_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionbank',
            name='category_names',
            field=models.ForeignKey(default='choices', on_delete=django.db.models.deletion.CASCADE, to='skill.domaincategory'),
        ),
    ]