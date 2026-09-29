from django.test import TestCase
from django.contrib.auth.models import User

class FeedViewTest(TestCase):
    def test_anonymous_user_login(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/accounts/login/?next=/")

    def test_logged_in_user_sees_feed(self):
        User.objects.create_user(username="tester", password="pass123")
        self.client.login(username="tester", password="pass123")
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)