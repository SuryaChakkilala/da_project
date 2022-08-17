from django.contrib import admin
from django.urls import path
from .views import index, loginPage, logoutUser, registerPage, facilities, facility, delete_facility, faq_form, rest_demo

urlpatterns = [
    path('', index, name='home'),
    path('login', loginPage, name='login'),
    path('register', registerPage, name='register'),
    path('facilities', facilities, name='facilities'),
    path('facility/<id>', facility, name='facility'),
    path('deletefacility/<id>', delete_facility, name='deletefacility'),
    path('logout', logoutUser, name='logout'),
    path('faqform', faq_form, name='faq-form'),
]

