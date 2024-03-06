# Generated by Django 5.0.2 on 2024-03-06 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Poor'), (2, '2 - Fair'), (3, '3 - Average'), (4, '4 - Good'), (5, '5 - Excellent')], null=True),
        ),
    ]