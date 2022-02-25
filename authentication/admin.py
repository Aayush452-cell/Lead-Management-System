from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib import messages
from django.utils.translation import ngettext
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Leads

# class BaseReadOnlyAdminMixin:
#     def has_add_permission(self, request):
#         return False
#
#     def has_change_permission(self, request, obj=None):
#         return False
#
#     def has_delete_permission(self, request, obj=None):
#         return False


@admin.action(description="Mark Selected as Approved")
def mark_approved(self, request, queryset):
    updated = queryset.update(status="Approved")
    self.message_user(request, ngettext(
        '%d user was successfully marked as Approved.',
        '%d users were successfully marked as Approved.',
        updated,
    ) % updated, messages.SUCCESS)

@admin.action(description="Mark Selected as Not Approved")
def mark_not_approved(self, request, queryset):
    updated = queryset.update(status="Not Approved")
    self.message_user(request, ngettext(
        '%d user was successfully marked as Not Approved.',
        '%d users were successfully marked as Not Approved.',
        updated,
    ) % updated, messages.SUCCESS)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ('email', 'is_staff', 'is_active', 'is_superuser', 'status')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'phone_no', 'manager_id', 'status')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser', 'first_name',
                       'last_name', 'phone_no', 'manager_id', 'status')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    actions = [mark_approved, mark_not_approved]

class LeadsAdmin(admin.ModelAdmin):
    list_display = ('email', 'status', 'sales_representative')
    list_filter = ('status', 'sales_representative', )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Leads, LeadsAdmin)
admin.site.site_header = "Leads Management Platform"
