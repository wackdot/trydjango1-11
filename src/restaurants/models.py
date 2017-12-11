from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save

from .utils import unique_slug_generator
from .validators import validate_category

User = settings.AUTH_USER_MODEL

# Create your models here.
class RestaurantLocation(models.Model):
    owner           = models.ForeignKey(User) #Django Models Unleshed JOINCFE.com
    name            = models.CharField(max_length=120)
    location        = models.CharField(max_length=120, null=True, blank=True)
    category        = models.CharField(max_length=120, null=True, blank=True, validators=[validate_category])
    
    # Note: auto_now_add would override auto_now
    # Both fields are now non editable, they do not appear in the admin
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    slug            = models.SlugField(null=True, blank=True)

    # Custom slug field
    def __str__(self):
        return self.name

    # Custom editable fields
    # my_date_field   = models.DateField(auto_now=False, auto_now_add=False)

    @property
    def title(self):
        return self.name # Used in conjunction with random generator

# Just prior saving a new / updating a record
def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    print('saving..')
    print(instance.timestamp)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)



# # Just after saving a new / updating a record
# def rl_post_save_receiver(sender, instance, created, *args, **kwargs):
#     print('saved..')
#     print(instance.timestamp)

pre_save.connect(rl_pre_save_receiver, sender=RestaurantLocation)

# post_save.connect(rl_post_save_receiver, sender=RestaurantLocation)

