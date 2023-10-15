
from django.contrib import admin
from django.urls import path, include
from .view import Homeview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Homeview.as_view(), name="home"),
    path ("blog/", include('blog.urls', namespace='blog'))
]
