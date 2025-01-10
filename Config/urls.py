from django.contrib import admin
from django.urls import path, include
# for recognizing & loading static files...
from django.conf.urls.static import static
from django.conf import settings
from main.views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('main.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/<int:id>', include('accounts.urls')),
    # REST API-related view
    path('api/tasks/',api_task_list_view ,name='api_task_list'),
    path('api/tasks/<int:pk>/',api_task_detail_view ,name='api_task_detail'),
    path('api/tasks/<int:pk>/delete/', api_task_delete_view, name='api_task_delete'),
    # Generating REST API auth token
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

# for recognizing & loading static files...
urlpatterns += static (settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)