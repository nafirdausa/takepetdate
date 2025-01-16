# from django.shortcuts import render
# from .models import Notification
# from takpede.models import CustomUser
# from django.contrib.auth.decorators import login_required
       

# # Create your views here.
# @login_required
# def notification(request):
#     user_notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
#     return render(request, 'apps/notification.html', {'notifications': user_notifications})


from django.shortcuts import render
from .models import Notification
from takpede.models import CustomUser
from django.contrib.auth.decorators import login_required

@login_required
def notification(request):
    # Ambil notifikasi untuk user yang sedang login
    user_notifications = Notification.objects.filter(user=request.user).order_by('-created_at')

    # Tambahkan data user terkait jika diperlukan
    for notif in user_notifications:
        try:
            notif.related_user = CustomUser.objects.get(id=notif.table_id)
        except CustomUser.DoesNotExist:
            notif.related_user = None

    return render(request, 'apps/notification.html', {'notifications': user_notifications})





