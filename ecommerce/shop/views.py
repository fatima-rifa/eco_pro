from django.shortcuts import render, redirect
from . models import Product, Cart, CartItem, Order, OrderItem
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.shortcuts import get_object_or_404


# Create your views here.




def registration(request):
    if request.method == "POST":
        username=request.POST['username']
        email = request.POST['email'] 
        password = request.POST['password'] 
        conf_pass = request.POST['conf_pass']

        if password != conf_pass: 
            return render(request, 'registration.html', {'error': 'Passwords do not match!'})
        
        if User.objects.filter(username=username).exists(): 
            return render(request, 'registration.html', {'error': 'Username already taken!'})
        
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        messages.success(request, "Account created successfully!")
        return redirect('login')
        
    return render(request,'registration.html')





def login_user(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")

        else:
            return render(request, "login.html", {
                "error": "Invalid Username or Password!"
            })

    return render(request, "login.html")





def logout_user(request):
    logout(request)
    return redirect('login')



@login_required()
def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})





@login_required
def add_to_cart(request, id):

    product = Product.objects.get(id=id)

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={"quantity": 1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart")




@login_required
def cart(request):

    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_items = CartItem.objects.filter(cart=cart)

    total = 0

    for item in cart_items:
        total += item.product.price * item.quantity

    return render(request, "cart.html", {
        "cart_items": cart_items,
        "total": total,
    })




@login_required
def remove_from_cart(request, id):
    cart = Cart.objects.get(user=request.user)

    cart_item = get_object_or_404(
        CartItem,
        id=id,
        cart=cart
    )

    cart_item.delete()

    return redirect('cart')




@login_required
def checkout(request):

    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    total = 0

    for item in cart_items:
        total += item.product.price * item.quantity

    order = Order.objects.create(
        user=request.user,
        total_amount=total
    )

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

    cart_items.delete()

    return redirect("orders")




@login_required
def buy_now(request, id):

    product = Product.objects.get(id=id)

    if request.method == "POST":

        quantity = int(request.POST["quantity"])

        total = product.price * quantity

        order = Order.objects.create(
            user=request.user,
            total_amount=total
        )

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=product.price
        )

        return redirect("orders")

    return render(request, "order.html", {
        "product": product
    })




@login_required
def orders(request):

    order_items = OrderItem.objects.filter(
        order__user=request.user
    ).order_by("-order__order_date")

    for item in order_items:
        item.total = item.price * item.quantity

    return render(request, "orders.html", {
        "order_items": order_items
    })



@login_required
def profile(request):
    return render(request, "profile.html")