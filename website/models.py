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
