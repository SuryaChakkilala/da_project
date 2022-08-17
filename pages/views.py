from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterUserForm
from .models import Facility
import requests

# Create your views here.
def index(request):
    context = {}
    return render(request, 'pages/index.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username (or) Password is incorrect')

    context = {}
    return render(request, 'pages/login.html', context)

def logoutUser(request):
    if not request.user.is_authenticated:
        return redirect('home')
    messages.success(request, f'{request.user} has been succesfully logged out.')
    logout(request)
    return redirect('login')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = RegisterUserForm()
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {user}')
            return redirect('login')
        
    context = {'form': form}
    return render(request, 'pages/register.html', context)

def facilities(request):
    facs = Facility.objects.filter()
    v_f = facs.filter(type="Vehicle")
    c_f = facs.filter(type="Cargo")
    g_f = facs.filter(type="Goods")
    context = {'v_list': v_f, 'c_list': c_f, 'g_list': g_f}
    return render(request, 'pages/facilities.html', context)

def facility(request, id):
    fac = Facility.objects.get(id=id)
    context = {
        'id': id,
        'name': fac.name,
        'address': fac.address,
        'type': fac.type,
        'image': fac.imageURL
    }
    return render(request, 'pages/facility.html', context)

def delete_facility(request, id):
    fac = Facility.objects.get(id=id)
    fac.delete()
    rest_demo(request.user.id, id)
    return redirect('facilities')

def faq_form(request):
    context = {}
    return render(request, 'pages/faq.html', context)

def rest_demo(uid, fid):
    # response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    # geodata = response.json()
    # return render(request, 'pages/demo.html', {
    #     'ip': geodata['title'],
    #     'country': geodata['body']
    # })

    response = requests.post('*****' + str(uid) + '/' + str(fid))
    data = response.json()
    return redirect('facilities')