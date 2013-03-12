import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Announcement(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    poster = models.ForeignKey(User)

    def was_posted_today(self):
        return was_posted(1)

    def was_posted(self, compdate):
        return self.date >= timezone.now() - datetime.timedelta(days=compdate)


class About(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()


class Account(models.Model):
    name = models.CharField(max_length=12)
    password = models.CharField(max_length=50)
    wins = models.IntegerField()
    loses = models.IntegerField()

    def set_winner_of_game(self, result):
        if result:
            wins += 1
        else:
            loses += 1


class Round(models.Model):
    player_one_pick = models.IntegerField()
    player_two_pick = models.IntegerField()
    turn = models.BooleanField()  # True = player_one, False = player_two


class Game(models.Model):
    player_one = models.CharField(max_length=12)
    player_two = models.CharField(max_length=12)
