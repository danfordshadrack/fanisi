from django.contrib import admin

# Register your models here.
from .models import Client, Party


class ClientAdmin(admin.ModelAdmin):

    list_display = ('name','email', 'phone')



admin.site.register(Client, ClientAdmin)

class PartyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'registered_address',
        'office_phone',
        'po_box',
        'office_email'

    )

admin.site.register(Party, PartyAdmin)