# Generated by Django 4.1 on 2022-10-02 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='leaveModel',
            fields=[
                ('leaveId', models.AutoField(primary_key=True, serialize=False)),
                ('leaveDate', models.DateField()),
                ('leaveReason', models.CharField(max_length=50)),
                ('leaveStatus', models.BooleanField(default=False, verbose_name='Approved')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
