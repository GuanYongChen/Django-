# Generated by Django 3.1.7 on 2021-04-06 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('JiaGouapp', '0007_auto_20210404_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='JiaGouapp.user'),
        ),
        migrations.AddField(
            model_name='collect',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='JiaGouapp.user'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='JiaGouapp.user'),
        ),
    ]