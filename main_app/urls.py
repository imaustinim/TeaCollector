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
    path('teas/<int:pk>/associate_ingredient/<int:fk>/', views.associate_ingredient, name='assoc_ingredient'),
    path('teas/<int:pk>/unassociate_ingredient/<int:fk>/', views.unassociate_ingredient, name='unassoc_ingredient'),
    path('teas/<int:pk>/add_photo/', views.add_photo, name='add_photo'),
    path('ingredients/', views.IngredientsList.as_view(), name='ingredients_index'),
    path('ingredients/<int:pk>/', views.IngredientDetail.as_view(), name='ingredients_detail'),
    path('ingredients/create/', views.IngredientCreate.as_view(), name='ingredients_create'),
    path('ingredients/<int:pk>/update/', views.IngredientUpdate.as_view(), name='ingredients_update'),
    path('ingredients/<int:pk>/delete/', views.IngredientDelete.as_view(), name='ingredients_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
]
