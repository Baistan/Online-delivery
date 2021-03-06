from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
# from Django.core.exception import ObjectDoesNotExist
from .forms import OrderForm, UserProfile
from .filters import OrderFilterSet
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomerRegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .decorators import *


@unauth_user
def register(request):
    form = CustomerRegisterForm
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='customer')
            Customer.objects.create(user=user,full_name=user.username)
            user.groups.add(group)
            messages.success(request,message='Success Registration')
            return redirect('home')
    context = {'form':form}
    return render(request,'store/register.html',context)


def user_page(request):
    orders = request.user.customer.order_set.all()

    context = {'orders':orders}
    return render(request,'store/user_page.html',context)


@unauth_user
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        login(request,user)
        if user is not None:
            login(request, user)
            return redirect('home')
    context = {}
    return render(request, 'store/login.html', context)



@login_required(login_url='login')
@admin_only
def home_page(request):
    orders_count = Order.objects.all().count()
    delivered = Order.objects.filter(status='Delivered').count()
    pending = Order.objects.filter(status='Pending').count()
    not_delivered = Order.objects.filter(status="Not delivered").count()
    customers = Customer.objects.all()
    orders = Order.objects.all()
    context = {'orders': orders,'customers': customers,'orders_count':orders_count,'pending':pending,'delivered':delivered,'not_delivered':not_delivered}
    return render(request,'store/home.html',context)


def logout_page(request):
    logout(request)
    return redirect('login')


def products_page(request):
    products =  Product.objects.all()
    context = {'products': products}
    return render(request,'store/product.html',context)

@admin_only
def customer_page(request,pk):
    try:
        customer = Customer.objects.get(id=pk)
        orders = customer.order_set.all()
        orders_count = orders.count()
        filterset = OrderFilterSet(request.GET,queryset=orders)
        orders = filterset.qs # Обращаемся к классу Model


        context = {'customer':customer,'orders':orders,'orders_count':orders_count,'filterset':filterset}
        return render(request,'store/customer.html',context)
    except:
        return HttpResponse('Выйди и зайди обратно!!!')

def create_order(request,pk):
    OrderFormSet = inlineformset_factory(Customer,Order,fields=('product','status'))
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(instance=customer)
    if request.method == 'POST':
        formset = OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset':formset,'customer':customer}
    return render(request,'store/order_form.html',context)

def update_order(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'store/order_form.html',context)


def account_settings(request):
    user =request.user.customer
    form = UserProfile(instance=user)
    if request.method == 'POST':
        form = UserProfile(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'store/account.html',context)

def delete_order(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'order':order}
    return render(request,'store/delete.html',context)
