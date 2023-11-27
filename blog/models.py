from django.db import models

# tabla de personal del geriatrico
class Personal (models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cargo = models.CharField(max_length=20)
    
    def __str__(self):
       return self.nombre, self.apellido
       

#Tabla de internos del geriatrico    
class Interno (models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    numero_cedula = models.IntegerField()
    edad = models.IntegerField()
    contacto_emergencia = models.IntegerField()
    
    def __str__(self):
       return self.nombre, self.apellido

#Tabla del doctor
class Doctor (models.Model):
    Nombre = models.CharField(max_length=30)
    Apellido = models.CharField(max_length=30)
    Especialidad= models.CharField(max_length=30)    
    
    def __str__(self):
       return self.Nombre, self.Apellido, self.Especialidad


#Tabla del historial medico de los internos   
class Historial_medico (models.Model):
    
    #Tupla para los tipos de sangre en historial medico
    STATUS_sangre= (
    ('O+', 'O POSITIVO'),
    ('O-', 'O NEGATIVO'),
    ('A+', 'A POSITIVO'),
    ('A-', 'A NEGATIVO'),
    ('AB+', 'AB POSITIVO'),
    ('AB-', 'AB NEGATIVO'),
    ('B+', 'B POSITIVO'),
    ('B-', 'B NEGATIVO'),
    )  
    
    Interno_Historial = models.ForeignKey(Interno, on_delete=models.CASCADE)
    Tipo_Sangre = models.CharField(choices=STATUS_sangre, max_length=3)
    Contacto_Emergencia = models.IntegerField()
    Enfermedades = models.CharField(max_length=255)
    Cirugias = models.CharField(max_length=255)
    Fecha_cirugias = models.DateField()
    
    def __str__(self) :
       return self.Interno_Historial, self.Tipo_Sangre, self.Contacto_Emergencia, self.Cirugias, self.Fecha_cirugias, self.Enfermedades
   
    


#tabla del medicamento de los internos    
class Medicamento (models.Model):
    
    Interno_medicamento = models.ForeignKey(Interno, on_delete=models.CASCADE)
    Nombre_medicamento = models.CharField(max_length=30)
    recomendaciones =models.CharField(max_length=150)
    
    def __str__(self):
        return self.Nombre_medicamento


#Tabla mesnualidad
class Mensualidad (models.Model):
    
    #Tupla para metodos de pago de la tabla mensualidad  
    STATUS_PAGO = (
    ('e','Efectivo'),
    ('TC','Tarjeta de credito'),
    ('TD','Tarjeta de debito'),
    ('pse','Pse'),
    ('c','Cheque'), 
    ('cb','Consignacion bancaria'),
)

    Interno_mesualidad = models.ForeignKey(Interno, on_delete=models.CASCADE)
    Valor_pago = models.DecimalField(max_digits=8, decimal_places=2)
    Metodo_pago = models.CharField(choices=STATUS_PAGO, max_length=20)
    
    def __str__(self):
       return self.Interno_mesualidad
 
#Tabla habitacion
class Habitacion (models.Model):
    
    Interno_habitacion = models.ForeignKey(Interno, on_delete=models.CASCADE)
    Numero_habitacion = models.IntegerField()
    
    def __str__(self):
        return self.Numero_habitacion
    
    