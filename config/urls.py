from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from blog.views import ImageRegisterAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/v1/',include('apiv1.urls')),
    path('api/blog/',include('blog.urls')),
    path('api/works/',include('works.urls')),
    path('mdeditor/uploads/', ImageRegisterAPIView.as_view(), name="imageRegister"),
    path('mdeditor/', include('mdeditor.urls'))
]
urlpatterns += static("/media/", document_root=settings.MEDIA_ROOT)