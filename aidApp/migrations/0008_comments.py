# Generated by Django 3.2.4 on 2021-07-17 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aidApp', '0007_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
