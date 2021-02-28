from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('create/', views.MyCreateView.as_view(), name='create'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    path('index/', views.IndexView.as_view(), name='index'),
]