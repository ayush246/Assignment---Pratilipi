from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product,PostView
from django.utils import timezone

a=0

def landing(request):
    # if request.META.get('HTTP_REFERER'):
    return render(request, "products/landing.html")

def home(request):
    products = Product.objects
    return render(request, "products/home.html", {'products':products})

@login_required #if the user is not logged in and tries to access this page they are sent elsewhere

def create(request):
    if request.method=="POST":
        if request.POST['title'] and request.POST['body'] and request.POST['url']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            # validating url by adding http://
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
            product.user_current = request.user
            product.save()
            return redirect('/products/'+ str(product.id))
        else:
            return render(request, "products/create.html", {'error':'All fields are required'})
    else:
        return render(request, "products/create.html")

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.user.is_authenticated:
        PostView.objects.get_or_create(user=request.user, product=product)
    return render(request, "products/detail.html",{'product':product})

