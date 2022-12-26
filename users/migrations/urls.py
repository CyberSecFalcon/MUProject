# In the urls.py file within your app (users/urls.py), define URL patterns for each of the views that you created:

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('corporate_signup/', views.corporate_signup, name='corporate_signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
]
