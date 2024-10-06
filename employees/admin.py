from django.utils.html import format_html
from django.contrib import admin
from .models import Employee, Address, Employment, Qualification, HealthDetails, WorkDetails

# Import the User and Group models
from django.contrib.auth.models import User, Group

admin.site.unregister(Group)
admin.site.site_header = "DHQ Kotli"
admin.site.site_title = "DHQ Kotli"
admin.site.index_title = f"Welcome to {admin.site.site_title}"


class AddressInline(admin.TabularInline):
    model = Address
    extra = 1


class EmploymentInline(admin.TabularInline):
    model = Employment
    extra = 1


class QualificationInline(admin.TabularInline):
    model = Qualification
    extra = 1


class HealthDetailsInline(admin.TabularInline):
    model = HealthDetails
    extra = 1


class WorkDetailsInline(admin.TabularInline):
    model = WorkDetails
    extra = 1


class EmployeeAdmin(admin.ModelAdmin):
    def photo_tag(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" style="border-radius: 50%; aspect-ratio:1/1" />'.format(obj.photo.url))
        return "No Image"

    photo_tag.short_description = 'Photo'

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, request, **kwargs)
        if db_field.name == 'photo' and request.resolver_match.kwargs.get('object_id', None):
            obj = self.get_object(
                request, request.resolver_match.kwargs['object_id'])
            if obj and obj.photo:
                formfield.help_text = format_html(
                    '<img src="{}" width="150" height="150" style="border-radius: 50%;" />',
                    obj.photo.url
                )
        return formfield

    fieldsets = (
        ('Personal Information', {
            'fields': ('photo', 'name', 'father_name', 'cnic', 'date_of_birth', 'gender', 'marital_status', 'blood_group', 'mobile_no', 'email')
        }),
        ('Additional Information', {
            'fields': ('seniority_no', 'personnel_no', 'remarks'),
        }),
    )

    inlines = [AddressInline, EmploymentInline,
               QualificationInline, HealthDetailsInline, WorkDetailsInline]

    list_display = ('photo_tag', 'name', 'cnic', 'email',
                    'mobile_no', 'gender', 'marital_status')

    search_fields = ('name', 'cnic', 'email')

    list_filter = ('gender', 'marital_status')

    ordering = ['name']


admin.site.register(Employee, EmployeeAdmin)
