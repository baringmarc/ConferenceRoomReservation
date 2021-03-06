# Generated by Django 3.2.10 on 2022-03-13 07:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomReservation', '0009_auto_20220312_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='dateReserved',
            field=models.DateField(default=datetime.date(2022, 3, 13)),
        ),
    ]
