from django.test import Client, TestCase
from django.urls import reverse

from .forms import EntryForm
from .models import Entry


class EntryFormTests(TestCase):
    def test_valid_form(self):
        form = EntryForm(data={"name": "Maria Santos", "message": "Great site, well done!"})
        self.assertTrue(form.is_valid())

    def test_blank_name_is_invalid(self):
        form = EntryForm(data={"name": "", "message": "Hello there"})
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)

    def test_blank_message_is_invalid(self):
        form = EntryForm(data={"name": "Juan", "message": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("message", form.errors)


class GuestbookViewTests(TestCase):
    def test_get_shows_unbound_form_with_csrf_token(self):
        response = self.client.get(reverse("guestbook"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_valid_post_saves_entry_and_redirects(self):
        response = self.client.post(
            reverse("guestbook"), {"name": "Ana Reyes", "message": "Hello from the lab!"}
        )
        self.assertRedirects(response, reverse("guestbook"))
        self.assertEqual(Entry.objects.count(), 1)

    def test_invalid_post_rerenders_with_errors_and_saves_nothing(self):
        response = self.client.post(reverse("guestbook"), {"name": "Ana Reyes", "message": ""})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["form"].errors)
        self.assertEqual(Entry.objects.count(), 0)

    def test_post_without_csrf_token_is_forbidden(self):
        strict_client = Client(enforce_csrf_checks=True)
        response = strict_client.post(
            reverse("guestbook"), {"name": "Ana Reyes", "message": "No token here"}
        )
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Entry.objects.count(), 0)
