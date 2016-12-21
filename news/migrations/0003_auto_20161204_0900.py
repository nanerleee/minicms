# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_article_display'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='display',
        ),
        migrations.AddField(
            model_name='article',
            name='home_display',
            field=models.BooleanField(default=False, verbose_name='\u9996\u9875\u663e\u793a'),
        ),
    ]
