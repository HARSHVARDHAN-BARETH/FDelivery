from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Product
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import CreateUserForm, ProfileForm
# from cart.cart import Cart

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.shortcuts import get_object_or_404, redirect
# from .models import Product, Cart, CartItems


# @login_required(login_url='login')
def edit(request):
    return render(request, 'edit.html')

@login_required(login_url='login')
def profilePage(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            username = request.user.username
            messages.success(request, f'{username}, Your Profile is Updated')
            return redirect("/profile/")   
    else:
        form = ProfileForm(instance=request.user.profile)

    context = {'form': form}
    return render(request, 'edit.html', context)

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f'{username}, You are logged in.')
            return redirect("/")
        else:
            messages.info(request, 'Wrong passwrod or username')
            return redirect('/login/')
    return render(request, 'login.html')

@unauthenticated_user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Account is created.')
            return redirect('/login/')
        else:
            context = {'form': form}
            messages.info(request, 'Invalid credentials')
            return render(request, 'signin.html', context)

    context = {'form': form}
    return render(request, 'signin.html', context)

@login_required(login_url='login')
def logOut(request):
    logout(request)
    messages.info(request, 'You logged out successfully')
    return redirect('/login/')



def new(request):
    return render(request, "home.html")


def home(request):
    if request.method=="POST": 
        name=request.session.get('name')
        product=int(request.POST.get('product'))
        
        cart = request.session.get('cart')
        print('this is cart', cart)
        print('this is product', product)
        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        
        #return HttpResponse('p')  check product id in console
        return redirect('home')

    prs=Product.get_all_products()     #calliing method
    # print(prs)
    # print(request.session.get('email'))
    return render(request,'menu.html',{"product":prs})

@login_required(login_url='login')
def cart_view(request):
    cart = request.session.get('cart', {})
    print('in the cart', cart)
    print(cart.keys())
    # Get the product IDs from the cart
    product_ids = cart.keys()
    print('product ids', product_ids)
    # # Get the product IDs from the cart
    # product_ids = [str(prod_id) for prod_id in cart.keys()]
    # print('product ids', product_ids)


    product_id_to_remove = request.POST.get('remove_product_id')

    if product_id_to_remove:
            # Remove the product from the cart if it exists
        cart = request.session.get('cart', {})
        if str(product_id_to_remove) in cart:
          del cart[str(product_id_to_remove)]
          request.session['cart'] = cart
          messages.success(request, 'Product removed from the cart.')

                # Redirect to the cart view after removing the item
        return redirect('cart_view')


    
    # Fetch the products based on their IDs
    products_in_cart = Product.objects.filter(id__in=product_ids)
    # print(products_in_cart)
    
    # Create a dictionary to map product IDs to their details
    cart_with_details = {}
    for product in products_in_cart:
        cart_with_details[product.id] = {
            'name': product.name,
            'image': product.image.url,  # Assuming image is a field in your Product model
            'price': product.price,
            'quantity': cart[str(product.id)],  # Get quantity from the cart
        }
    
    # Pass the detailed product information to the cart template
    return render(request, 'cart.html', {'cart': cart_with_details})
