from django.shortcuts import render
from django.http import HttpResponse
from .models import Customers


def index(request):

    return render(request, 'feedbackapp/index.html')


def about(request):
    return HttpResponse('We are at About')


def thanks(request):
    name = request.POST.get('customer_name', 'None')
    email = request.POST.get('customer_email', 'None')
    rating = request.POST.get('rating', -1)
    time = request.POST.get('time_taken', -1)
    suggestions = request.POST.get('suggestion', 'None')
    print(name)
    print(email)
    print(rating)
    print(time)
    print(suggestions)
    c = Customers(name=name, email = email, rating=rating, time_taken=time, suggestion=suggestions)
    c.save()
    return render(request, 'feedbackapp/thanks.html')
