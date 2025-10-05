from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from main.forms import ProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

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

@csrf_exempt
@require_POST
def create_product_ajax(request):
    data = json.loads(request.body)
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')
    category = data.get('category')
    thumbnail = data.get('thumbnail')
    is_featured = data.get('is_featured', False)
    stock = data.get('stock')
    brand = data.get('brand')
    user = request.user if request.user.is_authenticated else None

    product = Product.objects.create(
        name=name,
        price=price,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        stock=stock,
        brand=brand,
        user=user,
    )
    return JsonResponse({"message": "CREATED"}, status=201)

@csrf_exempt
@require_POST
def update_product_ajax(request, product_id):
    data = json.loads(request.body)
    product = Product.objects.get(pk=product_id)
    product.name = data.get('name')
    product.price = data.get('price')
    product.description = data.get('description')
    product.category = data.get('category')
    product.thumbnail = data.get('thumbnail')
    product.is_featured = data.get('is_featured', False)
    product.stock = data.get('stock')
    product.brand = data.get('brand')
    product.save()
    return JsonResponse({"message": "UPDATED"}, status=200)

@csrf_exempt
@require_POST
def delete_product_ajax(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return JsonResponse({"message": "DELETED"}, status=200)

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

def login_user_ajax(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponse("Login successful", status=200)
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            return HttpResponse("Invalid credentials", status=400)
    return HttpResponse("Invalid request method", status=405)

def register_ajax(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Account created successfully", status=201)
        else:
            return HttpResponse("Invalid data", status=400)
    return HttpResponse("Invalid request method", status=405)

def show_xml(request):
    products_list = Product.objects.all()
    data = serializers.serialize("xml", products_list)
    return HttpResponse(data, content_type="application/xml")

def show_json(request):
    products_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'category_display': product.get_category_display(),
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'stock': product.stock,
            'brand': product.brand,
            'user_id': product.user_id,
        }
        for product in products_list
    ]
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        data = serializers.serialize("xml", product_item)
        return HttpResponse(data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
def show_json_by_id(request, product_id):
    try:
        product_item = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product_item.id),
            'name': product_item.name,
            'price': product_item.price,
            'description': product_item.description,
            'category': product_item.category,
            'category_display': product_item.get_category_display(),
            'thumbnail': product_item.thumbnail,
            'is_featured': product_item.is_featured,
            'stock': product_item.stock,
            'brand': product_item.brand,
            'user_id': product_item.user_id,
            'user_username': product_item.user.username if product_item.user else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)