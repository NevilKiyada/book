from django.shortcuts import render ,redirect
from .models import *

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
