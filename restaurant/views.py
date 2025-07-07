from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Dish, Cook, DishType


def index(request: HttpRequest) -> HttpResponse:
    num_dishes = Dish.objects.count()
    num_cooks = Cook.objects.count()
    num_dish_types = DishType.objects.count()
    context = {
        "num_dishes": num_dishes,
        "num_cooks": num_cooks,
        "num_dish_types": num_dish_types,
    }
    return render(request, "restaurant/index.html", context = context)


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "restaurant/dish_type_list.html"
    context_object_name = "dish_type_list"


class DishListView(generic.ListView):
    model = Dish
    queryset = Dish.objects.select_related("dish_type")


def dish_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    dish = Dish.objects.get(pk=pk)
    context = {
        "dish": dish,
    }
    return render(request, "restaurant/dish_detail.html", context=context)


class CookListView(generic.ListView):
    model = Cook
