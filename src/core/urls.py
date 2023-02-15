from django.contrib import admin
from django.urls import (
    path,
    include
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('music.urls'))
]

urlpatterns += [
    path(
        'api-swagger/schema/',
        SpectacularAPIView.as_view(),
        name='schema'
    ),

    path(
        '',
        SpectacularSwaggerView.as_view(),
        name="swagger-ui"
    ),
]
