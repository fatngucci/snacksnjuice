# Generated by Django 4.1.4 on 2022-12-11 20:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Useradmin', '0010_remove_myuser_is_a_cat_myuser_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2002, 12, 11)),
        ),
    ]
