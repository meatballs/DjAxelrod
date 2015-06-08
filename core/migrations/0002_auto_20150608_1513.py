# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamentdefinition',
            name='noise',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournamentdefinition',
            name='repetitions',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournamentdefinition',
            name='turns',
            field=models.IntegerField(default=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='results',
            field=jsonfield.fields.JSONField(),
        ),
    ]
