from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Department, Course, Order


# Create your views here.
def store(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        conf_password = request.POST['password1']

        if password == conf_password:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'Username Already Taken')
                return redirect('Store:register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Taken')
                return redirect('Store:register')

            else:
                user = User.objects.create_user(
                    username=user_name, first_name=first_name, last_name=last_name,
                    password=password, email=email
                )
                user.save()
                messages.info(request, 'Welcome')
        else:
            messages.info(request, 'Password not matched')
            return redirect('Store:register')

        return redirect('Store:login')

    return render(request, 'register.html')

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('Store:order')
        else:
            messages.info(request, 'Invalid Credential')
            return redirect('Store:login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def order(request):
    return render(request, 'order.html')


def conf_order(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        department = request.POST['department']
        department = Department.objects.get(id=department)
        course = request.POST['course']
        course = Course.objects.get(id=course)
        purpose = request.POST['purpose']
        material = request.POST.getlist('material[]')
        orders = Order(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phone=phone,
            email=email,
            address=address,
            department=department,
            course=course,
            purpose=purpose,
            material=material
        )
        orders.save()
        messages.info(request, 'Order Placed Successfully')

    depts = Department.objects.all()
    course = Course.objects.all()
    return render(request, 'conforder.html', {'depts': depts, 'courses': course, })