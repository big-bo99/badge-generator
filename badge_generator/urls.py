from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('badge/', include('badge.urls')),
    path('admin/', admin.site.urls),
]
