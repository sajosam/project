# Generated by Django 4.1 on 2023-03-31 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0005_alter_datanalysis_day_alter_datanalysis_day_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='demo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
