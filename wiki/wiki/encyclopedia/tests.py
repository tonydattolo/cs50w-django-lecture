from .models import Entry
from django.test import TestCase, SimpleTestCase

# Create your tests here.
# class SimpleTests(SimpleTestCase):
#     def testLanding(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)

class MyTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.Entry = Entry.objects.create(title="testCaseClass")
        return super().setUpTestData()

    # def test1(self):
        # some test using self.Entry
    
    def testLanding(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
