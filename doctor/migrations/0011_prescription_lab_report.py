# Generated by Django 4.1 on 2023-03-16 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0010_alter_prescription_appoint_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='lab_report',
            field=models.CharField(blank=True, choices=[('Blood', 'Blood'), ('Urine', 'Urine'), ('Stool', 'Stool'), ('Sputum', 'Sputum'), ('X-Ray', 'X-Ray'), ('CT-Scan', 'CT-Scan'), ('MRI', 'MRI'), ('ECG', 'ECG'), ('Ultrasound', 'Ultrasound'), ('Other', 'Other')], max_length=100, null=True),
        ),
    ]