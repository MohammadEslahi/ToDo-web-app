from django.urls import path
from . import views


urlpatterns = [
    path('', views.homeView , name='home'),
    path('delete/<int:id>', views.deleteView, name='delete'),
    path('update/<int:id>', views.updateView, name='update')
]