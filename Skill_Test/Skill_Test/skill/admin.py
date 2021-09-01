from django.contrib import admin

from .models import QuestionBank,OptionsTable,ExamResults,TestLinkTable

# Register your models here.
@admin.register(QuestionBank)
class QuestionBankAdmin(admin.ModelAdmin):
    list_display = ['question_id','question','difficulty_level','difficulty_id','category_names','category_id','created_date','modified_date','flag']


@admin.register(OptionsTable)
class QuestionBankAdmin(admin.ModelAdmin):
    list_display = ['option_id','question_id','op1','op2','op3','op4','correct_option','created_date','modified_date']

@admin.register(ExamResults)
class QuestionBankAdmin(admin.ModelAdmin):
    list_display = ['exam_id','cad_id','given_by','given_date','flag']

@admin.register(TestLinkTable)
class QuestionBankAdmin(admin.ModelAdmin):
    list_display = ['test_id','category_id','no_of_questions','no_of_easy_questions','no_of_medium_questions','no_of_hard_questions','date_of_exam','start_time','end_time','test_link','flag']

from .models import *

# Register your models here.
admin.site.register(QuestionBank)
admin.site.register(DomainCategory)
admin.site.register(DifficultyLevel)




