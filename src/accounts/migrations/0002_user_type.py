# Generated by Django 3.1.3 on 2020-12-08 12:37

import accounts.enums
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[(accounts.enums.UserType['LIB'], 'LIBRARIAN'), (accounts.enums.UserType['LIB_USER'], 'LIBRARY_USER')], default='', max_length=5),
        ),
    ]
