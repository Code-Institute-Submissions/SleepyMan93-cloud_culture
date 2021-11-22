from django.db import models

class OrderInquiry(models.Model):
    """ 
    A view to allow users to contact the store:
    order enquiries
    """
    order_number = models.CharField(max_length=64, null=False, blank=False)
    name = models.CharField(max_length=64, null=False, blank=False)
    contact_email = models.EmailField(null=False, blank=False)
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name
