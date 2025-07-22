from django.test import TestCase
from django.contrib.auth import get_user_model

from restaurant.forms import CookCreationForm, DishForm, DishSearchForm
from restaurant.models import DishType


class CookCreationFormTest(TestCase):
    def test_form_fields(self):
        form = CookCreationForm()
        self.assertIn("first_name", form.fields)
        self.assertIn("last_name", form.fields)
        self.assertIn("username", form.fields)
        self.assertIn("password1", form.fields)
        self.assertIn("password2", form.fields)


class DishFormTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Pizza")
        self.cook1 = get_user_model().objects.create_user(
            username="cook1", password="test123"
        )
        self.cook2 = get_user_model().objects.create_user(
            username="cook2", password="test123"
        )

    def test_form_fields(self):
        form = DishForm()
        self.assertIn("name", form.fields)
        self.assertIn("description", form.fields)
        self.assertIn("price", form.fields)
        self.assertIn("dish_type", form.fields)
        self.assertIn("cooks", form.fields)

    def test_form_valid_with_cooks(self):
        form_data = {
            "name": "Margherita",
            "description": "Classic Italian pizza",
            "price": "10.00",
            "dish_type": self.dish_type.id,
            "cooks": [self.cook1.id, self.cook2.id],
        }
        form = DishForm(data=form_data)
        self.assertTrue(form.is_valid())


class DishSearchFormTest(TestCase):
    def test_empty_form_is_valid(self):
        form = DishSearchForm(data={})
        self.assertTrue(form.is_valid())

    def test_search_field_present(self):
        form = DishSearchForm()
        self.assertIn("name", form.fields)
        self.assertEqual(form.fields["name"].label, "")
        self.assertEqual(
            form.fields["name"].widget.attrs["placeholder"], "Search dish name"
        )
