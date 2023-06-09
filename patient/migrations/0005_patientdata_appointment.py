# Generated by Django 4.1 on 2023-03-09 05:22

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patient', '0004_patientappointment_timediv'),
    ]

    operations = [
        migrations.CreateModel(
            name='patientData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_diabetic', models.BooleanField(default=False)),
                ('is_asthma', models.BooleanField(default=False)),
                ('is_hypertension', models.BooleanField(default=False)),
                ('is_stroke', models.BooleanField(default=False)),
                ('alergetic_drugs', ckeditor.fields.RichTextField(blank=True, max_length=250)),
                ('weight', models.FloatField(blank=True, default=None)),
                ('height', models.FloatField(blank=True, default=None)),
                ('is_alcoholic', models.BooleanField(default=False)),
                ('blood_group', models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=10)),
                ('covid_vacciantion', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_email', models.EmailField(max_length=100)),
                ('appo_date', models.DateField(default=None)),
                ('appo_time', models.TimeField(default=None)),
                ('appo_status', models.CharField(choices=[('pending', 'pending'), ('accepted', 'accepted'), ('rejected', 'rejected'), ('completed', 'completed'), ('cancelled', 'cancelled'), ('rescheduled', 'rescheduled'), ('in_progress', 'in_progress')], default='pending', max_length=20)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
