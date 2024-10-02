from django.contrib import admin
from .models import Profile, Project, CertifyingInstitution, Certificate


# Register your models here.
class CertificateInline(admin.StackedInline):
    model = Certificate


class CertifyingInstitutionAdmin(admin.ModelAdmin):
    inlines = [CertificateInline]


admin.site.site_header = "Super Portfolio Admin"
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(CertifyingInstitution, CertifyingInstitutionAdmin)
