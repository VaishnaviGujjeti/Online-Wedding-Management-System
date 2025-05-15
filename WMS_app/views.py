from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, Service, City, Booking, Contact
from .forms import BookingForm, ContactForm, RegisterForm
from django.urls import reverse  # Add this import
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def services(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
        services = Service.objects.filter(category=category)
    except Category.DoesNotExist:
        services = Service.objects.none()  # Return empty queryset if category doesn't exist
    return render(request, 'services.html', {'services': services, 'category': category})


from django.contrib import messages  # Add this at the top

def booking(request):
    service_id = request.GET.get('service_id')
    initial_data = {}
    
    if service_id:
        try:
            service = Service.objects.get(id=service_id)
            initial_data['service'] = service
        except Service.DoesNotExist:
            initial_data = {}

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
            
        form = BookingForm(request.POST, initial=initial_data)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            try:
                booking.save()
                messages.success(request, "Booking confirmed successfully!")  # Add success message
                return redirect('home')  # Redirect to home page
            except Exception as e:
                form.add_error(None, f"Error saving booking: {e}")
        else:
            print(f"Form errors: {form.errors}")
    else:
        form = BookingForm(initial=initial_data)

    return render(request, 'booking.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')


def logout_view(request):
    print(f"Logging out user: {request.user}")  # Debug
    logout(request)
    print(f"User after logout: {request.user}")  # Should be AnonymousUser
    return redirect('home')