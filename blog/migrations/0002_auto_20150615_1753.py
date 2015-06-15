# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='reads',
            field=models.ManyToManyField(related_name='post_reader', verbose_name='\u041a\u0442\u043e \u043f\u0440\u043e\u0447\u0438\u0442\u0430\u043b', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
