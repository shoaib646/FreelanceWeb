from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path(r'result',views.forminfo, name='result'),
    path(r'CapstoneTermI', views.semesterone, name='semone'),
    path(r'term2', views.semestertwo, name='semtwo')

]
