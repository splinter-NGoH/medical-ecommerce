# Generated by Django 4.0.2 on 2022-03-09 00:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_customerrequests_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerrequests',
            name='phone_number',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='رقم الموبيل'),
        ),
    ]
