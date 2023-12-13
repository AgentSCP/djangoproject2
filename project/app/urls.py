from django.urls import path
from .views import index, myForm

url_patterns = [
    path('', index, name='name'),
    path('myform', myForm, name='form'),
    # path('user', user, name='user'),
]