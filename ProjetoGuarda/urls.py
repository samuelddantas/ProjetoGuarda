"""ProjetoGuarda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Guarda.views import Create2
from Guarda.views import Create
from Guarda.views import Create3
from Guarda.views import update
from Guarda.views import update2
from Guarda.views import update3
from Guarda.views import Read
from Guarda.views import delete
from Guarda.views import delete2
from Guarda.views import delete3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Read, name = 'url_Read'),
    path('forms/', Create, name ='url_forms'),
    path('forms2/', Create2, name ='url_forms2'),
    path('forms3/', Create3, name ='url_forms3'),
    path('update/<int:pk>/', update, name = 'url_update'),
    path('update2/<int:pk>/', update2, name = 'url_update2'),
    path('update3/<int:pk>/', update3, name = 'url_update3'),
    path('delete/<int:pk>/', delete, name = 'url_delete'),
    path('delete2/<int:pk>/', delete2, name = 'url_delete2'),
    path('delete3/<int:pk>/', delete3, name = 'url_delete3')
]
