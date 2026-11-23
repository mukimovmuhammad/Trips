from django.contrib import admin
from django.urls import path,include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('docs/',SpectacularAPIView.as_view(),name='docs'),
    path('schema/',SpectacularSwaggerView.as_view(url_name='docs'))
]
