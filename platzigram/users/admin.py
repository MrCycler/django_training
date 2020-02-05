from django.contrib import admin
from users.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin (admin.ModelAdmin):
    # Muestra que se debe mostrar en el admin para los perfiles
    list_display = ('pk','user', 'phone_number','website','picture')
    list_display_links = ('pk','user')
    list_editable = ('phone_number','website','picture')
    # Como se puede buscar
    search_fields = ('user__email',
    'user__username',
    'user__first_name',
    'user__last_name',
    'phone_number')
    # filtros que aparecen al costado
    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff',
    )
