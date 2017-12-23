from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from src.views import home
from rest_framework import routers
from api.viewsets import EmployeeViewSet
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Management Employee API')

router = routers.DefaultRouter()

router.register(r'employee', EmployeeViewSet)

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^api/', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^docs/', schema_view),
]
