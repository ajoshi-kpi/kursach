# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('publication_title', models.CharField(max_length=200)),
                ('publication_text', models.TextField()),
                ('publication_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'publication',
            },
            bases=(models.Model,),
        ),
    ]
