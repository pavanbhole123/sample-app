# Generated by Django 3.1.4 on 2021-01-05 06:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CookieConsent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64)),
                ('sessn', models.CharField(max_length=64)),
                ('concent', models.BooleanField(default=False)),
                ('last_modified', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]