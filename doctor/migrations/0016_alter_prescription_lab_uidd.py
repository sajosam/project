# Generated by Django 4.1 on 2023-03-18 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0015_prescription_lab_uidd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='lab_uidd',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]