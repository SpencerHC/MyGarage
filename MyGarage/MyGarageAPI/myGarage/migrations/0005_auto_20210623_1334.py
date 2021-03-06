# Generated by Django 3.2.4 on 2021-06-23 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myGarage', '0004_alter_car_next_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='curMileage',
            new_name='cur_mileage',
        ),
        migrations.RemoveField(
            model_name='boat',
            name='curMileage',
        ),
        migrations.RemoveField(
            model_name='truck',
            name='curMileage',
        ),
        migrations.AddField(
            model_name='boat',
            name='cur_mileage',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='truck',
            name='cur_mileage',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='boat',
            name='next_service',
            field=models.DateField(default='0001-01-01', verbose_name='next service date'),
        ),
        migrations.AlterField(
            model_name='boat',
            name='service_interval',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='next_service',
            field=models.DateField(default='0001-01-01', verbose_name='next service date'),
        ),
        migrations.AlterField(
            model_name='car',
            name='service_interval',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='truck',
            name='bed_length',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='truck',
            name='next_service',
            field=models.DateField(default='0001-01-01', verbose_name='next service date'),
        ),
        migrations.AlterField(
            model_name='truck',
            name='service_interval',
            field=models.CharField(default='', max_length=100),
        ),
    ]
