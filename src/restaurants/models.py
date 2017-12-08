from django.db import models

# Create your models here.
class RestaurantLocation(models.Model):
    name            = models.CharField(max_length=120)
    location        = models.CharField(max_length=120, null=True, blank=True)
    category        = models.CharField(max_length=120, null=True, blank=True)
    
    # Note: auto_now_add would override auto_now
    # Both fields are now non editable, they do not appear in the admin
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    # Custom editable fields
    my_date_field   = models.DateField(auto_now=False, auto_now_add=False)

