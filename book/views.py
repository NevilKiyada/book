from django.shortcuts import render ,redirect
from .models import *
from django.http import HttpResponse

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