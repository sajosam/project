# Generated by Django 4.1 on 2023-03-13 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_account_dob_alter_otp_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x0000012F8F749310>', max_length=200),
        ),
    ]
