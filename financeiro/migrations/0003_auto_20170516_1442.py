# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0002_auto_20170515_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tesouraria',
            name='numero_documento',
            field=models.CharField(verbose_name='Númedo do Documnto', max_length=20, default=''),
        ),
    ]
