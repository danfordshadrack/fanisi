from django.contrib import admin
from .models import HumanResources


# Register your models here.


class HumanResourcesAdmin(admin.ModelAdmin):

    list_display = ('name', 'department', 'title', 'start_date', 'end_date', 'salary', 'contract_duration', 'contract_document')

    list_filter = ('department', 'contract_duration')


admin.site.register(HumanResources, HumanResourcesAdmin)


# class PartyAdmin(admin.ModelAdmin):

#     list_display = (
#         'legal_name',
#         'phone',
#         'email',
#         'registration_number',
#         'registered_address',
#         'contact_person',
#         'signatory',
#     )


# admin.site.register(Party, PartyAdmin)

# class LicenceAdmin(admin.ModelAdmin):
#     pass


# admin.site.register(Licence, LicenceAdmin)

# class OperationAdmin(admin.ModelAdmin):
#     pass



# admin.site.register(Operation,OperationAdmin)