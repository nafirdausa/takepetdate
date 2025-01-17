from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from takpede.models import CustomUser
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponseNotAllowed

# Create your views here.


@login_required
def message(request):
    user = request.user
    messages = Message.get_message(user=request.user)
    active_direct = None
    directs = None

    
    query = request.GET.get('q')
    search_results = None
    if query:
        search_results = CustomUser.objects.filter(Q(username__icontains=query)).exclude(username=user.username)

    if messages:
        message = messages[0]
        active_direct = message['user'].username
        directs = Message.objects.filter(user=request.user, reciepient=message['user'])
        directs.update(is_read=True)

        for message in messages:
            if message['user'].username == active_direct:
                message['unread'] = 0

    context = {
        'directs': directs,
        'active_direct': active_direct,
        'messages': messages,
        'search_results': search_results,
    }
    
    return render(request, 'apps/inbox2.html', context)

@login_required
def Directs(request, username):
    user  = request.user
    messages = Message.get_message(user=user)
    active_direct = username
    directs = Message.objects.filter(user=user, reciepient__username=username)  
    directs.update(is_read=True)

    for message in messages:
            if message['user'].username == username:
                message['unread'] = 0
    context = {
        'directs': directs,
        'messages': messages,
        'active_direct': active_direct,
    }
    return render(request, 'apps/inbox2.html', context)

def SendDirect(request):
    from_user = request.user
    to_user_username = request.POST.get('to_user')
    body = request.POST.get('body')

    if request.method == "POST":
        to_user = CustomUser.objects.get(username=to_user_username)
        Message.sender_message(from_user, to_user, body)
        return redirect('message')

def UserSearch(request):
    query = request.GET.get('q')
    context = {}
    if query:
        users = CustomUser.objects.filter(Q(username__icontains=query))

        # Paginator
        paginator = Paginator(users, 8)
        page_number = request.GET.get('page')
        users_paginator = paginator.get_page(page_number)

        context = {
            'users': users_paginator,
            }

    return render(request, 'apps/search.html', context)

def NewConversation(request, username):
    from_user = request.user
    body = ''
    try:
        to_user = CustomUser.objects.get(username=username)
    except Exception as e:
        return redirect('search-users')
    if from_user != to_user:
        Message.sender_message(from_user, to_user, body)
    return redirect('message')