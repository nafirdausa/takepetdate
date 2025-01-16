from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from takpede.models import CustomUser
from django.http import JsonResponse, HttpResponseRedirect
from .models import Likes, Post
from notification.models import Notification
from django.urls import reverse

# Create your views here.
@login_required
def find_match(request):
    user = request.user

    users = CustomUser.objects.filter(is_superuser=0).exclude(id=request.user.id)
    posts = Post.objects.filter(
        user__is_superuser=0,
    ).exclude(user=request.user)

    for post in posts:
        # Tambahkan atribut sementara u/ template
        post.is_liked_by_user = post.post_likes.filter(user=user).exists()

    return render(request, 'apps/find_match.html', {'users':users, 'posts': posts})

@login_required
def find_match_detail(request, user_id):
    user = CustomUser.objects.get(pk = user_id)
   
    return render(request, 'apps/find_match_detail.html', {'user':user})



def like(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    current_likes = post.likes
    liked = Likes.objects.filter(user=user, post=post)

    if not liked.exists():
        # Jika belum like, add like
        Likes.objects.create(user=user, post=post)
        current_likes += 1
        
        # Tambahkan notip (only if user yang like berbeda dari pemilik post)
        if post.user != user:
            Notification.objects.create(
                user=post.user,  # Pemilik post yang get notip
                table_name="like",
                table_id=post.id,  # ID dari post
                message=f"{user.username} liked your post."  # Pesan notip
            )
    else:
        # Jika sudah like, hapus like lgi
        liked.delete()
        current_likes -= 1

    # Update jumlah likes di post
    post.likes = current_likes
    post.save()

    return redirect('find_match')
