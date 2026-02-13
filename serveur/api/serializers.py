# api/serializers.py
from rest_framework import serializers
from .models import Device

class DeviceRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer pour l'enregistrement des appareils
    Tous les champs sont optionnels sauf androidId
    """
    
    # On expose android_id comme androidId pour l'API
    androidId = serializers.CharField(source='android_id', required=True)
    
    class Meta:
        model = Device
        fields = [
            # Identifiants
            'androidId',
            
            # INFOS DE BASE
            'model',
            'manufacturer',
            'android_version',
            'brand',
            
            # INFOS MATÉRIELLES
            'hardware',
            'soc_manufacturer',
            'soc_model',
            'supported_abis',
            'board',
            'product',
            'device_code',
            
            # INFOS SYSTÈME
            'sdk_level',
            'build_id',
            'build_fingerprint',
            'build_type',
            'build_tags',
            'build_time',
            'security_patch',
            
            # MÉMOIRE ET STOCKAGE
            'total_ram',
            'total_storage',
            'available_storage',
            
            # ÉCRAN
            'screen_width',
            'screen_height',
            'screen_density',
            'screen_refresh_rate',
            
            # BATTERIE
            'battery_capacity',
            'battery_level',
            'is_charging',
            
            # RÉSEAU ET TÉLÉPHONIE
            'sim_operator',
            'sim_country',
            'sim_carrier_name',
            'network_operator',
            'network_country',
            'network_type',
            'is_roaming',
            'phone_count',
            'is_dual_sim',
            
            # LOCALISATION
            'language',
            'country',
            'timezone',
            'is_24hour_format',
            
            # SÉCURITÉ
            'is_rooted_score',
            'is_debuggable',
            'is_emulator',
            'has_verified_boot',
            'encryption_state',
            
            # CAPTEURS ET FONCTIONNALITÉS
            'has_camera',
            'has_nfc',
            'has_bluetooth',
            'has_fingerprint',
            'has_face_unlock',
            'has_ir_blaster',
            'has_compass',
            'has_gyroscope',
            'has_accelerometer',
            'camera_count',
            'camera_resolutions',
            
            # INFOS APPLICATION
            'app_version',
            'app_build_number',
            'is_first_install',
            'install_time',
            'update_time',
        ]
        extra_kwargs = {
            field: {'required': False, 'allow_null': True}
            for field in fields if field != 'androidId'
        }


class DeviceDetailSerializer(serializers.ModelSerializer):
    """
    Serializer pour afficher les détails d'un appareil (sans la clé)
    """
    class Meta:
        model = Device
        fields = [
            'id',
            'android_id',
            'model',
            'manufacturer',
            'brand',
            'android_version',
            'sdk_level',
            'is_active',
            'created_at',
            'last_seen',
            'total_ram',
            'total_storage',
            'battery_capacity',
            'has_nfc',
            'has_camera',
            'camera_count',
            'has_fingerprint',
            'language',
            'timezone',
            'is_rooted_score',
            'is_emulator',
        ]
        read_only_fields = fields