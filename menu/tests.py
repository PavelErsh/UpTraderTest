from django.test import TestCase
from django.urls import reverse
from menu.models import Menu, MenuItem


class MenuTestCase(TestCase):
    def setUp(self):
        # Создаем меню и пункты меню для тестов
        self.menu = Menu.objects.create(name="main_menu")
        self.home_item = MenuItem.objects.create(
            menu=self.menu, name="Home", url="/", order=1
        )
        self.about_item = MenuItem.objects.create(
            menu=self.menu, name="About", url="/about/", order=2
        )
        self.contact_item = MenuItem.objects.create(
            menu=self.menu, name="Contact", url="/contact/", order=3
        )

    def test_home_page_loads(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Home")

    def test_about_page_loads(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About")

    def test_contact_page_loads(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Contact")

    def test_menu_items_in_home_page(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Home")
        self.assertContains(response, "About")
        self.assertContains(response, "Contact")

    def test_active_menu_item(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, 'class="active"')
        self.assertContains(response, "Home")

        response = self.client.get(reverse("about"))
        self.assertContains(response, 'class="active"')
        self.assertContains(response, "About")

        response = self.client.get(reverse("contact"))
        self.assertContains(response, 'class="active"')
        self.assertContains(response, "Contact")

    def test_menu_item_with_children(self):
        child_item = MenuItem.objects.create(
            menu=self.menu,
            parent=self.about_item,
            name="Team",
            url="/about/team/",
            order=1,
        )
        response = self.client.get(reverse("about"))
        self.assertContains(response, "Team")
