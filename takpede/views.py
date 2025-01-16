from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser
from .forms import CustomUserCreationForm
from .forms import UpdateProfileForm
from .utilities import calculate_distance
from django.http import JsonResponse
from geopy.distance import geodesic  # Untuk hiitung jarak



# Create your views here.

def index(request):
    return render(request, 'apps/index.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('find_match')
    else:
        form = CustomUserCreationForm()

    return render(request, 'apps/signup.html', {'form':form})

def signin(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Current logged-in user:", request.user)
            return redirect('find_match')
        else:
            messages.error(request, 'Username atau Password salah')
    return render(request, 'apps/signin.html')




@login_required
def update_profile(request):
    user = request.user  # get user yang sedang login
    if request.method == "POST":
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # Cek jika request datang dari fetch (AJAX)
            latitude = request.POST.get("latitude")
            longitude = request.POST.get("longitude")
            if latitude and longitude:
                user.latitude = latitude
                user.longitude = longitude
                user.save()
                return JsonResponse({"message": "Location updated successfully!"})
        else:
            form = UpdateProfileForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                print(f"Updated Photo URL: {user.foto.url}")  # Debug
                return render(request, 'apps/profile.html', {'form': form, 'success': True})

    else:
        form = UpdateProfileForm(instance=user)

    return render(request, 'apps/profile.html', {'form': form})


@login_required
def save_location(request):
    if request.method == "POST":
        longitude = request.POST.get("longitude")
        latitude = request.POST.get("latitude")
        
        # Simpan ke database (contoh: user yang sedang login)
        user = request.user
        user.longitude = longitude
        user.latitude = latitude
        user.save()
        
        return render(request, 'apps/profile.html')


@login_required
def nearby_pets(request):
    # Get lokasi pengguna sekarang dri database
    current_user = request.user
    user_location = (current_user.latitude, current_user.longitude)

    # Get all user dg lokasi valid
    other_users = CustomUser.objects.exclude(id=current_user.id).exclude(latitude__isnull=True, longitude__isnull=True)

    # Filter pengguna berdasarkan radius tertentu
    search_radius_km = 5  # Radius dlm km
    nearby_users = []
    for user in other_users:
        other_user_location = (user.latitude, user.longitude)
        distance = geodesic(user_location, other_user_location).km
        if distance <= search_radius_km:
            nearby_users.append({
                'latitude': user.latitude,
                'longitude': user.longitude,
                'name': user.username,
            })

    # Kirim data ke template
    return render(request, 'apps/nearby_pets.html', {
        'user_latitude': current_user.latitude,
        'user_longitude': current_user.longitude,
        'nearby_pets': nearby_users,
    })
