# Generated by Django 3.0.8 on 2020-07-16 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_auto_20200716_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='destination',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='flight',
            name='origin',
            field=models.CharField(max_length=64),
        ),
        migrations.DeleteModel(
            name='Airport',
        ),
    ]
