# Generated by Django 4.1.3 on 2022-12-15 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vms_app', '0006_alter_driver_nationalid_alter_driver_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
