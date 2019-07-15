from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from .models import Questions, UserProfileInfo
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        password = request.POST.get('password')
        phone = request.POST.get('phone')

        user = User.objects.create_user(username=username, password=password, first_name=fname)
        user.save()
        login(request, user)
        userprofile = UserProfileInfo(user=user, phone=phone)
        userprofile.save()

        return HttpResponseRedirect(reverse('question_hub'))
    else:
        return render(request, 'basic_app/login.html')


def add_question(request):
    if request.method == "POST":
        questions = request.POST.get('q')
        choice1 = request.POST.get('c1')
        choice2 = request.POST.get('c2')
        choice3 = request.POST.get('c3')
        choice4 = request.POST.get('c4')
        correct = request.POST.get('option')
        if choice1 == "" or choice2 == "" or choice3 == "" or choice4 == "" or questions == "" or correct is None:
            return render(request, 'basic_app/coding.html', context={
                'c1': choice1, 'c2': choice2, 'c3': choice3,
                'c4': choice4, 'q': questions, 'correct': correct, 'error': 'true'
            })
        q = Questions(user=request.user)
        q.questions = questions
        q.choice1 = choice1
        q.choice2 = choice2
        q.choice3 = choice3
        q.choice4 = choice4
        q.correct = correct
        q.user = User.objects.get(username=request.user.username)
        userprofile = UserProfileInfo.objects.get(user=request.user)
        userprofile.nofquestion += 1
        userprofile.lastQuestion = timezone.now()
        userprofile.save()
        q.save()

        return HttpResponseRedirect(reverse('question_hub'))

    else:
        return render(request, 'basic_app/coding.html')


def edit_question(request, id):
    a = Questions.objects.get(id=id)
    if request.method == "GET":
        a = Questions.objects.get(id=id)
        dict = {'q': a.questions, 'c1': a.choice1, 'c2': a.choice2,
                'c3': a.choice3, 'c4': a.choice4, 'correct': a.correct}

        return render(request, 'basic_app/coding.html', context=dict)

    elif request.method == "POST":
        questions = request.POST.get('q')
        choice1 = request.POST.get('c1')
        choice2 = request.POST.get('c2')
        choice3 = request.POST.get('c3')
        choice4 = request.POST.get('c4')
        correct = request.POST.get('option')
        if choice1 == "" or choice2 == "" or choice3 == "" or choice4 == "" or questions == "" or correct is None:
            return render(request, 'basic_app/coding.html', context={
                'c1': choice1, 'c2': choice2, 'c3': choice3, 'c4': choice4, 'q': questions, 'correct': correct, 'error':'true
            })

        a.questions = questions
        a.choice1 = choice1
        a.choice2 = choice2
        a.choice3 = choice3
        a.choice4 = choice4
        a.correct = correct
        a.save()

        return HttpResponseRedirect(reverse('question_hub'))


def question_hub(request):
    questions = Questions.objects.filter(user=request.user)
    return render(request, 'basic_app/questionHub.html', context={'questions': questions})


def leader(request):
    if request.user.is_authenticated:
        a = UserProfileInfo.objects.order_by("nofquestion", '-lastQuestion')
        b = a.reverse()
        dict = {'list': b}
        return render(request, 'basic_app/leaderboard.html', context=dict)

    else:
        return HttpResponseRedirect(reverse('register'))


def elogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('question_hub'))

        else:
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'basic_app/login.html', {})


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('register'))













