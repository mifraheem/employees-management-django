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
    # Method to display the employee's photo
    def photo_tag(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" style="border-radius: 50%; aspect-ratio:1/1" />'.format(obj.photo.url))
        return "No Image"

    # Short description to be shown as column header
    photo_tag.short_description = 'Photo'

    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'father_name', 'cnic', 'date_of_birth', 'gender', 'marital_status', 'blood_group', 'mobile_no', 'email', 'photo')
        }),
        ('Additional Information', {
            'fields': ('seniority_no', 'personnel_no', 'remarks'),
        }),
    )

    inlines = [AddressInline, EmploymentInline,
               QualificationInline, HealthDetailsInline, WorkDetailsInline]

    # Add 'photo_tag' to the list_display to show the photo in the list
    list_display = ('photo_tag', 'name', 'cnic', 'email',
                    'mobile_no', 'gender', 'marital_status')

    search_fields = ('name', 'cnic', 'email')

    list_filter = ('gender', 'marital_status')

    ordering = ['name']


admin.site.register(Employee, EmployeeAdmin)
