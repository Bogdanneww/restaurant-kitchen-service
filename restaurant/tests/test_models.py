from django.contrib.auth import get_user_model
from django.test import TestCase
from restaurant.models import DishType, Dish


class ModelTest(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="test")
        self.assertEqual(str(dish_type), dish_type.name)

    def test_cook_str(self):
        cook = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        cook.first_name = "test_first"
        cook.last_name = "test_last"
        cook.save()

        self.assertEqual(
            str(cook), f"{cook.username} ({cook.first_name} {cook.last_name})"
        )

    def test_dish_str(self):
        dish_type = DishType.objects.create(name="test")
        dish = Dish.objects.create(name="test", price=10.50, dish_type=dish_type)
        self.assertEqual(str(dish), dish.name)

    def test_create_cook_with_experience(self):
        username = "test"
        cook = get_user_model().objects.create_user(
            username=username,
            password="test123",
        )
        cook.first_name = "test_first"
        cook.last_name = "test_last"
        cook.years_of_experience = 5
        cook.save()

        self.assertEqual(cook.username, username)
        self.assertEqual(cook.first_name, "test_first")
        self.assertEqual(cook.last_name, "test_last")
        self.assertEqual(cook.years_of_experience, 5)
