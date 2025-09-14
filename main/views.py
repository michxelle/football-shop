from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.http import HttpResponse
from django.core import serializers
from main.forms import ProductForm

def show_main(request):
    product_list = Product.objects.all()

    context = {
        'app_title': 'Footballed Co.',
        'name': 'Laudya Michelle Alexandra',
        'class': 'PBP A',
        'product_list': product_list
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        form.save()
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