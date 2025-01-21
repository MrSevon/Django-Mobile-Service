from django.shortcuts import render, redirect
from .models import Service
from .forms import OrderForm

def home(request):
    return render(request, 'main/home.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'main/services.html', {'services': services})

def order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_success')  # Страница успеха
    else:
        form = OrderForm()
    return render(request, 'main/order.html', {'form': form})

def order_success_view(request):
    return render(request, 'main/order_success.html')