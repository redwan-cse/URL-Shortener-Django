from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path('<str:short_url>/', views.redirect_original_url, name='redirect_original_url'),
    path('404/', views.error404)
]