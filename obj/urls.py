from django.contrib import admin
from django.urls import path, include  # include for referencing core app urls

urlpatterns = [
    path('', include('core.urls')),

    path('admin/', admin.site.urls),
]