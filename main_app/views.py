from django.shortcuts import render
from .models import Cat
from django.views.generic import ListView, DetailView

def home (request):
    return render(request, 'home.html')

def about (request):
    return render(request, 'about.html')
class CatList(ListView):
    model = Cat

    def get_queryset(self):
        return Cat.objects.all()


class CatDetail(DetailView):
    model = Cat