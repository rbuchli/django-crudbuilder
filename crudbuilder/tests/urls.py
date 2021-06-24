from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path('auth/',  include('django.contrib.auth.urls')),
    path('crud/',  include('crudbuilder.urls'))
    ]
