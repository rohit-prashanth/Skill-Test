from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from .forms import QuestionBankForm,OptionTableForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def questions(request):
    if request.method == 'POST':
        fm = QuestionBankForm(request.POST)
        fm1 = OptionTableForm(request.POST)
        if fm.is_valid() and fm1.is_valid():
            fm.save()
            fm1.save()
            messages.success(request, 'Added Question Successfully')
            return HttpResponseRedirect('/ques')
        else:
            messages.error(request,'Invalid Data')
            return HttpResponseRedirect('/ques')
    else:
        fm = QuestionBankForm()
        fm1 = OptionTableForm()
        question_id = "QAPY05"
        return render(request,'questions.html',{'form1':fm1,'form':fm,'q':question_id})

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

def Send_link_to_Email(request):
    if request.method == 'POST':
        mails = request.POST.get('email')
        var = mails.split(',')
        print(var)
        for i in var:
            # to = request.POST.get('email')
            # print(to)
            content = request.POST.get('content')
            print(i, content)
            send_mail(
                "Skill Assessment | OILC - 301 | Django | 30-Aug-21",
                content,
                settings.EMAIL_HOST_USER,
                [i]
            )
        return render(request, 'index.html', {'name': 'SEND eMAIL NOTIFICATION'})
    else:
        return render(request, 'index.html', {'name': 'SEND eMAIL NOTIFICATION'})

