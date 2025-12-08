from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
  path('', views.home_view, name='home'),
  path('register/', views.register_view, name='register'),
  path('login/', views.login_view, name='login'),
  path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
  path('add-money/', views.add_money_view, name='add_money'),
  path('spend-money/', views.spend_money_view, name='spend_money'),
  path('transactions/', views.user_transactions, name='transactions'),
]