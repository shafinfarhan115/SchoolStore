
from django.urls import path
from Store import views

app_name = 'Store'
urlpatterns = [
    path('', views.store, name='store'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('order/', views.order, name='order'),
    path('logout/', views.logout, name='logout'),
    path('confirm_order', views.conf_order, name='conf_order')
]
