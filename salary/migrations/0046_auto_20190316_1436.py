# Generated by Django 2.1.7 on 2019-03-16 12:36

from django.db import migrations, models
import salary.models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0045_auto_20190316_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='hrs',
            field=models.FloatField(default='0', validators=[salary.models.Employee.hrs]),
        ),
    ]
