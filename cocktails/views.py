from django.shortcuts import render, redirect
import requests
from .models import FavoriteCocktail
from django.template.loader import get_template
from .custom_filters import register  # Добавьте эту строку

def home(request):
    url = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'
    cocktails = []
    for _ in range(15):  # Получим 6 случайных коктейлей
        response = requests.get(url)
        data = response.json()
        cocktails.append(data['drinks'][0])
    return render(request, 'cocktails/home.html', {'cocktails': cocktails})

def search_cocktails(request):
    query = request.GET.get('q')
    url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={query}'
    response = requests.get(url)
    data = response.json()
    cocktails = data.get('drinks', [])
    return render(request, 'cocktails/search_results.html', {'cocktails': cocktails})

def cocktail_detail(request, cocktail_id):
    url = f'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={cocktail_id}'
    response = requests.get(url)
    data = response.json()
    cocktail = data.get('drinks', [{}])[0]
    return render(request, 'cocktails/cocktail_detail.html', {'cocktail': cocktail})

def add_to_favorites(request, cocktail_id):
    if request.user.is_authenticated:
        url = f'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={cocktail_id}'
        response = requests.get(url)
        data = response.json()
        cocktail = data.get('drinks', [{}])[0]
        FavoriteCocktail.objects.create(
            user=request.user,
            cocktail_id=cocktail_id,
            name=cocktail.get('strDrink'),
            image_url=cocktail.get('strDrinkThumb')
        )
    return redirect('cocktail_detail', cocktail_id=cocktail_id)