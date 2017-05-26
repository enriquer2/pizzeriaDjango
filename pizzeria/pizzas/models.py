from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(verbose_name=_("Nombre"), max_length=100)
    price = models.DecimalField(verbose_name=_("Precio"), max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(verbose_name=_("Nombre"), max_length=100)
    ingredients = models.ManyToManyField("pizzas.Ingredient", verbose_name=_("Ingredientes"), related_name="pizzas")
    image = models.ImageField(null=True, blank=True)
    ## description = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    text = models.CharField(max_length=140)
    created = models.DateTimeField(auto_now_add=True)
    #score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    score = models.IntegerField(default=0)
    pizza = models.ForeignKey(Pizza, related_name="comments", default=False)

    def save(self, *args, **kwargs):
        if self.score > 5:
            self.score = 5
        elif self.score < 0:
            self.score = 0
        super(Comment, self).save(*args, **kwargs)

    def __str__(self):
        return self.text

        
class Bebida(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    pizza = models.OneToOneField(Pizza, null=True)

    def __str__(self):
        return self.name