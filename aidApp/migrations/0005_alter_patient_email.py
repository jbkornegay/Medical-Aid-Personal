# Generated by Django 3.2.4 on 2021-06-21 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aidApp', '0004_rename_feedbackform_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
