from django.shortcuts import render
from django.http import HttpResponse
from .models import User


def home(request, id):
    user = User.objects.get(id=id)
    fname = user.first_name
    lname = user.last_name
    age = user.age
    username = user.username
    context = {'fname': fname, 'lname': lname, 'age': age, 'username': username}
    return render(request, 'friends/home.html', context=context)


def addfriend(request):
    pass


def friends(request):
    return render(request, 'friends/home.html')


def invite(request):
    return HttpResponse("Приглашения и заявки")


def about(request):
    return HttpResponse("О сайте")