# Generated by Django 4.1.5 on 2023-01-20 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Snacks', '0012_alter_snack_produkt_bewertung_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='sternbewertung',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
    ]
