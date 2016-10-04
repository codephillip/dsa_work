from django.conf.urls import url
from django.contrib import admin

from myapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^notes/', views.dsa_notes, name='dsa_notes'),
    url(r'^notes_details/(?P<pk>[-\w]+)/', views.dsa_notes_details, name='dsa_notes_details'),
    url(r'^about/', views.about, name='about'),
]
