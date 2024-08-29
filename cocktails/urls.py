from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_cocktails, name='search_cocktails'),
    path('cocktail/<str:cocktail_id>/', views.cocktail_detail, name='cocktail_detail'),
    path('cocktail/<str:cocktail_id>/add_to_favorites/', views.add_to_favorites, name='add_to_favorites'),
]