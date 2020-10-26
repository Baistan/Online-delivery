from django.shortcuts import render

def home_page(request):
    return render(request,'store/home.html')
def products_page(request):
    return render(request,'store/product.html')
def customer_page(request):
    return render(request,'store/customer.html')
