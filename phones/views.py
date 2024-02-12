from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    name_sort = request.GET.get("sort")
    
    if name_sort == 'name':
        phone_objects = Phone.objects.all().order_by('name')
    elif name_sort == 'min_price':
        phone_objects = Phone.objects.all().order_by('price')
    elif name_sort == 'max_price':
        phone_objects = Phone.objects.all().order_by('-price')
    else:
        phone_objects = Phone.objects.all()    
    phones = [i for i in phone_objects]
    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug= slug)
    phone_value = phone.values()
    context = {
        'phone': phone_value[0],
    }
    return render(request, template, context)
