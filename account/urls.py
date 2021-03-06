from django.urls import path
from . import views
from images.views import image_list
app_name = 'account'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('edit/', views.edit, name='edit'),
    path('user/follow/', views.user_follow, name='user_follow'),
    path('password_change/', views.password_change, name='password_change'),
    path('password_change_done/', views.password_change_done),
    path('manage_access/', views.manage_access),
    path('contact_history/', views.contact_history),
    path('privacy_and_security/', views.privacy_and_security),
]