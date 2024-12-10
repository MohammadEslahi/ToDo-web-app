from django.urls import path
from . import views


urlpatterns = [
    path('', views.TasksView , name='home'),
    path('delete/<int:id>', views.deleteView, name='delete'),
    path('update/<int:id>', views.updateView, name='update'),
    path('checker/<int:id>', views.checkerView, name='checker'),
    path('unchecker/<int:id>', views.uncheckerView, name='unchecker'),
]