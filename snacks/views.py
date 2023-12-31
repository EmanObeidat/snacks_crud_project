from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Snack
from django.urls import reverse_lazy, reverse
# Create your views here.
class SnackListView(ListView):
    template_name='snacks_list.html'
    model=Snack
class SnackDetailView(DetailView):
    template_name='snacks_detail.html'
    model=Snack


class SnackCreateView(CreateView) :
    template_name = 'snacks_create.html'
    model =Snack
    fields =['title','purchaser','description','reviewer']
class SnackUpdateView(UpdateView):
    template_name='snack_update.html'
    model=Snack
    fields= '__all__'
    success_url = reverse_lazy('home')

class SnackDeleteView(DeleteView):
    template_name='snack_delete.html'
    model= Snack
    success_url = reverse_lazy('home')