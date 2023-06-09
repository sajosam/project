# Generated by Django 4.1 on 2023-03-18 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0016_alter_prescription_lab_uidd'),
        ('lab', '0012_alter_labreport_lab'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labreport',
            name='prescription_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.prescription'),
        ),
        migrations.AlterField(
            model_name='labreport',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Rejected', 'Rejected'), ('Accepted', 'Accepted'), ('In Progress', 'In Progress')], default='In Progress', max_length=100),
        ),
    ]
