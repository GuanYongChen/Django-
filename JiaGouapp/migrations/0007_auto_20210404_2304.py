# Generated by Django 3.1.7 on 2021-04-04 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JiaGouapp', '0006_auto_20210404_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='pgoods_id',
        ),
        migrations.AlterField(
            model_name='goods',
            name='add_time',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='goods',
            name='upd_time',
            field=models.DateTimeField(default=None),
        ),
    ]