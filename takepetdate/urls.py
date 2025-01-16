"""
URL configuration for takepetdate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from takpede.views import index, signup, signin, update_profile, save_location, nearby_pets
from find_match.views import find_match, find_match_detail, like
from message.views import message, Directs, SendDirect, UserSearch, NewConversation
from notification.views import notification
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # home
    path('', index, name='index'),

    # find_match
    path('find_match/', find_match, name='find_match'),
    path('find_match/<int:user_id>/', find_match_detail, name='find_match_detail'),
    path('<int:post_id>/like', like, name='like'),

    # notif
    path('notification/', notification, name='notification'),

    # user and find_nearby
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', update_profile, name='profile'),
    path('save-location', save_location, name='save_location'),
    path('nearby_pets/', nearby_pets, name='nearby_pets'),

    # message
    path('message/', message, name='message'),
    path('direct/<username>', Directs, name='directs'),
    path('send/', SendDirect, name='send-directs'),
    path('search/', UserSearch, name="search-users"),
    path('new/<username>', NewConversation, name="conversation"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

