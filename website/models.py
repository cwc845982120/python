from __future__ import unicode_literals

from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=32, default='default')
    sex = models.TextField(null=True)

    def __unicode__(self):
        return self.name

