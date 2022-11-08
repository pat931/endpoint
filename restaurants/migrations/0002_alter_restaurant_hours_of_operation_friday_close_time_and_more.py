# Generated by Django 4.1.3 on 2022-11-07 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='hours_of_operation_friday_close_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='hours_of_operation_friday_open_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='hours_of_operation_monday_close_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='hours_of_operation_monday_open_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='hours_of_operation_saturday_close_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='hours_of_operation_saturday_open_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='hours_of_operation_sunday_close_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='hours_of_operation_sunday_open_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='hours_of_operation_thursday_close_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='hours_of_operation_thursday_open_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='hours_of_operation_tuesday_close_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='hours_of_operation_tuesday_open_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='hours_of_operation_wenesday_close_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='hours_of_operation_wenesday_open_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
