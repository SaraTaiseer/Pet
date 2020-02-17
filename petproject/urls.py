"""petproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from petApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.available_list ,name='Availables'),
    path('pets/detail/<int:pet_id>/',views.pets_detail ,name='pet-detail'),
    path('pet/create/',views.pet_create ,name='pet-create'),
    path('pet/update/<int:pet_id>/',views.pet_update ,name='pet-update'),
    path('pet/delete/<int:pet_id>/',views.pet_delete ,name='pet-delete'),

    #path('pets/detail/<int:pet_id>/',views.pets_detail ,name='pet-detail'),




]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
