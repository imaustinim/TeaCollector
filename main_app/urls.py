from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tea/add', views.TeaCreate.as_view(), name='tea_create'),
    path('tea/<int:pk>/', views.tea, name="detail"),
    path('tea/<int:pk>/edit/', views.TeaUpdate.as_view(), name="tea_update"),
    path('tea/<int:pk>/delete/', views.TeaDelete.as_view(), name="tea_delete"),
]
