from django.urls import path
from .views import *

urlpatterns = [path('index.html', index),
               path('work.html', work),
               path('order.html', order),
               path('about.html', about),
               path('contact.html', contact),
               path('branch.html', branch),
               path('', index)]

