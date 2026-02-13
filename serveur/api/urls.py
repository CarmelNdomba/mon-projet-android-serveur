# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Endpoint pour l'enregistrement des téléphones
    # URL: /api/register/
    path('register/', views.DeviceRegisterView.as_view(), name='device-register'),
    
    # Endpoint pour tester l'authentification
    # URL: /api/test/
    path('test/', views.DeviceTestView.as_view(), name='device-test'),
    
    # (Optionnel) Si tu veux ajouter d'autres endpoints plus tard
    # path('devices/', views.DeviceListView.as_view(), name='device-list'),
    # path('devices/<int:pk>/', views.DeviceDetailView.as_view(), name='device-detail'),
]