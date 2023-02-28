from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('lotto/', include('lotto.urls')),
    path('admin/', admin.site.urls),
]
