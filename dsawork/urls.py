from django.conf.urls import url
from django.contrib import admin

from myapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^sorting/', views.sorting, name='sorting'),
    url(r'^sorted_receipt/(?P<pk>[-\w]+)/', views.sorted_receipt, name='sorted_receipt'),
    url(r'^searching/(?P<item>[-\w]+)/', views.searching, name='searching'),
]
