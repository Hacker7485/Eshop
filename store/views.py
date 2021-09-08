from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models import Product,Category

# Create your views here.
def index(request):
    products=None
    categories = Category.objects.all()
    categoryID  = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_Categoryid(categoryID)
    else:
        products=Product.objects.all()
    data={}
    data['products']=products
    data['categories']=categories
    return render(request,'testapp/index.html',data)
    #return render(request,'testapp/base.html')

def signup(request):
    return render(request,'testapp/h.html')
