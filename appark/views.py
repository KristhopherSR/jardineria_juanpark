from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm, CustomUserCreationForm

def home(request):
    productos = Producto.objects.all()
    return render(request, 'home.html', {'productos': productos})

def contact(request):
    return render(request, 'contact.html')

def product_list(request):
    productos = Producto.objects.all()
    return render(request, 'product_list.html', {'productos': productos})

def add_product(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductoForm()
    return render(request, 'add_product.html', {'form': form})

def edit_product(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'edit_product.html', {'form': form})

def delete_product(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('product_list')

def login_view(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def cart(request):
    cart_ids = request.session.get('cart', [])
    productos = Producto.objects.filter(id__in=cart_ids)
    total = sum(producto.precio for producto in productos)
    context = {
        'productos': productos,
        'total': total,
    }
    return render(request, 'cart.html', context)

def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])
    if product_id not in cart:
        cart.append(product_id)
        request.session['cart'] = cart
    return redirect('product_list')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', [])
    if product_id in cart:
        cart.remove(product_id)
        request.session['cart'] = cart
    return redirect('cart')

