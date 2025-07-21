from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from restaurant.models import DishType, Dish


class PublicAccessTests(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Soup")
        self.dish = Dish.objects.create(
            name="Borshch",
            description="Traditional beet soup",
            price=12.5,
            dish_type=self.dish_type
        )
        self.cook = get_user_model().objects.create_user(
            username="cook",
            password="cookpass"
        )
        self.dish.cooks.add(self.cook)

    def test_index_accessible(self):
        response = self.client.get(reverse("restaurant:index"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("num_dishes", response.context)

    def test_dish_type_list_view_accessible(self):
        response = self.client.get(reverse("restaurant:dish-type-list"))
        self.assertEqual(response.status_code, 200)

    def test_dish_list_view_accessible(self):
        response = self.client.get(reverse("restaurant:dish-list"))
        self.assertEqual(response.status_code, 200)

    def test_cook_list_view_accessible(self):
        response = self.client.get(reverse("restaurant:cook-list"))
        self.assertEqual(response.status_code, 200)

    def test_dish_detail_view(self):
        response = self.client.get(reverse("restaurant:dish-detail", args=[self.dish.id]))
        self.assertEqual(response.status_code, 200)

    def test_cook_detail_view(self):
        response = self.client.get(reverse("restaurant:cook-detail", args=[self.cook.id]))
        self.assertEqual(response.status_code, 200)

    def test_protected_views_redirect_for_anonymous_user(self):
        protected_urls = [
            reverse("restaurant:dish-create"),
            reverse("restaurant:dish-update", args=[self.dish.id]),
            reverse("restaurant:dish-delete", args=[self.dish.id]),
            reverse("restaurant:dish-type-create"),
            reverse("restaurant:dish-type-update", args=[self.dish_type.id]),
            reverse("restaurant:dish-type-delete", args=[self.dish_type.id]),
            reverse("restaurant:cook-create"),
        ]
        for url in protected_urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302)
            self.assertTrue(response.url.startswith("/accounts/login/"))


class PrivateAccessTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpass123"
        )
        self.client.login(username="testuser", password="testpass123")
        self.dish_type = DishType.objects.create(name="Pizza")
        self.dish = Dish.objects.create(
            name="Margarita",
            description="Cheese and tomato",
            price=9.99,
            dish_type=self.dish_type
        )

    def test_create_dish_type(self):
        response = self.client.post(reverse("restaurant:dish-type-create"), {"name": "NewType"})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(DishType.objects.filter(name="NewType").exists())

    def test_update_dish_type(self):
        url = reverse("restaurant:dish-type-update", args=[self.dish_type.id])
        response = self.client.post(url, {"name": "UpdatedType"})
        self.dish_type.refresh_from_db()
        self.assertEqual(self.dish_type.name, "UpdatedType")

    def test_delete_dish_type(self):
        url = reverse("restaurant:dish-type-delete", args=[self.dish_type.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(DishType.objects.filter(id=self.dish_type.id).exists())

    def test_create_dish(self):
        response = self.client.post(reverse("restaurant:dish-create"), {
            "name": "TestDish",
            "description": "Test",
            "price": 15.5,
            "dish_type": self.dish_type.id,
            "cooks": [self.user.id]
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Dish.objects.filter(name="TestDish").exists())

    def test_update_dish(self):
        url = reverse("restaurant:dish-update", args=[self.dish.id])
        response = self.client.post(url, {
            "name": "UpdatedDish",
            "description": "Updated",
            "price": 10.0,
            "dish_type": self.dish_type.id,
            "cooks": [self.user.id]
        })
        self.dish.refresh_from_db()
        self.assertEqual(self.dish.name, "UpdatedDish")

    def test_delete_dish(self):
        url = reverse("restaurant:dish-delete", args=[self.dish.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Dish.objects.filter(id=self.dish.id).exists())

    def test_create_cook(self):
        url = reverse("restaurant:cook-create")
        response = self.client.post(url, {
            "username": "newcook",
            "password1": "strongpass123",
            "password2": "strongpass123"
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(get_user_model().objects.filter(username="newcook").exists())
