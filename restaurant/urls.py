from django.urls import path
from restaurant.views import index, DishTypeListView, DishListView, CookListView, dish_detail_view


urlpatterns = [
    path("", index, name="index"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", dish_detail_view, name="dish-detail"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
]

app_name = "restaurant"
