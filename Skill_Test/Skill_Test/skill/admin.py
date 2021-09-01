from django.contrib import admin
from .models import QuestionBank

# Register your models here.
@admin.register(QuestionBank)
class QuestionBankAdmin(admin.ModelAdmin):
    list_display = ['question_id','question','difficulty_level','difficulty_id','category_names','category_id','created_date','modified_date','flag']