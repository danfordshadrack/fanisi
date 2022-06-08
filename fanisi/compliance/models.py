from django.db import models

# Create your models here.
class Licence(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    issuing_institution = models.CharField(max_length=255, blank=False)
    date_issued = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True)
    expiry_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True)
    leseni = models.FileField(blank=False, upload_to='licenses', editable=True)


    def __str__(self):
        return self.title

    class Meta:


        managed = True
        verbose_name_plural = "Licences"