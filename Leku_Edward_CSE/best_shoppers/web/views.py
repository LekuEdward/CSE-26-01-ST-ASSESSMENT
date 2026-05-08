from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.
def landing(request):
    return render(request, 'web/landing.html')


def dashboard(request):
    products = Product.objects.all().order_by('-id')
    form = ProductForm()
    success = request.GET.get('success', False)

    total_sales = sum(p.price * p.quantity for p in products)
    total_orders = sum(p.price for p in products)
    in_stock_value = sum(p.price * p.quantity for p in products if p.quantity > 0)
    out_of_stock_count = products.filter(quantity=0).count()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/?success=true')

    context = {
        'form': form,
        'products': products,
        'success': success,
        'total_sales': total_sales,
        'total_orders': total_orders,
        'in_stock_value': in_stock_value,
        'out_of_stock_count': out_of_stock_count,
    }
    return render(request, 'web/dashboard.html', context)