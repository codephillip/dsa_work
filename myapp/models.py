from __future__ import unicode_literals

from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class SubTopic(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200, null=True, default=None)
    description = models.TextField()
    topic = models.ForeignKey(Topic)

    def __unicode__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200, null=True, default="images/te1.jpg")
    reg_num = models.CharField(max_length=20)
    student_num = models.IntegerField(null=True, default=12345)

    def __unicode__(self):
        return self.name
