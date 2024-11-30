from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from online_delivery.models import BaseUser


class BaseUserCreationForm(UserCreationForm):
    class Meta:
        model = BaseUser
        fields = ("username", "password")


class BaseUserChangeForm(UserChangeForm):
    class Meta:
        model = BaseUser
        fields = ("username",)
