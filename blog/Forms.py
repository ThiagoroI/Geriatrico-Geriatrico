from django import forms
from .models import *

#form para el modelo del interno
class createInterno(forms.ModelForm):
    class Meta:
        model = Interno
        fields = ('nombre', 'apellido', 'numero_cedula', 'edad', 'contacto_emergencia')

#form para el modelo de doctor       
class createDoctor(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('Nombre', 'Apellido', 'Especialidad')

#Form para el modelo historial   
class createHistorialMedico (forms.ModelForm):
    class Meta:
        model = Historial_medico
        fields = ('Interno_Historial', 'Tipo_Sangre', 'Contacto_Emergencia', 'Enfermedades', 'Cirugias', 'Fecha_cirugias')  
        
class createPersonal (forms.ModelForm):
    class Meta:
        model = Personal
        fields =  ('nombre', 'apellido', 'cargo')     