from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from .forms import QuestionBankForm,OptionTableForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import QuestionBank,OptionsTable

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

from django.http import JsonResponse, HttpResponse

from .models import CandidatesTable
from .forms import Candidate_form



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

def questions(request):
    if request.method == 'POST':
        fm = QuestionBankForm(request.POST)
        fm1 = OptionTableForm(request.POST)
        if fm.is_valid() and fm1.is_valid():
            messages.success(request, 'Added Question Successfully')
            difficulty_names=fm.cleaned_data['difficulty_names']
            category_names=fm.cleaned_data['category_names']
            question = fm.cleaned_data['question']
            option1 = fm1.cleaned_data['option1']
            option2 = fm1.cleaned_data['option2']
            option3 = fm1.cleaned_data['option3']
            option4 = fm1.cleaned_data['option4']
            correct_option = fm1.cleaned_data['correct_option']
            count = QuestionBank.objects.filter(category_names=category_names).last()
            if count:
                q_id = 'QA'+str(category_names)[0:2]+str(len(count))
                op_id = 'OP'+str(category_names)[0:2]+str(len(count))
            else:
                q_id = 'QA' + str(category_names)[0:2] + '00'
                op_id = 'OP' + str(category_names)[0:2] + '00'
            Object = QuestionBank(question_id = q_id,question=question,difficulty_names=difficulty_names,category_names=category_names)
            Object.save()
            Object1 = OptionsTable(option_id=op_id,question_id = q_id,option1=option1,option2=option2,option3=option3,option4= option4,correct_option=correct_option )
            Object1.save()

            return HttpResponseRedirect('/ques')
        else:
            messages.error(request,'Invalid Data')
            return HttpResponseRedirect('/ques')
    else:
        fm = QuestionBankForm()
        fm1 = OptionTableForm()
        return render(request,'questions.html',{'form1':fm1,'form':fm})

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



# Create your views here.
def testApi(request):
    Time = 11
    start = 10
    end = 15
    if Time in range(start, end):
        if request.method == "POST":
            fm = Candidate_form(request.POST)
            if fm.is_valid():
                first_name = fm.cleaned_data['first_name']
                last_name = fm.cleaned_data['last_name']
                domain = fm.cleaned_data['domain']
                candidate_mail = fm.cleaned_data['candidate_mail']
                mobile_no = fm.cleaned_data['mobile_no']
                candidate_id = 'CA' + first_name + mobile_no[-4:]
                Object = CandidatesTable(candidate_id=candidate_id,first_name=first_name, last_name=last_name, domain=domain,
                                      candidate_mail=candidate_mail,mobile_no=mobile_no)

                Object.save()
                return redirect('/instructions')
        else:
            fm = Candidate_form
            return render(request, 'candidate.html', {'form': fm})

    elif Time <= start:
        link = 'Test not yet started..'
        return render(request, 'before_test.html', {'link': link})
    else:

        link = "Access Denied"
        var = 'This test has been deactivated.Please contact your administrator at Ojas innovative technologies..'
    return render(request, 'after_test.html', {'link': link, 'test': var})

def Test_instructins(request):
    return render(request, "home.html")
