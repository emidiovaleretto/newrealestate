from django.test import TestCase

class TestHome(TestCase):
    def test_home_page_returns_status_code_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_hello_world(self):
        response = self.client.get("/")
        self.assertContains(response, "Hello, World!")
