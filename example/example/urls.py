from django.conf.urls import include, url
# from django.contrib import admin
from django.contrib import admin
from django.db import connection
from django.urls import path

from crudbuilder import urls
from . import views

tables = connection.introspection.table_names()

urlpatterns = [
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('crud/', include(urls)),
    path('', views.login_redirect, name='home'),
]

if 'django_content_type' in tables:
    from .views import (
        MyCustomPersonListView,
        MyCustomPersonCreateView
    )

    urlpatterns += [
        url(r'^mycustom_people/$',
            MyCustomPersonListView.as_view(),
            name='mycustom-people'),

        url(r'^mycustom_people/create/$',
            MyCustomPersonCreateView.as_view(),
            name='mycustom-create'),
    ]
