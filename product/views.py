from django.shortcuts import render

from product.models import Category

# Create your views here.
def getCategories(request):
    categories=Category.objects.all()
    print(categories)
    return render(request,'product.html')
