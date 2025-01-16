from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'no_hp', 'spesies', 'alamat', 'umur', 
            'jenis_hewan', 'jenis_kelamin', 'short_deskripsi', 
            'deskripsi', 'foto', 'latitude', 'longitude'
        ]
        widgets = {
            'alamat': forms.TextInput(attrs={'class': 'input input-bordered'}),
            'umur': forms.NumberInput(attrs={'class': 'input input-bordered'}),
            'no_hp': forms.NumberInput(attrs={'class': 'input input-bordered'}),
            'spesies': forms.TextInput(attrs={'class': 'input input-bordered'}),
            'short_deskripsi': forms.TextInput(attrs={'class': 'input input-bordered'}),
            'deskripsi': forms.Textarea(attrs={'class': 'textarea textarea-bordered'}),
            'jenis_hewan': forms.Select(choices=[('Anjing', 'Anjing'), ('Kucing', 'Kucing')]),
            'jenis_kelamin': forms.Select(choices=[('Jantan', 'Jantan'), ('Betina', 'Betina')]),
            # tambahkan class Tailwind lainnya sesuai kebutuhan
        }