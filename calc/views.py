from django.http import HttpResponse
from django.shortcuts import render

from .models import Food

def home(request):
    return render(request,'home.html')



def phones(request):

    return render(request,'phone_item.html')


def tablet(request):
   
    return render(request,'tablet_item.html')

def television(request):
    return render(request,'television_item.html')

def computer(request):
    return render(request,'computer_item.html')
    
def gaming(request):
    return render(request,'gaming_item.html')

def about(request):
    return render(request,'about_item.html')

def contact(request):
    return render(request,'contact_item.html')