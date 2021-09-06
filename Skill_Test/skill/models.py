from django.db import models
import datetime

class DomainCategory(models.Model):
    category_id = models.CharField(max_length=20)
    category_name = models.CharField(max_length=20)
    def __str__(self):
        return self.category_name
class DifficultyLevel(models.Model):
    difficulty_id = models.CharField(max_length=20)
    difficulty_name = models.CharField(max_length=20)
    def __str__(self):
        return self.difficulty_name

class QuestionBank(models.Model):
    question_id = models.CharField(max_length=50,primary_key=True)
    question = models.TextField(max_length=1000)
    category_names = models.ForeignKey(DomainCategory,on_delete=models.CASCADE,default='1')
    difficulty_names = models.ForeignKey(DifficultyLevel,on_delete=models.CASCADE,default='1')
    created_date = models.DateField(auto_now_add=True,null=True)
    modified_date = models.DateField(auto_now=True,null=True)
    flag = models.BooleanField(default=1)
    def __str__(self):
        return self.question_id
class OptionsTable(models.Model):
    option_id = models.CharField(max_length=50,primary_key=True)
    question_id = models.CharField(max_length=50)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    correct_option = models.CharField(max_length=50)
    created_date = models.DateField(auto_now_add=True, null=True)
    modified_date = models.DateField(auto_now=True, null=True)

class ExamResults(models.Model):
    exam_id = models.CharField(max_length=50)
    cad_id = models.CharField(max_length=50)
    given_by = models.CharField(max_length=50)
    given_date = models.DateField()
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

class CandidatesTable(models.Model):
    class Meta:
        db_table = 'Candidatestable'
    candidate_id = models.CharField(primary_key=True,max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=12)
    domain_name = models.ForeignKey(DomainCategory,on_delete=models.CASCADE,default='1')
    candidate_mail = models.EmailField(max_length=254)
    created_date = models.DateField(auto_now_add=True)
    flag = models.BooleanField(default=1)

class EmployeeTable(models.Model):
    class Meta:
        db_table = 'Employeetable'
    emp_id = models.CharField(primary_key=True,max_length=200)
    emp_name = models.CharField(max_length=200)
    domain = models.ForeignKey(DomainCategory,on_delete=models.CASCADE)
    flag = models.BooleanField(default=1)

