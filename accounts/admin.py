from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Custom admin interface for user model"""

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    list_display = (
        'username', 'email', 'first_name', 'last_name',
        'is_active', 'is_staff', 'email_verified', 'created_at'
    )

    list_filter = ('is_active', 'is_staff', 'is_superuser', 'email_verified')

    search_fields = ('username', 'email', 'first_name', 'last_name')

    ordering = ('-date_joined',)

    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': (
                'bio', 'avatar', 'website', 'telegram',
                'github', 'birth_date', 'location'
            )
        }),
        ('Verification', {
            'fields': ('email_verified', 'email_verification_token')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'password1', 'password2',
                'first_name', 'last_name', 'bio'
            )
        }),
    )
