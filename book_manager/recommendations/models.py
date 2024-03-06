from django.db import models


class RecommendedBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    cover_image = models.ImageField()
    category = models.CharField(max_length=100, choices=(('recently_added', 'Recently Added'), ('most_read', 'Most Read'), ('all_time_favorites', 'All Time Favorites')))

    def __str__(self):
        return self.title
