# Generated by Django 3.2.5 on 2021-09-02 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0015_alter_optionstable_correct_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionbank',
            name='category_names',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='skill.domaincategory'),
        ),
    ]
