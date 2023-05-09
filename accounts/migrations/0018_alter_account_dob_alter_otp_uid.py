# Generated by Django 4.1 on 2023-03-14 16:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_otp_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='dob',
            field=models.DateField(default=datetime.date(2023, 3, 14)),
        ),
        migrations.AlterField(
            model_name='otp',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x0000026801ABB310>', max_length=200),
        ),
    ]