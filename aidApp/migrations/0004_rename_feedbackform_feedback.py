# Generated by Django 3.2.4 on 2021-06-21 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aidApp', '0003_feedbackform'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FeedbackForm',
            new_name='Feedback',
        ),
    ]