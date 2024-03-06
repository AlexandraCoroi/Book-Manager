from django.urls import path, include
from django.contrib.auth import views as auth_views
from users.views.account import register_view

app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='books/login.html',
        redirect_authenticated_user=True
    )),
    path('', include('django.contrib.auth.urls')),
    path('register/', register_view, name='register')
]