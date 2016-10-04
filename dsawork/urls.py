from django.conf.urls import url
from django.contrib import admin

from myapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^notes/', views.dsa_notes, name='dsa_notes'),
    url(r'^about/', views.about, name='about'),
]
