from django.shortcuts import render

# Create your views here.

def notification(request):
    return render(request, 'apps/notification.html')