from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db import models
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from .forms import QuestionBankForm,OptionTableForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import QuestionBank,OptionsTable
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

from django.http import JsonResponse, HttpResponse

from .models import CandidateTable, TestLinkTable
from .forms import Candidate_form, TestLinkTableForm


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
            count = QuestionBank.objects.filter(category_names=category_names)
            print(count,type(count))
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
        obj = TestLinkTable.objects.all()
        return render(request,'profile.html',{'name':request.user,'objects':obj})
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
                domain_name = fm.cleaned_data['domain_name']
                candidate_mail = fm.cleaned_data['candidate_mail']
                mobile_no = fm.cleaned_data['mobile_no']
                candidate_id = 'CA' + first_name + mobile_no[-4:]
                Object = CandidateTable(candidate_id=candidate_id,first_name=first_name, last_name=last_name, domain_name=domain_name,
                                      candidate_mail=candidate_mail,mobile_no=mobile_no)

                Object.save()
                return HttpResponseRedirect('/instructions')
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
    return render(request, "instructions_page.html")

def createtestlink(request):
    global test_link
    if request.method == 'POST':
        fm = TestLinkTableForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Testlink created Successfully')
            category_name=fm.cleaned_data['category_name']
            no_of_questions = fm.cleaned_data['no_of_questions']
            no_of_easy_questions = fm.cleaned_data['no_of_easy_questions']
            no_of_medium_questions = fm.cleaned_data['no_of_medium_questions']
            no_of_hard_questions = fm.cleaned_data['no_of_hard_questions']
            date_of_exam = fm.cleaned_data['date_of_exam']
            start_time = fm.cleaned_data['start_time']
            end_time = fm.cleaned_data['end_time']
            strdate = date_of_exam.strftime("%d%m%Y")

            total = int(no_of_easy_questions) + int(no_of_hard_questions) + int(no_of_medium_questions)

            print(total)

            print(no_of_questions)

            if total == int(no_of_questions):
                if str(category_name) == "PYTHON":
                    test_link = 'http://192.168.7.233:8000/pytest'
                    test_id = str(category_name) + strdate
                if str(category_name) == "JAVA":
                    test_link = 'http://192.168.7.233:8000/jvtest'
                    test_id = str(category_name) + strdate
                if str(category_name) == "DOTNET":
                    test_link = 'http://192.168.7.233:8000/dntest'
                    test_id = str(category_name) + strdate
                if str(category_name) == "IDM":
                    test_link = 'http://192.168.7.233:8000/idmtest'
                    test_id = str(category_name) + strdate
                if str(category_name) == "TESTING":
                    test_link = 'http://192.168.7.233:8000/tstest'
                    test_id = str(category_name) + strdate
                if str(category_name) == "UI":
                    test_link = 'http://192.168.7.233:8000/uitest'
                    test_id = str(category_name) + strdate

                Object = TestLinkTable(test_id=test_id,category_name = category_name,no_of_questions=no_of_questions,
                                       no_of_easy_questions=no_of_easy_questions,no_of_medium_questions=no_of_medium_questions,
                                       no_of_hard_questions=no_of_hard_questions, date_of_exam=date_of_exam, start_time=start_time,
                                       end_time=end_time,test_link=test_link)
                Object.save()
                messages.add_message(request, messages.SUCCESS, 'Improve your profile today!')
                return HttpResponseRedirect('/successmessage/')
            else:
                messages.error(request, 'Data Not Matched')
                data = 'Data not Matched'
                fm = TestLinkTableForm()
                return render(request,'createtestlink.html',{'form':fm,'data':data})
        else:
            messages.error(request,'Invalid Data')
            return HttpResponseRedirect('/link/')
    else:
        fm = TestLinkTableForm()
        return render(request,'createtestlink.html',{'form':fm})


def randomques(request):
    import random
    questions_easy = QuestionBank.objects.filter(category_names__category_name="PYTHON",difficulty_names__difficulty_name='EASY')
    randques_easy = random.sample(list(questions_easy),3)
    questions_medium = QuestionBank.objects.filter(category_names__category_name="PYTHON",difficulty_names__difficulty_name='MEDIUM')
    randques_medium = random.sample(list(questions_medium), 3)
    questions_hard = QuestionBank.objects.filter(category_names__category_name="PYTHON",difficulty_names__difficulty_name='HARD')
    randques_hard = random.sample(list(questions_hard), 3)
    easy_list=[]
    for i in randques_easy:
        option = OptionsTable.objects.filter(question_id=i)
        for i in option:
            easy_list.append([i.option1,i.option2,i.option3,i.option4])
    for sublist in easy_list:
        random.shuffle(sublist)
    print(easy_list)
    medium_list = []
    for i in randques_medium:
        option = OptionsTable.objects.filter(question_id=i)
        for i in option:
            medium_list.append([i.option1, i.option2, i.option3, i.option4])
    for sublist in medium_list:
        random.shuffle(sublist)

    hard_list = []
    for i in randques_hard:
        option = OptionsTable.objects.filter(question_id=i)
        for i in option:
            hard_list.append([i.option1, i.option2, i.option3, i.option4])
    for sublist in hard_list:
        random.shuffle(sublist)
    my_ques_easy = zip(randques_easy, easy_list)
    my_ques_medium = zip(randques_medium, medium_list)
    my_ques_hard = zip(randques_hard, hard_list)
    return render(request, "random.html", {'easy_q':my_ques_easy,'medium_q':my_ques_medium,'hard_q':my_ques_hard})

def index(request):
    user_list = User.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 5)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'pagination.html', {'users': users})

def successmessage(request):
    return render(request,"successmessage.html")


