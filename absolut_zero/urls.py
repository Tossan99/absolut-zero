"""
URL configuration for absolut_zero project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("home.urls")),
    path("about/", include("about.urls")),
    path("checkout/", include("checkout.urls")),
    path("faq/", include("faq.urls")),
    path("products/", include("products.urls")),
    path("profile/", include("profiles.urls")),
    path("shopping_cart/", include("shopping_cart.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

HANDLER403 = "home.views.view_custom403"
HANDLER404 = "home.views.view_custom404"
HANDLER405 = "home.views.view_custom405"
HANDLER500 = "home.views.view_custom500"
