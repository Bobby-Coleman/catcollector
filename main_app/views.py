from django.shortcuts import render, redirect
from .models import Cat
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm

def home (request):
    return render(request, 'home.html')

def about (request):
    return render(request, 'about.html')
class CatList(ListView):
    model = Cat

    def get_queryset(self):
        return Cat.objects.all()

def cat_detail(request, pk):
    cat = Cat.objects.get(id=pk)
    feeding_form = FeedingForm()
    return render(request, 'main_app/cat_detail.html', {
        'cat': cat,
        'feeding_form': feeding_form
    })
    
def add_feeding(request, pk):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = pk
        new_feeding.save()
    return redirect('cats_detail', pk=pk)


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
