# Generated by Django 2.1.3 on 2019-01-17 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0002_auto_20190117_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]