from django.urls import path, include
from rest_framework import routers
from api import views


# Los routers determinan de forma automáticamente la configuración de URL
router = routers.DefaultRouter()
router.register(r'User', views.UserViewSet)

urlpatterns=[
    path('', include(router.urls))
]