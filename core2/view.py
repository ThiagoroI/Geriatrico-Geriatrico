from django.views.generic import View
from django.shortcuts import render

#Vista inicial del programa
class Homeview(View):
    def get(self, request, *args, **kwargs):
        contexto={
            
        }
        return render (request,'Home.html', contexto)