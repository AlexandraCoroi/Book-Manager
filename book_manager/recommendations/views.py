from django.shortcuts import render
from .models import RecommendedBook

def book_recommendations_view(request):
    context = {
        'recently_added': RecommendedBook.objects.filter(category='recently_added'),
        'most_read': RecommendedBook.objects.filter(category='most_read'),
        'all_time_favorites': RecommendedBook.objects.filter(category='all_time_favorites'),
    }
    return render(request, 'books/book_recommendations.html', context)
