# Generated by Django 4.1 on 2023-03-14 16:15

import cloudinary.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0017_delete_patientappointment'),
        ('doctor', '0002_prescription'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lab', '0003_delete_csvdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='labReport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lab_type', multiselectfield.db.fields.MultiSelectField(choices=[('Blood', 'Blood'), ('Urine', 'Urine'), ('Stool', 'Stool'), ('Sputum', 'Sputum'), ('X-Ray', 'X-Ray'), ('CT-Scan', 'CT-Scan'), ('MRI', 'MRI'), ('ECG', 'ECG'), ('Ultrasound', 'Ultrasound'), ('Other', 'Other')], max_length=100)),
                ('report', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('is_active', models.BooleanField(default=True)),
                ('appo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.appointmentconfirmation')),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.lab')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('prescription_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.prescription')),
            ],
        ),
    ]