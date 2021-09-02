from django.db import models
class DomainCategory(models.Model):
    category_id = models.CharField(max_length=20)
    category_name = models.CharField(max_length=20)
    def __str__(self):
        return self.category_id
class DifficultyLevel(models.Model):
    difficulty_id = models.CharField(max_length=20)
    difficulty_name = models.CharField(max_length=20)
    def __str__(self):
        return self.difficulty_id
class QuestionBank(models.Model):
    question_id = models.CharField(max_length=50,primary_key=True)
    question = models.TextField(max_length=1000)
    category_names = models.ForeignKey(DomainCategory,on_delete=models.CASCADE)
    difficulty_names = models.ForeignKey(DifficultyLevel,on_delete=models.CASCADE)
    category_id = models.CharField(max_length=10)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    flag = models.BooleanField(default=1)

