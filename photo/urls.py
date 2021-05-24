from django.urls import path
from . import views
urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),
    path('photo/<str:pk>/rotate_right',views.rotate_right,name="right"),
    path('photo/<str:pk>/rotate_left',views.rotate_left,name="left")
]