from django.contrib import admin
from .models import Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):

    list_display = (
        'id', 'manufacturer', 'model', 'android_version',
        'android_id', 'is_active', 'last_seen', 'created_at'
    )

    list_filter = (
        'manufacturer', 'android_version', 'sdk_level',
        'is_emulator', 'is_debuggable', 'is_active'
    )

    search_fields = (
        'android_id', 'model', 'manufacturer', 'device_key'
    )

    readonly_fields = (
        'device_key', 'created_at', 'last_seen'
    )

    fieldsets = (
        ("🆔 Identité", {
            'fields': ('android_id', 'device_key', 'model', 'manufacturer', 'android_version')
        }),
        ("🧱 Matériel", {
            'fields': (
                'brand', 'hardware', 'soc_manufacturer', 'soc_model',
                'supported_abis', 'board', 'product', 'device_code'
            )
        }),
        ("⚙️ Système", {
            'fields': (
                'sdk_level', 'build_id', 'build_fingerprint',
                'build_type', 'build_tags', 'build_time', 'security_patch'
            )
        }),
        ("💾 Mémoire & Stockage", {
            'fields': ('total_ram', 'total_storage', 'available_storage')
        }),
        ("📱 Écran", {
            'fields': (
                'screen_width', 'screen_height',
                'screen_density', 'screen_refresh_rate'
            )
        }),
        ("🔋 Batterie", {
            'fields': ('battery_capacity', 'battery_level', 'is_charging')
        }),
        ("📡 Réseau", {
            'fields': (
                'sim_operator', 'sim_country', 'sim_carrier_name',
                'network_operator', 'network_country', 'network_type',
                'is_roaming', 'phone_count', 'is_dual_sim'
            )
        }),
        ("🌍 Localisation", {
            'fields': ('language', 'country', 'timezone', 'is_24hour_format')
        }),
        ("🔐 Sécurité", {
            'fields': (
                'is_rooted_score', 'is_debuggable', 'is_emulator',
                'has_verified_boot', 'encryption_state'
            )
        }),
        ("🧭 Capteurs & Fonctions", {
            'fields': (
                'has_camera', 'has_nfc', 'has_bluetooth',
                'has_fingerprint', 'has_face_unlock',
                'has_ir_blaster', 'has_compass',
                'has_gyroscope', 'has_accelerometer',
                'camera_count', 'camera_resolutions'
            )
        }),
        ("📦 Application", {
            'fields': (
                'app_version', 'app_build_number',
                'is_first_install', 'install_time', 'update_time'
            )
        }),
        ("🕒 Métadonnées", {
            'fields': ('is_active', 'created_at', 'last_seen')
        }),
    )

    list_per_page = 25
