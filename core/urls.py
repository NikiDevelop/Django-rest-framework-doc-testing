
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls


# Conectamos nuestra Api utilizando routers automáticamente 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('docs/', include_docs_urls(title='api Documentation')),
]
