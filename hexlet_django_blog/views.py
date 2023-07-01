from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

class IndexView(TemplateView):

    template_name = 'index.html'
    def index(self, request):
        
        return render(request, 'index.html', context={'name': 'Articles'})

def about(request):
    tags = ['обучение', 'программирование', 'python', 'oop']
    return render(
        request, 
        'about.html',
        context={'tags' : tags},
        )