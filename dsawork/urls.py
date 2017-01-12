from django.conf.urls import url
from django.contrib import admin

from myapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^sorting/', views.sorting, name='sorting'),
    url(r'^single_sort/(?P<pk>[-\w]+)/', views.single_sort, name='single_sort'),
]
