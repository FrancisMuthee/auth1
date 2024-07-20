# Import necessary modules
from django.contrib import admin # Django admin module
from django.urls import path
from django.conf.urls.static import static

# from big.big.settings import STATIC_URL	 # URL routing
from . import views
from . views import * # Import views from the authentication app
from django.conf import settings # Application settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # Static files serving

# Define URL patterns
urlpatterns = [
    path('', views.home, name='home'),  # URL for the home page
    path('login/', views.login_page, name='login'),  # URL for the login page
    path('register/', views.register_page, name='register'),  # URL for the registration page
]

# Serve media files if DEBUG is True (development mode)
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files using staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
