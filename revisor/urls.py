from django.contrib import admin
from django.urls import path
from polls import views

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('', views.registro, name='registro'),
]