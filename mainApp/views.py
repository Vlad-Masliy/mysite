from django.shortcuts import render

def index(request):
    return render(request, 'mainApp/homePage.html')

def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['My phone number:' , '+380965956540 - Maslii Vladyslav']})

def vavilon(request):
    return render(request, 'mainApp/vavilon.html')

def baffetologic(request):
    return render(request, 'mainApp/baffetologic.html')

def uorrenbaffet(request):
    return render(request, 'mainApp/uorrenbaffet.html')

def father(request):
    return render(request, 'mainApp/father.html')

def think(request):
    return render(request, 'mainApp/think.html')

def master(request):
    return render(request, 'mainApp/master.html')

def money(request):
    return render(request, 'mainApp/money.html')