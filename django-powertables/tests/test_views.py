from django.test import RequestFactory, TestCase
from powertables.views import PowertableView

from .models import PowertableTestModel


class PowertableViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_that_view_response_with_200(self):
        request = self.factory.get("/")
        response = PowertableView.as_view(model=PowertableTestModel)(request)
        self.assertEqual(response.status_code, 200)

    def test_that_view_has_a_default_pagination_of_50(self):
        self.assertEqual(PowertableView.paginate_by, 50)
