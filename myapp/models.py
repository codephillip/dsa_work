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
    image = models.CharField(max_length=200)
    description = models.TextField()
    topic = models.ForeignKey(Topic)

    def __unicode__(self):
        return self.name
