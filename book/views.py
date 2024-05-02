from django.shortcuts import render ,redirect
from .models import *
from django.http import HttpResponse
#for user model maintaining user record
from django.contrib.auth.models import User
#for give message user alredy existing
from django.contrib import messages

# Create your views here.
#function name is passed in url.py in path 
def get_book (request):
    #catch data from insert_data.html
    if request.method == 'POST':
        data=request.POST
        bi=request.FILES.get('bi')
        bt=data.get('bt')
        bd=data.get('bd')
        #data going into models 
        Book.objects.create(
            book_image=bi,
            book_title=bt,
            book_description=bd,
        )
        #it is use for redirect that page without popup mess for continue or cancel 
        return redirect('/book/')

    q1=Book.objects.all()
    #search_text have input or not that is check by if 
    if request.GET.get('Search_book'):

        #compare with all objects if match than return that object otherwise give all objects
        q1=q1.filter(book_title__icontains = request.GET.get('Search_book'))
        print(request.GET.get('Search_book'))

    context={'page':'contect','book':q1}
    return render(request,'insert_data.html',context)

def delete_book(request,id):
    print (id)
    qurry=Book.objects.get(id=id)
    qurry.delete()
    return redirect('/book/')


def update_book(request,id):
    qurry=Book.objects.get(id=id)
    if request.method == 'POST':

        data=request.POST
        bt=data.get('bt')
        bd=data.get('bd')
        bi=request.FILES.get('bi')

        qurry.book_title=bt
        qurry.book_description=bd
        if bi:
            qurry.book_image=bi

        qurry.save()
        return redirect('/book/')    

    print (id)
    
    context={"book":qurry}
    
    return render(request,'update_book.html',context)


def login(request):
    return render(request,'login.html')


def Ragister(request):
    if request.method == 'POST':
        #catch all data frome form to an variables
        First_name = request.POST.get('fn')
        Last_name = request.POST.get('ln')
        Username= request.POST.get('un')
        Email= request.POST.get('email')
        Password= request.POST.get('password')

        #for find user name alredy existing
        same_uname=User.objects.filter(username=Username)
        #if exists give a message to ragister form
        if same_uname.exists():
            messages.info(request, "User name already exists")
            return redirect('/Ragister/') 



        #give value to objects of User model by using variables
        user= User.objects.create(
            first_name=First_name,
            last_name=Last_name,
            username=Username,
            email = Email
        )
        user.set_password(Password)
        user.save()
        messages.info(request, "Account Created successfully") 

        return redirect ('/Ragister/')
    return render(request,'ragister.html')