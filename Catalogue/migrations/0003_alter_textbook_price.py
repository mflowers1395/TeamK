# Generated by Django 4.0.2 on 2022-04-10 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalogue', '0002_textbook_price_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textbook',
            name='price',
            field=models.FloatField(default=10, max_length=8, verbose_name='Price'),
        ),
    ]
