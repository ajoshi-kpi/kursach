# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('comments_text', models.TextField()),
                ('comments_publication', models.ForeignKey(to='publication.Publication')),
            ],
            options={
                'db_table': 'comments',
            },
            bases=(models.Model,),
        ),
    ]
