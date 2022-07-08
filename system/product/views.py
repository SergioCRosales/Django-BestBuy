from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BbCategoriesImport
from .forms import ProductForm
# Create your views here.

def begin(request):
    return render(request, 'pages/begin.html')
def about(request):
    return render(request, 'pages/about.html')

def products(request):
    products = BbCategoriesImport.objects.all()
    return render(request, 'products/index.html', {'products': products})

def create(request):
    formulario = ProductForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('products')
    return render(request, 'products/create.html', {'formulario': formulario})

def edit(request, id):
    product = BbCategoriesImport.objects.get(id=id)
    formulario = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('products')
    return render(request, 'products/edit.html', {'formulario': formulario})

def eliminate(request, id):
    product = BbCategoriesImport.objects.get(id=id)
    product.delete()
    return redirect('products')
