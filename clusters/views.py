from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from django.views.generic import ListView, DetailView, CreateView

class ClusterListView(ListView):
    model = Cluster

