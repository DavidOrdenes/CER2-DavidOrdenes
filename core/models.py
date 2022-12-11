from django.db import models


class Matrona (models.Model):
    nombre = models.CharField(max_length=30,null=False,blank=False)
    primerapellido = models.CharField(max_length=30,null=False,blank=False)
    segundoapellido = models.CharField(max_length=30,null=True,blank=True)
    cargo = models.CharField(max_length=20,null=False,blank=False,choices=[("Matrona Jefe","Matrona Jefe"),("Matrona General","Matrona General")])
    run = models.CharField(max_length=10,null=False,blank=False)
    contraseña = models.CharField(max_length=15,null=False)

    def __str__(self) -> str:
        return "%s %s, %s" % (self.nombre, self.primerapellido, self.cargo)

class Padre(models.Model):
    run = models.CharField(max_length=10,null=True,blank=True)
    pasaporte = models.CharField(max_length=30, null=True,blank=True)
    nombre = models.CharField(max_length=30,null=False,blank=False)
    primerapellido = models.CharField(max_length=30,null=False,blank=False)
    segundoapellido = models.CharField(max_length=30,null=True,blank=True)
    correo = models.EmailField(null=False,blank=False)
    telefono = models.CharField(max_length=30,null=False,blank=False)
    contraseña = models.CharField(max_length=15,null=False)

    def __str__(self) -> str:
        return "%s %s" % (self.nombre,self.primerapellido)

altas = [("Fallecimiento","Fallecimiento"),("Traslado","Traslado"),("Retorno a Hogar","Retorno a Hogar")]

class RecienNacido (models.Model):
    fecha_nacimiento = models.DateField(null=False,blank=False)
    nombre = models.CharField(max_length=30,null=False,blank=False)
    primerapellido = models.CharField(max_length=30,null=False,blank=False)
    segundoapellido = models.CharField(max_length=30,null=True,blank=True)
    peso = models.IntegerField(null=False,blank=False)
    altura = models.IntegerField(null=False,blank=False)
    sexo = models.CharField(max_length=1,null=False,blank=False,choices=[("H","Hombre"),("M","Mujer")])
    direccion = models.CharField(max_length=30)
    run = models.CharField(max_length=30,null=True,blank=True)
    tipo_alta = models.CharField(max_length=20,null=True,blank=True,choices=altas)
    fecha_alta = models.DateField(auto_now=True,null=True,blank=True)
    padres = models.ForeignKey(Padre,on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return "%s %s, %s" % (self.nombre,self.primerapellido,self.sexo)  

class Seguimiento(models.Model):
    peso_diario = models.IntegerField(null=False,blank=False)
    tolerancia_alimentaria = models.CharField(max_length=30,null=False,blank=False)
    orina = models.CharField(max_length=1,null=False,blank=False)
    deposicion = models.CharField(max_length=1,null=False,blank=False)
    sector_sala = models.CharField(max_length=3,null=False,blank=False,choices=[("UTI","UTI"),("UCI","UCI")])
    n_cupo = models.CharField(max_length=5,null=False,blank=False)
    fecha = models.DateField(auto_now=True,null=False,blank=False)
    observacion = models.CharField(max_length=120,null=True,blank=True)
    matrona = models.ForeignKey(Matrona,on_delete=models.RESTRICT)
    recien_nacido = models.ForeignKey(RecienNacido,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "%s, %s %s" % (self.recien_nacido.nombre,self.sector_sala, self.n_cupo)


