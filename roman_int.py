# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    roman_int.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mgrayson <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/16 16:55:20 by mgrayson          #+#    #+#              #
#    Updated: 2020/11/16 17:16:59 by mgrayson         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Install Django
pip install django

# Create a new Django project
django-admin startproject contactslist

# Navigate into the new project directory
cd contactslist

# Start the development server
python manage.py runserver

# Open your browser and navigate to http://127.0.0.1:8000/ to verify that the project is running correctly

# Deploy the project to a hosting service like Heroku or PythonAnywhere

# Create a new app
python manage.py startapp contacts

# Open the contacts/views.py file and create a new view function that returns a basic HTTP response
from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello, world!')

# Map the view to a URL by creating a new contacts/urls.py file
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]

# Include the new URL configuration in the project's urls.py file
from django.urls import include, path

urlpatterns = [
    path('contacts/', include('contacts.urls')),
]

# Create a new view that renders a template with a list of contacts
from django.shortcuts import render
from .models import Contact

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})


# Define a new model in contacts/models.py
from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)

# Register the Contact model in contacts/admin.py
from django.contrib import admin
from .models import Contact

admin.site.register(Contact)

# Access the Contact model via admin by logging in to the admin site and navigating to the Contacts section
