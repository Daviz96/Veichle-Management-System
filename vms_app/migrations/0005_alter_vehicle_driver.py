# Generated by Django 4.1.3 on 2022-12-13 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vms_app', '0004_vehicle_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='driver',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='vms_app.driver'),
        ),
    ]
