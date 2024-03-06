# Generated by Django 5.0.2 on 2024-03-06 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecommendedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('cover_image', models.ImageField(upload_to='covers/')),
                ('category', models.CharField(choices=[('recently_added', 'Recently Added'), ('most_read', 'Most Read'), ('all_time_favorites', 'All Time Favorites')], max_length=100)),
            ],
        ),
    ]