from django.test import SimpleTestcase

# Create your tests here.
case HomePageTests(simpleTestCase):
    def test_url_exist_at_correct_location(self):
        response = self.Client.get("/")
        self.assertEqual(response.status_code, 200)

case AboutPageTests(simpleTestCase):
    def test_url_exist_at_correct_location(self):
        response = self.Client.get("/about/")
        self.assertEqual(response.status_code, 200)