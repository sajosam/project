# Generated by Django 4.1 on 2023-03-24 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0003_alter_leavemodel_leavediv'),
    ]

    operations = [
        migrations.CreateModel(
            name='datanalysis',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('month', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=10)),
                ('day', models.CharField(max_length=10)),
                ('day_type', models.CharField(max_length=10)),
                ('specialty', models.CharField(max_length=10)),
                ('disease', models.CharField(max_length=10)),
            ],
        ),
    ]
