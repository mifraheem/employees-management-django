
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from employees.views import add_dummy_employees
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-dummy-employees/', add_dummy_employees, name='add-dummy-employees'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
