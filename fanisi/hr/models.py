from django.db import models

DEPARTMENTS= [
    ('Operations', 'Operations'),
    ('Business', 'Business'),
    ('IT', 'IT'),
    ('Legal', 'Legal'),
    ('Human resources', 'Human resources'),
]


class HumanResources(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    department = models.CharField(max_length=50, choices=DEPARTMENTS, default='Operations')
    title = models.CharField(max_length=100, blank=False)
    start_date = models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    salary = models.IntegerField(blank=False)
    contract_duration = models.CharField(max_length=10, blank=False)
    contract_document = models.FileField(blank=False, upload_to='contracts')

    def __str__(self):
        
        return self.name
        

    class Meta:
        
        managed = True
        verbose_name = 'Human Resource'