from django.urls import path

from . import views

app_name = 'score'

urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('create/', views.MyCreateView.as_view(), name='create'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('result/', views.ResultView.as_view(), name='result'),
]