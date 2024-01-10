from django.shortcuts import render, redirect
# install HttpResponse
from django.http import HttpResponse
from .models import *
from .forms import ProductForm
# Create your views here.
# After creating a view then import them into the urls.py page in accounts


def home(request):
    # returning a template
    #print(request)
    product = Product.objects.all()
    context = {'products': product}
    return render(request, 'accounts/dashboard.html', context)


def addProduct(request):
    #print(request)
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    context = {'form': form}
    return render(request, 'accounts/product_form.html', context)


def editEntry(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect(home)
    context = {'form': form}
    #print(context)
    # print(context['product'].product_Name)
    return render(request, 'accounts/product_form.html', context)


def deleteEntry(request, id):
    Product.objects.get(id=id).delete()
    return redirect(home)
