from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from takpede.models import CustomUser

# Create your views here.
@login_required
def find_match(request):
    users = CustomUser.objects.filter(is_superuser=0).exclude(id=request.user.id)
    

    return render(request, 'apps/find_match.html', {'users':users})

@login_required
def find_match_detail(request, user_id):
    user = CustomUser.objects.get(pk = user_id)
    return render(request, 'apps/find_match_detail.html', {'user':user})