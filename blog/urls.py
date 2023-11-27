from django.urls import path
from .views import *

app_name="Geriatrico"

#Dirigimos las url para su uso entre ellas
urlpatterns = [
    path('', BloglistView.as_view(), name="home"),
    path('Internos/', InternoCreateView.as_view(), name = "Internos"),
    path('Doctor/', DoctorCreateView.as_view(), name = 'Doctores'),
    path('Historial/', HistorialHistorialView.as_view(), name = 'Historial'),
    path('personal/,', PersonalView.as_view(), name = 'Personal')
]
