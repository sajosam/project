# Generated by Django 4.1 on 2023-03-15 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_alter_prescription_is_lab_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='diagnosis',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='symptoms',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]