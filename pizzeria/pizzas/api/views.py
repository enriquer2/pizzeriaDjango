from rest_framework import viewsets

from pizzas.api.serializers import IngredientSerializer, PizzaSerializer, BebidaSerializer, CommentSerializer
from pizzas.models import Ingredient, Pizza, Bebida, Comment

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [
        # Ejemplo de permiso para usuario logeado: IsAuthenticated
    ]

class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = []

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = []

class BebidaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bebida.objects.all()
    serializer_class = BebidaSerializer
    permission_classes = []
    