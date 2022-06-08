from django.contrib import admin

# Register your models here.
from party.models import Client, Party
from .models import NonDisclosure, Contract, Addendum


class NonDisclosureAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'party',
        'date_signed',
        'agreement',

    )

admin.site.register(NonDisclosure, NonDisclosureAdmin)




class ContractAdmin(admin.ModelAdmin):


    list_display = (
        'name',
        'party',
        'contract_area',
        'duration',
        'date_signed',
        'start_date',
        'end_date',
        'agreement',
        'price',
    )

admin.site.register(Contract, ContractAdmin)


class AddendumAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'contract',
        'date_signed',
        'effective_date',
        'end_date',
        'price',
        'agreement',
    )

admin.site.register(Addendum, AddendumAdmin)