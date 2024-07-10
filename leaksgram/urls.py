from django.contrib import admin
from django.urls import path
from base.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('video', video),
    path('firebase-messaging-sw.js', firebase_messaging_sw)
]
