from django.urls import URLPattern, path
from .import views

urlpatterns=[
    path('',views.side,name='side'),
    path('table',views.table,name='table'),
]