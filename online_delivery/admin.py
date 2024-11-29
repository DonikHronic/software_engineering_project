from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from online_delivery.forms import BaseUserCreationForm, BaseUserChangeForm
from online_delivery.models import BaseUser, Product, Restaurant, ProductCategory


class CustomUserAdmin(UserAdmin):
    add_form = BaseUserCreationForm
    form = BaseUserChangeForm
    model = BaseUser
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )
        }
         ),
    )
    search_fields = ("email",)
    ordering = ("email",)


class RestaurantAdmin(admin.ModelAdmin):
    model = Restaurant


class CategoryAdmin(admin.ModelAdmin):
    model = ProductCategory


class ProductAdmin(admin.ModelAdmin):
    model = Product


admin.site.register(BaseUser, CustomUserAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(ProductCategory, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
