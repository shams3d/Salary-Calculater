# Generated by Django 2.1.7 on 2019-03-05 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0027_auto_20190305_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary',
            name='salary',
            field=models.PositiveIntegerField(default='0', editable=False),
        ),
    ]
