from django.urls import path
from .views import *

urlpatterns = [
    path("", home),
    path("calculator/", calculator),
    path('timer/', timer),
    path('convert/', convertor),
    path('game/', game),
    path('random/', randomiser),
    path('notes/', notepad),
    path('code/', shtrih),
    path('metres/', metres),
    path('pay/', payment),
    path('table/', table)
]
