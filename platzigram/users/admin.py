from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib.auth.models import User
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

    #paginacion de la pagina admin de edicion de profile
    fieldsets = (
        ('Profile',{
            'fields': (
                ('user','picture'),
            )
        }),
        ('Extra info',{
            'fields':(
                ('website','phone_number'),
                ('biography')
            )
        }),
        ('Metadata',{
            'fields':(('created','modified'),)
        }),
    )

    readonly_fields = ('created','modified',)

#Permite crear usuario a la vez que profile

class ProfileInline (admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
