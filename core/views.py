from django.core import paginator
from django.shortcuts import render
from django.core .paginator import Page, Paginator
# Create your views here.
from .models import Products
def index(request):
    print("making the request")
    product = Products.objects.all()
    product_objects = Products.objects.all()

     #search
    item_name = request.GET.get("item_name")
    if item_name !='' and item_name is not None:
        product_objects=product_objects.filter(title__icontains=item_name)
        #paginator
    paginator=Paginator(product_objects, 4)
    page= request.GET.get('page')
    product_objects=paginator.get_page(page)
    # print(len(product))
    print(product[0].image) 
    return render(request, 'base.html',{'products': product})
    #Getting the details for each product using id
def detail(request, id):
    product_object= Products.objects.get(id=id)
    return render(request, 'base.html',{'product_object': product_object})
