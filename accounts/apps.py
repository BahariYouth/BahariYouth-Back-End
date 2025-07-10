from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        from django.contrib import admin
        from rest_framework.authtoken.models import Token

        try:
            admin.site.unregister(Token)
        except admin.sites.NotRegistered:
            pass

        # ⬅️ هنا نستورد التسجيل اليدوي
        import accounts.admin_token
