from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView ,UpdateView ,DeleteView
from .models import *
from django.urls import reverse_lazy

# Create your views here.

class HomeView(ListView):
    template_name = 'home.html'
    model = Crud_r

class CrudDetailsView(DetailView):
    template_name = 'crud_detail.html'
    model = Crud_r

class CrudCreateView(CreateView):
    template_name = 'crud_create.html'
    model = Crud_r
    fields = ['title', 'author', 'body']

class CrudUpdateView(UpdateView):
    template_name = 'crud_update.html'
    model = Crud_r
    fields = ['title', 'author', 'body']

class CrudDeleteView(DeleteView):
    template_name = 'crud_delete.html'
    model = Crud_r
    fields = ['title', 'author', 'body']
    success_url = reverse_lazy('home')
