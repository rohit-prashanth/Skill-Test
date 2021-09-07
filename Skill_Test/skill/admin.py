from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(QuestionBank)
class QuestionBankAdmin(admin.ModelAdmin):
    list_display = ['question_id','category_names','question','difficulty_names','created_date','modified_date','flag']


@admin.register(OptionsTable)
class OptionTableAdmin(admin.ModelAdmin):
    list_display = ['option_id','question_id','option1','option2','option3','option4','correct_option','created_date','modified_date']

@admin.register(ExamResults)
class ExamResultsAdmin(admin.ModelAdmin):
    list_display = ['exam_id','cad_id','given_by','given_date','flag']

@admin.register(TestLinkTable)
class TestLinkTableAdmin(admin.ModelAdmin):
    list_display = ['test_id','category_name','no_of_questions','no_of_easy_questions','no_of_medium_questions','no_of_hard_questions','date_of_exam','start_time','end_time','test_link','flag']


@admin.register(DomainCategory)
class DomainCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_id','category_name']

@admin.register(DifficultyLevel)
class DiffucultyLevelAdmin(admin.ModelAdmin):
    list_display = ['difficulty_id','difficulty_name']

@admin.register(CandidateTable)
class CandidatesTableAdmin(admin.ModelAdmin):
    list_display = ['candidate_id','first_name','last_name','domain_name','flag','mobile_no',"created_date",'candidate_mail','flag']

@admin.register(EmployeeTable)
class EmployeeTableAdmin(admin.ModelAdmin):
    list_display = ['emp_id', 'emp_name','domain','flag']





