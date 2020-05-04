from django.shortcuts import render
from .models import Cat
from django.views.generic import ListView

def home (request):
    return render(request, 'home.html')

def about (request):
    return render(request, 'about.html')

# def cats_index (request):
#     cats = Cat.objects.all()
#     return render(request, 'cats/index.html', { 'cats' : cats })
class CatList(ListView):
    model = Cat

    def get_queryset(self):
        return Cat.objects.all()


def cats_detail (request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', { 'cat' : cat })
