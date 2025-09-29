from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from main.forms import ProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'app_title': 'Footballed Co.',
        'name': 'Laudya Michelle Alexandra',
        'class': 'PBP A',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('main:show_main')
    
    context = {
        'form': form,
        'app_title': 'Footballed Co.',
        'name': 'Laudya Michelle Alexandra',
        'class': 'PBP A',
    }
    return render(request, "create_product.html", context)

def show_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
        'app_title': 'Footballed Co.',
        'name': 'Laudya Michelle Alexandra',
        'class': 'PBP A',
    }
    return render(request, "product_detail.html", context)

def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')
    
    context = {
        'form': form,
        'app_title': 'Footballed Co.',
        'name': 'Laudya Michelle Alexandra',
        'class': 'PBP A'
    }

    return render(request, "edit_product.html", context)

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    else:
        form = UserCreationForm()
    
    context = {
        'form': form,
        'app_title': 'Footballed Co.',
        'name': 'Laudya Michelle Alexandra',
        'class': 'PBP A',
    }
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse('main:show_main'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
    context = {
        'form': form,
        'app_title': 'Footballed Co.',
        'name': 'Laudya Michelle Alexandra',
        'class': 'PBP A',
    }
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def show_xml(request):
    products_list = Product.objects.all()
    data = serializers.serialize("xml", products_list)
    return HttpResponse(data, content_type="application/xml")

def show_json(request):
    products_list = Product.objects.all()
    data = serializers.serialize("json", products_list)
    return HttpResponse(data, content_type="application/json")

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        data = serializers.serialize("xml", product_item)
        return HttpResponse(data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
def show_json_by_id(request, product_id):
    try:
        product_item = Product.objects.get(pk=product_id)
        data = serializers.serialize("json", [product_item])
        return HttpResponse(data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)