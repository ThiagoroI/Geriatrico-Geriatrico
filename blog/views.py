from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .Forms import *
from .models import *

#Pagina principal del sitio
class BloglistView(View):
    def get (self, request, *args, **kwargs):
        contexto = {
            
        }
        return render (request, 'Geriatrico.html', contexto)

#Vista para el interno    
class InternoCreateView (View):
    def get (self, request, *args, **kwargs):
        form=createInterno()
        contexto = {
            'form':form
        }
        return render (request, 'Internos.html', contexto)
    
    #Mandamos la informacion a la base de datos
    def post (self, request, *args, **kwargs):
        if request.method == "POST":
            form = createInterno(request.POST)
            if form.is_valid():
                nombre = form.cleaned_data.get('nombre')
                apellido = form.cleaned_data.get('apellido')
                numero_cedula = form.cleaned_data.get('numero_cedula')
                edad = form.cleaned_data.get('edad')
                contacto_emergencia = form.cleaned_data.get('contacto_emergencia')
                
                p, created = Interno.objects.get_or_create(nombre=nombre, apellido = apellido, numero_cedula= numero_cedula, edad=edad, contacto_emergencia= contacto_emergencia) 
                p.save()
                return redirect('blog:home')
            
            
        contexto = {
            
        }
        return render (request, 'Internos.html', contexto)

#vista para el doctor
class DoctorCreateView (View):
    def get (self, request, *args, **kwargs):
        form = createDoctor()
        contexto = {
            'form':form
        }
        return render (request, 'Doctor.html', contexto)
    
    #Mandamos la informacion a la base de datos
    def post (self, request, *args, **kwargs):
        if request.method == "POST":
            form = createDoctor(request.POST)
            if form.is_valid():
                Nombre = form.cleaned_data.get ('Nombre')
                Apellido = form.cleaned_data.get ('Apellido')
                Especialidad = form.cleaned_data.get ('Especialidad')
                
                p, created = Doctor.objects.get_or_create(Nombre=Nombre, Apellido=Apellido, Especialidad=Especialidad)
                p.save()
                return redirect ('blog:home')                             
        contexto = {
            
        }
        return render (request, 'Doctor.html', contexto)

#Vista para el historial del interno
class HistorialHistorialView(View):
    def get (self, request, *args, **kwargs):
        form = createHistorialMedico()
        contexto = {
            'form':form
        }
        return render (request, 'Historial_medico.html', contexto)
    
    #Mandamos la informacion a la base de datos
    def post (self, request, *args, **kwargs):
        if request.method == "POST":
            form = createHistorialMedico(request.POST)
            if form.is_valid():
                Interno_Historial = form.cleaned_data.get('Interno_Historial')
                Tipo_Sangre = form.cleaned_data.get('Tipo_sangre')
                Contacto_Emergencia = form.cleaned_data.get('Contacto_Emergencia')
                Enfermedades = form.cleaned_data.get('Enfermedades')
                Cirugias = form.cleaned_data.get('Cirugias')
                Fecha_Cirugias = form.cleaned_data.get('Fecha_Cirugias')
                
                p, created = Historial_medico.objects.get_or_create(Interno_Historial=Interno_Historial, Tipo_Sangre=Tipo_Sangre, Contacto_Emergencia=Contacto_Emergencia, Enfermedades=Enfermedades, Cirugias=Cirugias, Fecha_Cirugias=Fecha_Cirugias)
                p.save()
                return redirect ('blog:home')
        contexto = {
            
        }
        return render (request, 'Historial_medico.html', contexto)

class PersonalView (View):
    def get (self, request, *args, **kwargs):
        contexto = {
            
        }
        return render (request, 'Personal.html', contexto)
    
    def post (self, request, *args, **kwargs):
        contexto={
            
        }   
        return render (request, 'Personal.html', contexto) 