"""
URL configuration for janvi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from book.views import *
from home.views import *
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from janvi import settings
urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contect/',contect,name='contect'),
    path('help',help,name='help'),
    path('book/',get_book,name='book'),

    
    path('delete_book/<id>',delete_book,name='delete_book'),
    path('update_book/<id>',update_book,name='update_book'),

    path('Ragister/',Ragister,name='Ragister'),
    path('login/' ,login_page,name='login'),
    path('logout/' ,logout_page,name='logout'),
    
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()