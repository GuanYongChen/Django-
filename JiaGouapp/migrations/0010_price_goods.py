# Generated by Django 3.1.7 on 2021-04-08 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('JiaGouapp', '0009_remove_price_goods'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='goods',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='JiaGouapp.goods'),
            preserve_default=False,
        ),
    ]