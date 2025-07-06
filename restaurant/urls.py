from django.urls import path
from restaurant.views import index, dish_types_list_view


urlpatterns = [
    path("", index, name="index"),
    path("dish-types/", dish_types_list_view, name="dish-types-list"),
]

app_name = "restaurant"
