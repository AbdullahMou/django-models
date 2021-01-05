from django.shortcuts import render
# from django.views.generic import TemplateView , ListView
from django.views.generic import  ListView,DetailView,CreateView ,UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
class HomeView(ListView):
    template_name='home.html'
    model = Post

class DetailsView(DetailView):
    template_name='details.html'
    model = Post

class Create_view(CreateView):
    template_name='create.html'        
    model = Post
    fields=['model','owner','price']

class Update_view(UpdateView):
    template_name='update.html'        
    model = Post
    fields=['model','owner','price']

class Delete_view(DeleteView):
    template_name='delete.html'        
    model = Post
    fields=['model','owner','price']
    success_url =reverse_lazy('home')
