# Generated by Django 3.2.4 on 2021-06-23 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myGarage', '0006_rename_cur_mileage_boat_cur_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='make',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='boat',
            name='model',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='make',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='truck',
            name='make',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='truck',
            name='model',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='truck',
            name='year',
            field=models.CharField(max_length=4),
        ),
    ]
