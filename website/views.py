from django.http import HttpResponse
from django.shortcuts import render
from website.models import Announcement, About


def announcement(request):
    announcement_list = Announcement.objects.order_by('-date')[:10]
    context = {'announcement_list': announcement_list}
    return render(request, 'announcement.html', context)


def play(request):
    return render(request, 'play.html')


def hiscores(request):
    return render(request, 'hiscores.html')


def about(request):
    about_list = About.objects.order_by('title')
    context = {'about_list': about_list}
    return render(request, 'about.html', context)


def rules(request):
    return render(request, 'rules.html')
