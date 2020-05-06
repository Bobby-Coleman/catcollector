from django.shortcuts import render
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
    
def add_feeding(request, cat_id):
	# create the ModelForm using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.cat_id = cat_id
    new_feeding.save()
  return redirect('detail', cat_id=cat_id)


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
