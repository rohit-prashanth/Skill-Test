from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import QuestionBank,OptionsTable


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
        fields = ['question_id','question', 'category_names', 'difficulty_names']
        labels = {'question': 'Question', 'category_names': 'Category_Names', 'difficulty_names': 'Difficulty_Names'}
        widgets = {
            'question_id': forms.TextInput(attrs={'class': 'form-control'}),
            'category_names': forms.Select(attrs={'class': 'form-control'}),
            'difficulty_names': forms.Select(attrs={'class': 'form-control'}),
            'question': forms.Textarea(attrs={'class':'form-control'}),
        }

class OptionTableForm(forms.ModelForm):
    class Meta:
        model = OptionsTable
        fields = ['option_id','option1', 'option2','option3','option4','correct_option']
        widgets = {
            'option_id': forms.TextInput(attrs={'class': 'form-control'}),

            'option1': forms.TextInput(attrs={'class':'form-control'}),
            'option2': forms.TextInput(attrs={'class':'form-control'}),
            'option3': forms.TextInput(attrs={'class':'form-control'}),
            'option4': forms.TextInput(attrs={'class':'form-control'}),
            'correct_option': forms.TextInput(attrs={'class':'form-control'}),
        }
