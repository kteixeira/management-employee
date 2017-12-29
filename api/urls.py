from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from api.viewsets import EmployeeViewSet
from src.views import home


schema_view = get_swagger_view(title='Management Employee API')

router = routers.DefaultRouter()

router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^docs/', schema_view),
]
