from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render
from django.views import generic
from rest_framework.reverse import reverse_lazy

from .models import Dish, Cook, DishType


def index(request: HttpRequest) -> HttpResponse:
    num_dishes = Dish.objects.count()
    num_cooks = Cook.objects.count()
    num_dish_types = DishType.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "num_dishes": num_dishes,
        "num_cooks": num_cooks,
        "num_dish_types": num_dish_types,
        "num_visits": num_visits + 1,
    }
    return render(request, "restaurant/index.html", context = context)


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "restaurant/dish_type_list.html"
    context_object_name = "dish_type_list"


class DishListView(generic.ListView):
    model = Dish
    queryset = Dish.objects.select_related("dish_type")
    paginate_by = 5


class DishDetailView(generic.DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("restaurant:dish-list")
    template_name = "restaurant/dish_form.html"


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("restaurant:dish-list")
    template_name = "restaurant/dish_form.html"


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    template_name = "restaurant/dish_confirm_delete.html"
    success_url = reverse_lazy("restaurant:dish-list")


class CookListView(generic.ListView):
    model = Cook
    paginate_by = 3


class CookDetailView(generic.DetailView):
    model = Cook
