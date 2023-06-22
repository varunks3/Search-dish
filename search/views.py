from django.shortcuts import render
from .forms import SearchForm
from .models import Dish


from django.db.models import Q

def search_dishes(request):
    form = SearchForm(request.GET)
    dishes = []

    if form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            dishes = Dish.objects.filter(items__icontains=query)

    return render(request, 'search_results.html', {'form': form, 'dishes': dishes})



def index(request):
    dishes = Dish.objects.all()
    return render(request, 'index.html', {'dishes': dishes})


