"""urbvans URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

# Django
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

# Django REST Framework
from rest_framework.schemas import get_schema_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include('vans.urls')),

    path('openapi/', get_schema_view(
        title="Urbvan vans",
        description="API REST to manage vans",
        version="1.0.0",
    ), name='openapi-schema'),

    path('doc/', TemplateView.as_view(
        template_name='doc.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='doc'),
]
