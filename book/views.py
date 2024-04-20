from django.shortcuts import render

# Create your views here.
def book (request):
    context={'page':'contect'}
    return render(request,'insert_data.html',context)
