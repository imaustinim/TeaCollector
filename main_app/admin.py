from django.contrib import admin
from .models import Tea, Ingredients, Tea_Type, Photo
# Register your models here.

admin.site.register(Tea)
admin.site.register(Ingredients)
admin.site.register(Tea_Type)
admin.site.register(Photo)
