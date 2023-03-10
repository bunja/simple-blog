from django.conf import settings
from django.contrib import admin
from posts.views import homepage, post, about, search, postlist, allposts
from django.urls import path
from . import views

urlpatterns = [
    path('', homepage, name = 'homepage'),
    path('post/<slug>/', post, name = 'post'),
    path('about/', about, name = 'about' ),
    path('search/', search, name = 'search'),
    path('postlist/<slug>/', postlist, name = 'postlist'),
    path('posts/', allposts, name = 'allposts'),
]