# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0002_auto_20150604_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='name',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
