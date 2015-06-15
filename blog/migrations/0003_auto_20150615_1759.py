# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150615_1753'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subscribe',
            unique_together=set([('author', 'reader')]),
        ),
    ]
