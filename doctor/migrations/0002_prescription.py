# Generated by Django 4.1 on 2023-03-14 16:15

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0017_delete_patientappointment'),
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('prescription', models.CharField(blank=True, max_length=100, null=True)),
                ('symptoms', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('diagnosis', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('is_lab_report', models.BooleanField(default=False)),
                ('appo_id', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.appointmentconfirmation')),
            ],
        ),
    ]
