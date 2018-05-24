from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from solvecore.libs.accounts.forms import UserCreationForm, AdminUserChangeForm

from django.contrib.auth import get_user_model
User = get_user_model()


USERNAME_FIELD = User.USERNAME_FIELD

REQUIRED_FIELDS = (USERNAME_FIELD,) + tuple(User.REQUIRED_FIELDS)

BASE_FIELDS = (None, {
    'fields': REQUIRED_FIELDS + ('password',),
})

PROFILE_FIELDS = (_('Profile'), {
    'fields': ('name', 'profile_picture',),
})

PERMISSION_FIELDS = (_('Permissions'), {
    'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',),
})

DATE_FIELDS = (_('Important dates'), {
    'fields': ('last_login', 'date_joined',),
})


class UserAdmin(DjangoUserAdmin):
    # The forms to add and change user instances
    add_form_template = None
    add_form = UserCreationForm
    form = AdminUserChangeForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('is_active', USERNAME_FIELD, 'email', 'name', 'is_superuser', 'is_staff',)
    list_display_links = (USERNAME_FIELD, 'name',)
    search_fields = ('email', 'name',)
    fieldsets = (
        BASE_FIELDS,
        PROFILE_FIELDS,
        PERMISSION_FIELDS,
        DATE_FIELDS,
    )
    list_filter = ('is_superuser', 'is_staff', 'is_active',)
    add_fieldsets = (
        (None, {
            'fields': REQUIRED_FIELDS + (
                'password1',
                'password2',
            ),
        }),
    )
    ordering = None
    filter_horizontal = ('groups', 'user_permissions',)
    readonly_fields = ('last_login', 'date_joined')


admin.site.register(User, UserAdmin)
