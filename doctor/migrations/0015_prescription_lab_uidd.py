# Generated by Django 4.1 on 2023-03-17 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0014_alter_prescription_lab_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='lab_uidd',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
