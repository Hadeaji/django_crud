from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('<int:pk>/',CrudDetailsView.as_view(), name = 'crud_detail'),
    path('new/', CrudCreateView.as_view(), name='crud_create'),
    path('<int:pk>/edit/', CrudUpdateView.as_view(), name='crud_update'),
    path('<int:pk>/delete/', CrudDeleteView.as_view(), name='crud_delete'),
]