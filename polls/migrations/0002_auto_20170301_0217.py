# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 02:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='Choice_text',
            new_name='choice_text',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_test',
            new_name='question_text',
        ),
    ]
