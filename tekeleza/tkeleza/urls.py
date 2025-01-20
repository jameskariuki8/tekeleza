from django.urls import path, include
from django.contrib.auth import views as auth_views
from . views import login_view, custom_logout
from . import views

urlpatterns = [
    path('', views.my_view, name='my_view'),
    path('accounts/', include('allauth.urls')),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', custom_logout, name='logout'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
     path('contact_us', views.contact_us, name='contact_us'),
    
]
