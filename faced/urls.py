
from django.contrib import admin
from django.urls import path
from base import views
urlpatterns = [
    path('',views.home),
    path('admin/', admin.site.urls),
    path('get-face', views.get_face)
]
