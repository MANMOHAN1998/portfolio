from django.urls import path
from .views import *
urlpatterns = [
    path('',first_function),
    path('intro/',intro),
    path('blog/',blogs),
    path('services/',services),
    path('contact/',contact),
]