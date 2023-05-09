# Generated by Django 4.1 on 2023-03-17 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0008_alter_labreport_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='labreport',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Rejected', 'Rejected'), ('Accepted', 'Accepted'), ('In Progress', 'In Progress')], default='Pending', max_length=100),
        ),
    ]