from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from restaurant.models import DishType, Dish, Cook


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "dish_type"]
    list_filter = ["dish_type"]
    search_fields = ["name"]


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        ("years of experience", {"fields": ("years_of_experience",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "additional info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "years_of_experience",
                )
            },
        ),
    )


admin.site.register(DishType)
