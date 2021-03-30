from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tea/add', views.add, name='Add Tea'),
    path('tea/<int:tea_id>/edit/', views.edit),
    path('tea/<int:tea_id>/delete/', views.delete),
    path('tea/<int:tea_id>/', views.tea),
]
