from django.contrib import admin
from django.urls import path, include

"""
Defines main URL patterns for project.
"""

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('', include('nourish_home.urls'), name="home-urls"),
    path('summernote/', include('django_summernote.urls')),
]
