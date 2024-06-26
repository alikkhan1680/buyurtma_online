from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Pastebin API')




urlpatterns = [
    path('swagger/', schema_view),
    path('admin/', admin.site.urls),
    path('', include("app.urls")),
    path('api-auth/', include('rest_framework.urls')),
    ]








