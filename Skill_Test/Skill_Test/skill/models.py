from django.db import models

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
    category_names = models.ForeignKey(DomainCategory,on_delete=models.CASCADE)
    difficulty_names = models.ForeignKey(DifficultyLevel,on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    flag = models.BooleanField(default=1)
    def __str__(self):
        return self.question_id
class OptionsTable(models.Model):
    option_id = models.CharField(max_length=50,primary_key=True)
    question_id = models.OneToOneField(QuestionBank, on_delete=models.CASCADE)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    options=[('option1','option1'),('option2','option2'),('option3','option3'),('option4','option4'),]
    correct_option = models.CharField(choices=options,max_length=50)
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

class CandidatesTable(models.Model):
    class Meta:
        db_table = 'Candidatestable'
    candidate_id = models.IntegerField(primary_key=True)
    candidate_name = models.CharField(max_length=200)
    domain = models.CharField(max_length=50)
    candidate_mail = models.EmailField(max_length=254)
    flag = models.BooleanField(default=1)

class EmployeeTable(models.Model):
    class Meta:
        db_table = 'Employeetable'
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=200)
    domain = models.CharField(max_length=50)
    flag = models.BooleanField(default=1)