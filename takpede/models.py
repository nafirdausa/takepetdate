from django.db import models
# make model pengguna kustom
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128) 
    
    # Atribut tambahan
    no_hp = models.CharField(max_length=15, null=True, blank=True)
    spesies = models.CharField(max_length=100, null=True, blank=True)
    alamat = models.TextField(null=True, blank=True)
    umur = models.IntegerField(null=True, blank=True)
    jenis_hewan = models.CharField(
        max_length=10, 
        null=True, 
        blank=True,
        choices=[('Anjing', 'Anjing'), ('Kucing', 'Kucing')]
    )
    jenis_kelamin = models.CharField(
        max_length=10, 
        null=True, 
        blank=True,
        choices=[('Jantan', 'Jantan'), ('Betina', 'Betina')]
    )
    short_deskripsi = models.CharField(max_length=60, null=True, blank=True)
    deskripsi = models.TextField(null=True, blank=True)
    foto = models.ImageField(upload_to='user_photos/', null=True, blank=True)
    status_kesehatan = models.ImageField(upload_to='user_health/', null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.username