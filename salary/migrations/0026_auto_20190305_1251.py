# Generated by Django 2.1.7 on 2019-03-05 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0025_auto_20190305_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='hrs',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='rate',
            field=models.PositiveIntegerField(),
        ),
    ]