from django.shortcuts import render
from .models import Cat
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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


class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    # success_url = '/cats/'

class CatUpdate(UpdateView):
    model = Cat
    fields = ['name', 'description', 'age']

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'
