from django.urls import path, include
from django.contrib.auth import views as auth_views
from . views import login_view, custom_logout, article_list
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
    path('forgot-password/', auth_views.PasswordResetView.as_view(
        template_name='tkeleza/forgot_password.html',
        email_template_name='tkeleza/password_reset_email.html',
        success_url='/forgot-password/done/'
    ), name='password_reset'),
    
    path('forgot-password/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='tkeleza/forgot_password_done.html'
    ), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='tkeleza/password_reset_confirm.html',
        success_url='/reset/done/'
    ), name='password_reset_confirm'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='tkeleza/password_reset_complete.html'
    ), name='password_reset_complete'),
    path('article_list', views.article_list, name='article_list'),
]
