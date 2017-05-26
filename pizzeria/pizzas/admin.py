from django.contrib import admin

from pizzas.models import Ingredient, Pizza, Bebida, Comment
# Register your models here.

admin.site.register(Ingredient)
admin.site.register(Pizza)
admin.site.register(Bebida)
admin.site.register(Comment)