from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.test2, name='test2'),
    path('xyz/', views.xyz, name='xyz'),
    path('test/', views.test, name='test'),
    path('product/', views.product, name='product'),
    path('add/', views.add, name='add')
]