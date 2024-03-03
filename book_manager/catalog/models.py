from django.db import models


class Book(models.Model):
    titlu = models.CharField(max_length=200, null=True, blank=True)
    autor = models.CharField(max_length=100, null=True, blank=True)
    gen = models.CharField(max_length=100, null=True, blank=True)
    rezumat = models.TextField(null=True, blank=True)
    data_adaugare = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titlu



