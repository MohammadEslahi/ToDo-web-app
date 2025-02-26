from django.urls import path
from . import views
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.TasksView , name='home'),
    path('delete/<int:id>', views.deleteView, name='delete'),
    path('update/<int:id>', views.updateView, name='update'),
    path('checker/<int:id>', views.checkerView, name='checker'),
    path('unchecker/<int:id>', views.uncheckerView, name='unchecker'),
    path('categories/<int:id>', views.manageCategories, name='categories'),
    # DRF and JWT urls...
    path('tasks/', api_task_list_view, name='api_task_list'),
    path('register/', API_user_register_view, name='API_user_register'),
    path('token/', TokenObtainPairView.as_view(), name='TokenObtainPair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='TokenRefresh'),
    path('login/', API_user_login, name='api_login'),
    path('tasks/<int:pk>/', api_task_detail_view, name='api_task_detail'),
    path('tasks/<int:pk>/delete/', api_task_delete_view, name='api_task_delete'),
]