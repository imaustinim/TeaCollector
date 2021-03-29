from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tea/add', views.add_tea, name='Add Tea'),
    path('tea/<int>:tea_id', views.tea, name='teas'),
    path('tea/submit', views.tea_submit, name='teas'),
]
