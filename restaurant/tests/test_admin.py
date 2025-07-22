from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="testadmin",
        )
        self.client.force_login(self.admin_user)
        self.cook = get_user_model().objects.create_user(
            username="cook_user", password="testpass123"
        )
        self.cook.first_name = "John"
        self.cook.last_name = "Doe"
        self.cook.years_of_experience = 5
        self.cook.save()

    def test_years_of_experience_displayed_in_admin_list(self):
        """Check that years_of_experience is shown in admin list display"""
        url = reverse("admin:restaurant_cook_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.cook.years_of_experience)
        self.assertContains(response, self.cook.username)

    def test_years_of_experience_editable_in_admin(self):
        """Check that years_of_experience is on the admin form"""
        url = reverse("admin:restaurant_cook_change", args=[self.cook.id])
        response = self.client.get(url)

        self.assertContains(response, "years_of_experience")
