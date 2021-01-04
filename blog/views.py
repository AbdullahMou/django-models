from django.shortcuts import render
# from django.views.generic import TemplateView , ListView
from django.views.generic import  ListView,DetailView
from .models import Post

# Create your views here.
class HomeView(ListView):
    template_name='home.html'
    model = Post

class DetailsView(DetailView):
    template_name='details.html'
    model = Post

        