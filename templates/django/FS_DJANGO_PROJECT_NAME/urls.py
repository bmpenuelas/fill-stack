"""{{ FS_DJANGO_PROJECT_NAME }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
{% if render_features['django-jwt'] %}
from rest_framework_jwt.views import obtain_jwt_token
{% endif %}


urlpatterns = [
    path('{{ FS_API_PATH }}/admin/', admin.site.urls),

    {% if render_features['django-jwt'] %}
    path('{{ FS_API_PATH }}/auth-jwt/', obtain_jwt_token),
    {% endif %}

    {% if render_features['django-socialauth'] %}
    path('{{ FS_API_PATH }}/auth-social/', include('rest_framework_social_oauth2.urls', namespace='django-socialauth')),
    {% endif %}

    path('{{ FS_API_PATH }}/', include('{{ FS_DJANGO_APP_NAME }}.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
