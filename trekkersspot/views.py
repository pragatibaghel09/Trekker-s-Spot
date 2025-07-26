from django.shortcuts import render, redirect
from .models import *
# from django.http import HttpResponse
# from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'home.html')



def registration(request):

    if request.method == 'POST':
          post = Registration()
          post.full_name = request.POST['full_name']
          post.mo_num = request.POST['mo_num']
          post.email = request.POST['email']
          post.gender = request.POST['gender']
          post.age = request.POST['age']
          post.height = request.POST['height']
          post.weight = request.POST['weight']
          post.password1 = request.POST['password1']
          post.password2 = request.POST['password2']
          

          if post.password1 == post.password2: 
           post.save()
           return redirect('payment')
          else:
            messages.error(request,"passowrd didn't match ")
    
    return render(request,'registration.html')  


def aboutus(request):
    return render(request, 'aboutus.html')


def HPT(request):
    return render(request, 'HPT.html')


def contactus(request):
    return render(request, 'contactus.html')



def payment(request):
    
    if request.method == 'POST':
          post =  Payment()
          post.full_name = request.POST['full_name']
          post.mo_num = request.POST['mo_num']
          post.email = request.POST['email']
          post.acnum = request.POST.get('acnum', False)
          post.card_type = request.POST.get('card_type', False)
          post.card_num = request.POST.get('card_num', False)
          post.cvv = request.POST.get('cvv', False)
          
          post.save()
          return redirect ('sucess')
    return render(request,'payment.html')


def sucess(request):
    return render(request,'sucess.html')

def alltreks(request): 
    return render(request,'alltreks.html') 

def feedback(request):
    
     
    if request.method == 'POST':
          post =  Feedback()
          post.fname = request.POST['fname']
          post.Email = request.POST['Email']
          post.Trektrip = request.POST['Trektrip']
          post.suggestions = request.POST['suggestions']
          
          post.save()
          return redirect('home')
    return render (request,'feedback.html')
   
   
   

   
   
   
