# Generated by Django 4.1 on 2023-03-11 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_account_dob_alter_otp_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x0000016178999310>', max_length=200),
        ),
    ]
