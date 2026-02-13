# api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import Device
from .serializers import DeviceRegistrationSerializer, DeviceDetailSerializer

class DeviceRegisterView(APIView):
    """
    Endpoint pour l'enregistrement des téléphones
    """
    permission_classes = [AllowAny]
    
    def post(self, request):
        # 1. Le serializer valide automatiquement les données
        serializer = DeviceRegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            # 2. Données validées - prêtes à être utilisées
            validated_data = serializer.validated_data
            android_id = validated_data.pop('android_id')
            
            # 3. Créer ou mettre à jour
            device, created = Device.objects.update_or_create(
                android_id=android_id,
                defaults=validated_data
            )
            
            # 4. Réponse avec les infos essentielles
            return Response({
                'success': True,
                'deviceKey': device.device_key,
                'deviceId': device.id,
                'isNewDevice': created,
                'message': '✅ Enregistrement réussi'
            }, status=status.HTTP_200_OK)
        
        # 5. Erreurs de validation
        return Response({
            'success': False,
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        return Response({
            'success': True,
            'message': '📱 API prête',
            'required_fields': ['androidId', 'model', 'manufacturer'],
            'optional_fields': list(DeviceRegistrationSerializer.Meta.fields)[1:]
        })


class DeviceTestView(APIView):
    """
    Endpoint pour tester l'authentification
    """
    permission_classes = [AllowAny]
    
    def post(self, request):
        auth_key = request.headers.get('X-Device-Key')
        
        if not auth_key:
            return Response({
                'success': False,
                'error': '🔑 Clé manquante'
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            device = Device.objects.get(device_key=auth_key, is_active=True)
            device.save()
            
            serializer = DeviceDetailSerializer(device)
            
            return Response({
                'success': True,
                'message': '✅ Authentification réussie',
                'device': serializer.data
            })
            
        except Device.DoesNotExist:
            return Response({
                'success': False,
                'error': '❌ Clé invalide'
            }, status=status.HTTP_401_UNAUTHORIZED)