from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    genre = models.CharField(max_length=100, null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Average'),
        (4, '4 - Good'),
        (5, '5 - Excellent'),
    ]
    rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)


    def __str__(self):
        return self.title



