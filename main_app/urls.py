from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("about/", views.about, name="about"),
    path("teas/", views.teas, name="index"),
    path('teas/<int:pk>/', views.tea, name="detail"),
    path("teas/create/", views.TeaCreate.as_view(), name="teas_create"),
    path('teas/<int:pk>/update/', views.TeaUpdate.as_view(), name='teas_update'),
    path('teas/<int:pk>/delete/', views.TeaDelete.as_view(), name='teas_delete'),
    path('teas/<int:pk>/add_drink/', views.add_drink, name='add_drink'),


    path('teas/<int:cat_id>/add_photo/', views.add_photo, name='add_photo'),






    # Authentication
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),

]
