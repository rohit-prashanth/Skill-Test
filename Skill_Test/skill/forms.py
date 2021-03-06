from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import QuestionBank,OptionsTable

from .models import CandidateTable,TestLinkTable

class Candidate_form(forms.ModelForm):
    class Meta:
        model = CandidateTable
        exclude = ['candidate_id','created_date','flag']
        widget = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile_no': forms.TextInput(attrs={'class': 'form-control'}),
            'domain_name': forms.Select(attrs={'class': 'form-control'}),
            'candidate_mail': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email'}
        widget = {

        }


class QuestionBankForm(forms.ModelForm):
    class Meta:
        model = QuestionBank
        fields = ['question', 'category_names', 'difficulty_names']
        labels = {'question': 'Question', 'category_names': 'Category_Names', 'difficulty_names': 'Difficulty_Names'}
        widgets = {
            # 'question_id': forms.TextInput(attrs={'class': 'form-control'}),
            'category_names': forms.Select(attrs={'class': 'form-control'}),
            'difficulty_names': forms.Select(attrs={'class': 'form-control'}),
            'question': forms.Textarea(attrs={'class':'form-control'}),
        }

class OptionTableForm(forms.ModelForm):
    class Meta:
        model = OptionsTable
        fields = ['option1', 'option2','option3','option4','correct_option']
        widgets = {

            'option_id': forms.TextInput(attrs={'class': 'form-control'}),

            'option1': forms.TextInput(attrs={'class':'form-control'}),
            'option2': forms.TextInput(attrs={'class':'form-control'}),
            'option3': forms.TextInput(attrs={'class':'form-control'}),
            'option4': forms.TextInput(attrs={'class':'form-control'}),
            'correct_option': forms.TextInput(attrs={'class':'form-control'}),
        }


class TestLinkTableForm(forms.ModelForm):
    class Meta:
        model = TestLinkTable
        fields = ['category_name', 'no_of_questions','no_of_easy_questions','no_of_medium_questions','no_of_hard_questions','date_of_exam','start_time','end_time']
        widgets = {
            'category_name': forms.Select(attrs={'class': 'form-control'}),

            'no_of_questions': forms.TextInput(attrs={'class': 'form-control'}),

            'no_of_easy_questions': forms.TextInput(attrs={'class':'form-control'}),
            'no_of_medium_questions': forms.TextInput(attrs={'class':'form-control'}),
            'no_of_hard_questions': forms.TextInput(attrs={'class':'form-control'}),
            'date_of_exam': forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'start_time': forms.TimeInput(attrs={'class':'form-control','type':'time'}),
            'end_time': forms.TimeInput(attrs={'class':'form-control','type':'time'}),
        }
