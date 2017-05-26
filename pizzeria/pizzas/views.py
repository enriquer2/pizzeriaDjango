from django.shortcuts import render

from django.http import HttpResponse
# from django.template import loader  -- Al utilizar render no hace falta
from pizzas.models import Pizza
from django.http import Http404

# Create your views here.

def index(request):
    pizza_list = Pizza.objects.all()
    # # html = ''
    # # for pizza in pizza_list:
    # #     url = '/pizzas/' + str(pizza.id) + '/'
    # #     html += '<a href="' + url + '">' + pizza.name + '</a><br>'
    # template = loader.get_template('pizza/index.html')
    context = {
        'pizza_list': pizza_list
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'pizza/index.html', context)

def detail(request, pizza_id):
    try:
        pizza = Pizza.objects.get(pk=pizza_id)
    except Pizza.DoesNotExist:
        raise Http404("Esta pizza no existe")
    #return HttpResponse("<h2> Detalles de la pizza " + str(pizza_id) + "</h2>")
    # context = {
    #     'pizza': pizza
    # }
    return render(request, 'pizza/detail.html', {'pizza': pizza})

def conocenos(request):
    return HttpResponse("<h1>Pizzeria</h1><h3>Pizzeria tradicional familiar, con grandes recetas<h3>")

def fichero(request):
    template = loader.get_template('pizza/fichero.html')
    context = {}
    return HttpResponse(template.render(context, request))
