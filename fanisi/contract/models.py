from django.db import models

from party.models import Party


CONTRACT_AREA= [
    ('Operations', 'Operations'),
    ('Business', 'Business'),
    ('IT', 'IT'),
    ('Legal', 'Legal'),
    ('Human resources', 'Human resources'),
    ('Professional Service', 'Professional service'),
]


# Create your models here.
class NonDisclosure(models.Model):

    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=False, null=False)
    date_signed = models.DateTimeField()
    agreement = models.FileField(max_length=255, blank=False, null=False)


    def __str__(self):
        return self.name


    class Meta:

        verbose_name= "Non Disclosure"


    
class Contract(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    contract_area = models.CharField(max_length=50, choices=CONTRACT_AREA, default='Operation')
    contract_description = models.CharField(max_length=100, blank=False, null=False)
    duration = models.IntegerField(blank=False, null=False)
    date_signed = models.DateTimeField(blank=False, null=False)
    start_date = models.DateTimeField(blank=False, null=False)
    end_date = models.DateTimeField(blank=False, null=False)
    agreement = models.FileField(max_length=50, blank=False, null=False)
    price = models.CharField(max_length=50)



    def __str__(self):
        return self.name


    class Meta:


        verbose_name = "Contract"

        verbose_name_plural = "Contract"


class Addendum(models.Model):
    name = models.CharField(max_length=255,null=False, blank=False)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, blank=False, null=False, default="None")
    date_signed = models.DateTimeField(blank=False, null=False)
    effective_date = models.DateTimeField(blank=False, null=False)
    end_date = models.DateTimeField(blank=False, null=False)
    price = models.CharField(max_length=50)
    agreement = models.FileField(max_length=50, blank=False, null=False)


    def __str__(self):

        return self.name

    class Meta:

        verbose_name = "Addendum"
        verbose_name_plural = "Addenda"

class Appointee(models.Model):
    name = models.CharField(max_length=255 , null=False, blank=False)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Appointee"
        verbose_name_plural = "Appointees"



class BoardResolution(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    appointees = models.ManyToManyField(Appointee)
    date = models.DateField(auto_now_add=False, blank=True, null=True)
    resolution = models.FileField(max_length=255, blank=False, null=False)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Board Resolution"



    