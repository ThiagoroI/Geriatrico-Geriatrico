from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class BloglistView(View):
    def get (self, request, *args, **kwargs):
        contexto = {
            
        }
        return render (request, 'Geriatrico.html', contexto)