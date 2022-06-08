from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False)
    phone = models.CharField(max_length=255, blank=False, null=False)


    def __str__(self):
        
        return self.name


    class Meta:

        verbose_name = ("Client")
        verbose_name_plural = "Clients"


class Party(models.Model):
    name = models.CharField(max_length=255, blank=False)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    registered_address = models.CharField(max_length=255, blank=False, null=False)
    office_phone = models.CharField(max_length=255, blank=False, null=False)
    po_box = models.CharField(max_length=255, blank=False, null=False)
    office_email = models.EmailField(max_length=255, blank=False)



    def __str__(self):
        return self.name


    class Meta:

        verbose_name = "Party"

        verbose_name_plural = 'Parties'





