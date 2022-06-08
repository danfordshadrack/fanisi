from django.contrib import admin
from .models import Licence

class LicenceAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'issuing_institution',
        'date_issued',
        'expiry_date',
        'leseni'

    )

admin.site.register(Licence, LicenceAdmin)