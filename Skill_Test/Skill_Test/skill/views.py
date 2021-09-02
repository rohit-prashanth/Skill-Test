from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import QuestionBankForm,OptionTableForm
from django.contrib import messages
def questions(request):
    if request.method == 'POST':
        fm = QuestionBankForm(request.POST)
        fm1 = OptionTableForm(request.POST)
        if fm.is_valid():
            fm.save()
            if fm1.is_valid():
                fm1.save()
            return HttpResponseRedirect('/ques')
        else:
            messages.error(request,'Invalid Data')
            return HttpResponseRedirect('/ques')

    else:
        fm = QuestionBankForm()
        fm1 = OptionTableForm()
        return render(request,'questions.html',{'form':fm,'form1':fm1})

def user_login(request):

   if request.method == 'POST':
        fm = AuthenticationForm(request=request,data=request.POST)
        print(fm.is_valid())
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            print(uname,upass)
            user = authenticate(username=uname,password=upass)
            print(user)
            if user is not None:
                login(request,user)
                messages.success(request,'Logged in Succesfully !!!')
                return HttpResponseRedirect('/profile')
   else:
        fm = AuthenticationForm()
   return render(request, 'user_login.html', {'form': fm})

def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')