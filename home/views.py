from django.shortcuts import render
from book.models import *

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse


# Create your views here.
def home(request):
    q1=Book.objects.all()
    users = User.objects.all()

    print (q1)
    print (users)
    
        
#     people=[
#         {'name': 'janvi', 'age':19},
#         {'name': 'nevil', 'age':17},
#         {'name': 'John', 'age':24},
#         {'name': 'raju', 'age':21},
#         {'name': 'james', 'age':15},
#         {'name': 'hannes', 'age':21},
#         {'name': 'alice', 'age':17},
#         {'name': 'jain', 'age':57},
#         {'name': 'kelvin', 'age':7}
#     ]
#     vn="""Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cum doloremque officiis non molestias quas, nemo itaque aliquam expedita fugiat quam et quaerat laborum quo. Est quae eveniet pariatur accusantium voluptatibus nesciunt eaque aut alias odio asperiores. Tempore dignissimos sequi reprehenderit. Saepe iure provident nulla dolor deleniti? Voluptas nisi architecto, libero eos exercitationem cum, dolorum eum, blanditiis repudiandae autem est numquam! Eaque voluptatibus sed eius magni numquam! Perspiciatis nihil, deleniti aliquid consectetur magni nisi tempore expedita quidem soluta. Quidem culpa, commodi illum, animi expedita debitis corporis sequi distinctio esse ratione totam consequatur! Ipsa incidunt natus esse doloremque libero minus sit odit?
# """
    return render(request,"index.html", context={'page':'welocome', 'book':q1,'user':users})

def help(request):
    print ("1*" * 10)
    return HttpResponse(" this for help purposes")

def about(request):
    context={'page':'about'}
    return render(request, 'about.html', context)

def contect(request):
    context={'page':'contect'}
    return render(request, 'contect.html',context)