# Generated by Django 2.1.7 on 2019-05-03 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question_text',
            new_name='question',
        ),
    ]
