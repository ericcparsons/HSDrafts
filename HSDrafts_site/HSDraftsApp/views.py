from django.shortcuts import render

def index(request):
    return render(request, 'HSDraftsApp/home.html')

def contact(request):
    return render(request, 'HSDraftsApp/basic.html', {'content':['Contact us here:', 'ecparsons42@gmail.com']})