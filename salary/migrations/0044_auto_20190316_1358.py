# Generated by Django 2.1.7 on 2019-03-16 11:58

from django.db import migrations, models
import salary.models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0043_auto_20190316_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='hrs',
            field=models.FloatField(default='0', validators=[salary.models.Employee.hrs]),
        ),
    ]
