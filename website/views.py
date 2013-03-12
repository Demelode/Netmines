from django.http import HttpResponse
from django.shortcuts import render
from website.models import Announcement, About, Game

from django.contrib.auth.models import User, Group
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from website.serializers import UserSerializer, GroupSerializer, GameSerializer


@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'users': reverse('user-list', request=request),
        'groups': reverse('group-list', request=request),
        'game': reverse('game-list', request=request),
    })


class GameList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of games.
    """
    model = Game
    serializer_class = GameSerializer


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single game.
    """
    model = Game
    serializer_class = GameSerializer


class UserList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of users.
    """
    model = User
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single user.
    """
    model = User
    serializer_class = UserSerializer


class GroupList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of groups.
    """
    model = Group
    serializer_class = GroupSerializer


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single group.
    """
    model = Group
    serializer_class = GroupSerializer


def main(request):
    announcement_list = Announcement.objects.order_by('-date')[:3]
    context = {'announcement_list': announcement_list}
    return render(request, 'main.html', context)


def play(request):
    return render(request, 'play.html')


def hiscores(request):
    return render(request, 'hiscores.html')


def about(request):
    about_list = About.objects.order_by('title')[:1]
    context = {'about_list': about_list}
    return render(request, 'about.html', context)
