# Generated by Django 2.1.7 on 2019-03-28 06:14

from django.db import migrations, models
import salary.models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0064_auto_20190326_1953'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Employee', 'verbose_name_plural': 'Employees'},
        ),
        migrations.AlterField(
            model_name='employee',
            name='hrs',
            field=models.FloatField(validators=[salary.models.Employee.hrs]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='rate',
            field=models.FloatField(validators=[salary.models.Employee.rate]),
        ),
    ]