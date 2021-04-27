from django.urls import path,include

from .views import catalog

app_name='catalog'
urlpatterns = [
    path('', catalog,name='catalog'),
]
