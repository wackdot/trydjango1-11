from django import forms
from .models import Item

from restaurants.models import RestaurantLocation

# Forms used to perform more manipulation before transferring to the view
class ItemForm(forms.ModelForm):
    # Describes the properties of the model
    class Meta:
        model = Item
        fields = [
            'restaurant',
            'name',
            'contents',
            'excludes',
            'public'
        ]
    
    # Manipulates Model Form before use by the view
    # __init__ indicate it runs at instantiation
    def __init__(self, user=None, *args, **kwargs):
        #Note: Both user and kwargs are printed for the Create + Update View 
        print(user)
        print(kwargs)
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['restaurant'].queryset = RestaurantLocation.objects.filter(owner=user).exclude(item__isnull=False)




