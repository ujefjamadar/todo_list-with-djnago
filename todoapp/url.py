from django.urls import path
from todoapp import views

urlpatterns=[
    path('',views.display),
    path('add',views.add),
    path('edit/<tid>',views.edit),
     path('delete/<tid>',views.delete)
]