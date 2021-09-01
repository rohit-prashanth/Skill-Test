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

class OptionsTable(models.Model):
    option_id = models.CharField(max_length=50,primary_key=True)
    question_id = models.ForeignKey(QuestionBank, on_delete=models.CASCADE)
    op1 = models.CharField(max_length=50)
    op2 = models.CharField(max_length=50)
    op3 = models.CharField(max_length=50)
    op4 = models.CharField(max_length=50)
    correct_option = models.CharField(max_length=50)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

class ExamResults(models.Model):
    exam_id = models.CharField(max_length=50)
    cad_id = models.CharField(max_length=50)
    given_by = models.CharField(max_length=50)
    given_date = models.CharField(max_length=50)
    flag = models.BooleanField(default=1)

class TestLinkTable(models.Model):
    test_id = models.CharField(max_length=50,primary_key=True)
    category_id = models.CharField(max_length=10)
    no_of_questions = models.CharField(max_length=10)
    no_of_easy_questions = models.CharField(max_length=10)
    no_of_medium_questions = models.CharField(max_length=10)
    no_of_hard_questions = models.CharField(max_length=10)
    date_of_exam = models.DateField()
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)
    test_link = models.URLField()
    flag = models.BooleanField(default=1)
