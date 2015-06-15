# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('body', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0437\u0430\u043f\u0438\u0441\u0438')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f')),
                ('author', models.ForeignKey(verbose_name='\u0410\u0432\u0442\u043e\u0440', to=settings.AUTH_USER_MODEL)),
                ('reads', models.ManyToManyField(related_name='post_reader', verbose_name='\u041a\u0442\u043e \u043f\u0440\u043e\u0447\u0438\u0442\u0430\u043b', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': '\u0417\u0430\u043f\u0438\u0441\u044c',
                'verbose_name_plural': '\u0417\u0430\u043f\u0438\u0441\u0438',
            },
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_joined', models.DateField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f')),
                ('author', models.ForeignKey(related_name='author', verbose_name='\u0410\u0432\u0442\u043e\u0440', to=settings.AUTH_USER_MODEL)),
                ('reader', models.ForeignKey(related_name='reader', verbose_name='\u0427\u0438\u0442\u0430\u0442\u0435\u043b\u044c', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_joined'],
                'verbose_name': '\u041f\u043e\u0434\u043f\u0438\u0441\u043a\u0430',
                'verbose_name_plural': '\u041f\u043e\u0434\u043f\u0438\u0441\u043a\u0438',
            },
        ),
    ]
