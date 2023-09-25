from django.urls import URLPattern, path
from .import views
urlpatterns=[
    path('',views.chart,name='chart'),
    path('data_exp/',views.data_exp,name='data_exp'),
    path('data_add',views.data_add,name="data_add"),
    path('trans',views.trans,name="trans")
]