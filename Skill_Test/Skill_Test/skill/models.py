from django.db import models

# Create your models here.
class QuestionBank(models.Model):
    question_id = models.CharField(max_length=50,primary_key=True)
    question = models.TextField(max_length=1000)
    difficulty_level = [('EA','Easy'),('ME','Medium'),('HA','Hard')]
    difficulty_id = models.CharField(max_length=10,choices=difficulty_level)
    category_names=[('PY','Python'),('JV','Java'),('DN','Dotnet'),('TS','Testing'),('UI','UI'),('IDM','IDM')]
    category_id = models.CharField(max_length=10,choices=category_names)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    flag = models.BooleanField(default=1)

class sample(models.Model):
    pass