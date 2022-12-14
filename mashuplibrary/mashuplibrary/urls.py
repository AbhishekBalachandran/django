from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='catalog/')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('catalogapi/', include('catalogapi.urls')),
    path('fileupload/', include('profilemaker.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)