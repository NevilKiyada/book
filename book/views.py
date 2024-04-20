from django.shortcuts import render

# Create your views here.
def book (request):
    if request.method == 'POST':
        data=request.POST
        book_title=data.get('book_title')
        book_description=data.get('book_description')
        print ("book description=",book_description)

        print ("book Name",book_title)

        
    context={'page':'contect'}
    return render(request,'insert_data.html',context)
