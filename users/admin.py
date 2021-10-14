from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User
from users.forms import CustomUserCreationForm, CustomUserChangeForm


class UserAdmin(UserAdmin):
    """Customize user/admin on django admin."""
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    search_fields = ('email',)
    list_display = ('email', 'id', 'username', 'is_driver',
                    'is_verified', 'is_active')
    list_filter = ('is_active', 'is_staff', 'is_verified', 'is_driver')
    ordering = ('email', )

    readonly_fields = ('date_joined', 'birth_date')

    fieldsets = (
        (None, {
            'fields': ('email', 'username', 'password')
        }),
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'birth_date', 'date_joined')
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_driver', 'is_verified')
        }),
        ('Status', {
            'fields': ('is_active', )
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff')}
         ),
    )


admin.site.register(User, UserAdmin)
