from django.contrib import admin
from django.urls import path
from base.views import *
from django.views.generic.base import RedirectView, TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('video', video),
    path('firebase-messaging-sw.js', TemplateView.as_view(template_name="firebase-messaging-sw.js", content_type='application/javascript')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
