from authapp.forms import ShopUserEditForm
from authapp.models import ShopUser
from django import forms


class ShopUserAdminEditForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = '__all__'
